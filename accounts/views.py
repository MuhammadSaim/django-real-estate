from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from contacts.models import Contact


# Create your views here.
def dashboard(request):
    contacts = Contact.objects.order_by("-contact_date").filter(user_id=request.user.id)
    context = {
        'contacts': contacts
    }
    return render(request, "accounts/dashboard.html", context)


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is already exists.")
                return redirect("register")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email is already exists.")
                    return redirect("register")
                else:
                    user = User.objects.create(username=username, email=email, first_name=first_name, last_name=last_name)
                    user.set_password(password)
                    user.save()
                    messages.success(request, "Account is registered successfully.")
                    return redirect("login")
        else:
            messages.error(request, "Your password dose'nt match.")
            return redirect("register")
    return render(request, "accounts/register.html")


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "Your are logged in successfully.")
            return redirect("dashboard")
        else:
            messages.error(request, "Credentials are invalid.")
            return redirect("login")

    return render(request, "accounts/login.html")


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect("home")
    return redirect("home")
