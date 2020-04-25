from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = RegisterForm()

    return render(request, "register/register.html", {"form":form})

# def logout_view(request):
#     logout(request)
    # Redirect to a success page.
    # return redirect("register/logout.html")

# def login(request):
#     return render(request, "registration/login.html")
    # redirect("/login")
