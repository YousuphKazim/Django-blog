from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import ProfileForm

from post.models import Post


def register(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect("all_posts")

    else:

        form = UserCreationForm()

    return render(

        request,

        "register.html",

        {

            "form": form

        }

    )


@login_required
def profile(request):

    if request.method == "POST":

        form = ProfileForm(

            request.POST,

            instance=request.user

        )

        if form.is_valid():

            form.save()

            return redirect("profile")

    else:

        form = ProfileForm(

            instance=request.user

        )

    total_posts = Post.objects.count()

    return render(

        request,

        "profile.html",

        {

            "form": form,

            "total_posts": total_posts

        }

    )