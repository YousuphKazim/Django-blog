from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, "index.html")

# Create your views here.
@login_required
def all_posts(request):
    posts = Post.objects.all().order_by('-created_at')
    print(posts)
    return render(request, 'posts.html', {"posts": posts})



@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('all_posts')
        else:
            print(form.errors)


    else:
        form = PostForm()
        
    
    return render(request, 'create_post.html', {'form': form})


def single_post(request, post_id):
    post = Post.objects.get(id=post_id)

    return render(request, 'single_post.html', {'post': post})


@login_required
def edit_post(request, post_id):

    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":

        form = PostForm(
            request.POST,
            request.FILES,
            instance=post
        )

        if form.is_valid():

            form.save()

            return redirect("all_posts")

    else:

        form = PostForm(instance=post)

    return render(
        request,
        "edit_post.html",
        {
            "form": form,
            "post": post
        }
    )

@login_required
def delete_post(request, post_id):

    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":

        post.delete()

        return redirect("all_posts")

    return render(
        request,
        "delete_post.html",
        {
            "post": post
        }
    )