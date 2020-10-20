from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import logout, authenticate, login

# Create your views here.

from django.shortcuts import render

from .models import Posts, UserRegistration
from .forms import NewUserForm, PostsForm
from django.views.generic import RedirectView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def home(request):
    user = False
    query = Posts.objects.all().order_by('-id')
    user_data=None
    if request.user.is_authenticated:
        user =True
        user_data = UserRegistration.objects.get(id=request.user.id)

    return render(request, 'home.html', {"user": request.user, "query": query,"user_data":user_data,"image":user})


def register(request):
    if request.method == "POST":

        form = NewUserForm(request.POST or None ,request.FILES or None)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("home")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request=request,
                          template_name="register.html",
                          context={"form": form})
    form = NewUserForm

    return render(request=request,
                  template_name="register.html",
                  context={"form": form})


def login_view(request):
    if request.method == 'POST':

        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request,
                  template_name="login.html",
                  context={"form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home")

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostsForm(request.POST)
        if form.is_valid():
            post = form.cleaned_data.get('post')
            title = form.cleaned_data.get('title')
            instance = Posts()
            instance.post = post
            instance.title = title
            instance.user = request.user
            instance.save()
            return redirect("home")

    form = PostsForm

    return render(request=request,
                  template_name="thoughts.html",
                  context={"form": form})


class PostLikeRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        ids = self.kwargs.get("id")
        print("ids", ids)
        obj = get_object_or_404(Posts, id=ids)
        user = self.request.user
        if user.is_authenticated():
            obj.likes.add(user)
        return ("home")


def post_view(request, id):
    # query = Posts.objects.get(id=id)
    liked = False
    query = get_object_or_404(Posts, id=id)
    if query.likes.filter(id=request.user.id).exists():
        print("exists")
        liked = True
    if request.user :
        print("fff")
    else:
        print("rfrf")
    return render(request, 'post_details.html', {"user": request.user, "query": query, "d":liked})

@transaction.atomic
def like_view(request, id):
    post = get_object_or_404(Posts, id=id)
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        print("already liked")
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post_detail',args=[str(id)]))
