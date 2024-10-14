from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import View, DetailView, ListView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from cloudinary.forms import cl_init_js_callbacks
from django.utils.text import slugify
from django.contrib import messages
from django import forms
from .models import ImagePost
from .forms import CommentForm, ImagePostForm
import random
import string
import cloudinary


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
            # Retrieve the cleaned form data
            title = form.cleaned_data['title']
            slug = slugify(title)
            user = request.user
            author = user
            image = form.cleaned_data['image']
            location = form.cleaned_data['location']
           text = form.cleaned_data['text']

        # Save the image to Cloudinary
        response = cloudinary.uploader.upload(image)
        image_url = response['secure_url']

        # Check if a post with the same slug already exists
        while ImagePost.objects.filter(slug=slug).exists():
            # If it does, add a random string to the end of the slug
            random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
            slug = f"{slug}-{random_string}"

        # Create a new ImagePost object with the image URL
        ImagePost.objects.create(title=title, slug=slug, user=user, author=user, image=image_url, location=location, text=text, status=0)

        # add a success message
        messages.success(request, 'Post successfully uploaded!')

        return redirect('profile')
    return render(request, 'upload.html',)


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
