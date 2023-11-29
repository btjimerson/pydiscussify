from datetime import datetime
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from discussify.forms import PostForm, CommentForm
from discussify.models import Post

class PostListView(ListView):
    model = Post
    template_name = "discussify/post_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Posts / Discussify"
        context["table_title"] = "All Posts"
        return context
    
class PostDetailView(DetailView):
    model = Post
    template_name = "discussify/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "View Post / Discussify"
        context["comment_form"] = CommentForm(None)
        return context

class SearchListView(ListView):
    model = Post
    template_name = "discussify/post_list.html"

    def get_queryset(self):
        return Post.objects.filter(content__icontains=self.request.GET['searchTerm'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Search Results / Discussify"
        context["table_title"] = f"Search Results for '{self.request.GET['searchTerm']}'"
        return context

def new_post(request):
    form = PostForm(data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.post_date = datetime.now()
            post.save()
            return redirect("post_list")
        else:
            print(form.errors)
    else:
        return render(request, "discussify/post_form.html", {"title": "New Post / Discussify", "form": form})

def comment(request, pk):
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post_id = pk
        comment.comment_date = datetime.now()
        comment.save()
        return redirect("post_detail", pk=pk)
    else:
        print(form.errors)
