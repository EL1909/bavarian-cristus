from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import View, DetailView, ListView, CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from cloudinary.forms import cl_init_js_callbacks
from django.utils.text import slugify
from django import forms
from .models import ImagePost
from .forms import CommentForm, ImagePostForm
import cloudinary


class PostList(ListView):
    model = ImagePost
    queryset = ImagePost.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(DetailView):

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


class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(ImagePost, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class UserProfile(LoginRequiredMixin, View):

    def get(self, request):
        user = request.user
        # queryset = ImagePost.objects.filter(status=1)
        image_posts = ImagePost.objects.filter(user=user)
        context = {'user': user, 'image_posts': image_posts, }
        return render(request, "profile.html", context)


@login_required
def upload(request):
    if request.method == "POST":
        title = request.POST.get('title')
        slug = slugify(title)
        user = request.user
        author = request.POST.get('user')
        image = request.FILES.get('image') # Use request.FILES to get the uploaded image
        location = request.POST.get('location')
        text = request.POST.get('text')
        status = 1

        # Save the image to Cloudinary
        response = cloudinary.uploader.upload(image)
        image_url = response['secure_url']

        # Create a new ImagePost object with the image URL
        ImagePost.objects.create(title=title, slug=slug, user=user, author=user, image=image_url, location=location, text=text, status=1)

        return redirect('profile')
    return render(request, 'upload.html',)


@login_required
def Post_edit(request, item_slug):
    return render(request, 'post_edit.html',)


def about(request):
    return render(request, 'about.html')
