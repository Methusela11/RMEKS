from django.contrib.auth.decorators import login_required
from django.core.mail import BadHeaderError, send_mail
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

from methusela import settings
from rmeks.models import ContactMessage


def home(request):
    return render(request,'index.html')

def cv(request):
    return render(request,'cv.html')

def services(request):
    return render(request,'services.html')

def about(request):
    return render(request,'about.html')

def projects(request):
    return render(request,'projects.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        try:
            # ✅ Save to database
            ContactMessage.objects.create(
                name=name,
                email=email,
                message=message
            )

            # ✅ Display success popup
            messages.success(request, "✅ Your message has been sent successfully!")

        except BadHeaderError:
            messages.error(request, "❌ Invalid header found.")
        except Exception as e:
            messages.error(request, f"❌ Something went wrong: {e}")

        return redirect("contact")

    return render(request, "contact.html")


def login_page(request):
    return None

