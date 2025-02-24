from django.shortcuts import render, get_object_or_404
from django.views.generic import View, DetailView, ListView
from .models import ImagePost
from .forms import CommentForm


class PostList(ListView):
    model = ImagePost
    queryset = ImagePost.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(DetailView):

    model = ImagePost

    def get(self, request, slug, *args, **kwargs):
        queryset = ImagePost.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },

        )
