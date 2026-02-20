from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_http_methods, require_POST

from .forms import SignupForm, LoginForm


@never_cache
@require_http_methods(["GET", "POST"])
def login_view(request):
    form = LoginForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = authenticate(
            request,
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"],
        )
        if user is not None:
            login(request, user)
            return redirect("memo")

        form.add_error(None, "ユーザー名またはパスワードが正しくありません。")

    return render(request, "login/login.html", {"form": form})

@never_cache
@require_POST
def logout_view(request):
    logout(request)
    return redirect("home")


@require_http_methods(["GET", "POST"])
def signup(request):
    form = SignupForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("login")

    return render(request, "login/signup.html", {"form": form})
