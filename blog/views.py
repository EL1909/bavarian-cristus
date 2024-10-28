from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import slugify
from django.utils.text import slugify
from django.views.generic import View, DetailView, ListView
from .models import ImagePost, Payment
from .forms import CommentForm, ImagePostForm
import cloudinary
import json
import requests



class sendPostcardView(View):
    def post(self, request, *args, **kwargs):
        # Parse the incoming JSON data
        data = json.loads(request.body)
        
        # Extracting data from the request
        from_name = data.get('from_name')
        from_street1 = data.get('from_street1')
        from_street2 = data.get('from_street2')
        from_city = data.get('from_city')
        from_state = data.get('from_state')
        from_postcode = data.get('from_postcode')
        from_country = data.get('from_country')
        to_name = data.get('to_name')
        to_street1 = data.get('to_street1')
        to_street2 = data.get('to_street2')
        to_city = data.get('to_city')
        to_state = data.get('to_state')
        to_postcode = data.get('to_postcode')
        to_country = data.get('to_country')
        image_url = data.get('image_url')  # URL of the image for the postcard
        message = data.get('message')  # Message to be printed on the postcard
       
        # ClickSend API endpoint and credentials
        url = 'https://rest.clicksend.com/v3/post/postcards/send'
        auth = (settings.CLICKSEND_USERNAME, settings.CLICKSEND_API_KEY)

        # Prepare the payload with the extracted data
        payload = {
            "messages": [
                {
                    "file_url": image_url,
                    "recipients": [
                        {
                            "name": to_name,
                            "address_line_1": to_street1,
                            "address_line_2": to_street2,
                            "city": to_city,
                            "state": to_state,
                            "postal_code": to_postcode,
                            "country": to_country
                        }
                    ],
                    "sender": {
                        "name": from_name,
                        "address_line_1": from_street1,
                        "address_line_2": from_street2,
                        "city": from_city,
                        "state": from_state,
                        "postal_code": from_postcode,
                        "country": from_country
                    },
                    "message": message  # Optional: message to be printed on the postcard
                }
            ]
        }

        headers = {'Content-Type': 'application/json'}

        # Make the request to ClickSend API
        response = requests.post(url, json=payload, auth=auth, headers=headers)

        # Handle the response from ClickSend
        if response.status_code == 200:
            return JsonResponse({'status': 'success', 'message': 'Postcard sent!'})
        else:
            return JsonResponse({'status': 'error', 'message': response.json()})


class handlePaymentView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        order_id = data.get('orderId')
        status = data.get('status', 'pending')
        slug = data.get('slug')
        payer = data.get('payer')

        print("Received orderId:", order_id)
        if not order_id:
            return JsonResponse({'error': 'Order ID is missing'}, status=400)
                
        print("Received payer:", data.get('payer'))
        # Fallback to signed-in user for payer
        if not payer:
            payer = request.user if request.user.is_authenticated else None

        # Get the associated post using the slug
        post = get_object_or_404(ImagePost, slug=slug)

        # Create or update the payment object
        payment, created = Payment.objects.update_or_create(
            transaction_id=order_id,
            defaults={'status': status,
                      'post': post, 
                      'payer': payer,
            }
        )

        if created:
            message = 'Payment created successfully'
        else:
            message = 'Payment updated successfully'

        return JsonResponse({'status': 'success', 'message': message})


class postList(ListView):
    model = ImagePost
    queryset = ImagePost.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class postDetail(DetailView):

    model = ImagePost

    def get(self, request, slug, *args, **kwargs):
        queryset = ImagePost.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        context = {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            }
        return render(request, "post_detail.html", context,)

    def post(self, request, slug, *args, **kwargs):
        queryset = ImagePost.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.image_post = post
            comment.user = request.user
            comment.save()
        else:
            comment_form = CommentForm()
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class postLike(LoginRequiredMixin, View):
    def post(self, request, slug):
        post = ImagePost.objects.get(slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return redirect('post_detail', slug=slug)


class userProfile(LoginRequiredMixin, View):
    def get(self, request):
        user = self.request.user
        image_posts = ImagePost.objects.filter(user=user)
        context = {'user': user, 'image_posts': image_posts, }
        return render(request, "profile.html", context)


class authorProfile(LoginRequiredMixin, View):
    def get(self, request, username):
        author = get_object_or_404(User, username=username)
        image_posts = ImagePost.objects.filter(author=author)
        context = {'author': author, 'image_posts': image_posts, }
        return render(request, "profile.html", context)


@login_required
def upload(request):
    if request.method == "POST":
        form = ImagePostForm(request.POST, request.FILES)
        if form.is_valid():
            image_post = form.save(commit=False)
            image_post.user = request.user
            image_post.author = request.user
            image_post.status = 1

            # Save the image to Cloudinary
            response = cloudinary.uploader.upload(request.FILES['image'])
            image_post.image = response['secure_url']

            # Generate a Excerpt from text
            # image_post.excerpt = image_post.text

            # Generate a unique slug
            image_post.slug = slugify(image_post.title)
            image_post.save()

            messages.success(request, 'Post successfully uploaded!')
            return redirect('profile')
    else:
        form = ImagePostForm()

    return render(request, 'upload.html', {"form": form},)

@login_required
def Post_edit(request, item_slug):
    item = get_object_or_404(ImagePost, slug=item_slug, user=request.user)
    if request.method == 'POST':
        # include request.FILES in the form
        form = ImagePostForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            # Save the form data without committing to the database yet
            post = form.save(commit=False)
            # Check if a new image was uploaded
            if 'image' in request.FILES:
                # Save the image to Cloudinary
                image = request.FILES['image']
                response = cloudinary.uploader.upload(image)
                image_url = response['secure_url']
                # Update the image URL in the database
                post.image = image_url
            # Save the post to the database
            post.save()
            # add a success message to the messages framework
            messages.success(request, 'Post successfully Edited')
            return redirect('profile')
    else:
        form = ImagePostForm(instance=item)
    context = {
        "form": form
    }
    return render(request, 'post_edit.html', context)


@login_required
def delete(request, item_slug):
    item = get_object_or_404(ImagePost, slug=item_slug, user=request.user)

    if request.method == 'POST':
        # Check if the user has confirmed the deletion
        if request.POST.get('delete'):
            item.delete()
            # add a success message to the messages framework
            messages.success(request, 'Post deleted')
            return redirect('profile')
    else:
        # Render the confirmation template
        return render(request, 'confirm_delete.html', {'item_slug': item_slug})


@login_required
def confirm_delete(request, item_slug):
    item = get_object_or_404(ImagePost, slug=item_slug, user=request.user)
    return render(request, 'confirm_delete.html', {'item': item})


def about(request):
    return render(request, 'about.html')


def handler404(request, exception):
    """
    Custom 404 page
    """
    return render(request, "errors/404.html", status=404)


def handler500(request):
    """
    Custom 500 page
    """
    return render(request, "errors/500.html", status=500)


def handler403(request, exception):
    """
    Custom 403 page
    """
    return render(request, "errors/403.html", status=403)


def handler405(request, exception):
    """
    Custom 405 page
    """
    return render(request, "errors/405.html", status=405)


