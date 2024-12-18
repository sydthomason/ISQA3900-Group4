from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            login(request, user)  # Log the user in
            return redirect('shop:product_list')  # Redirect to shop's product list
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})
