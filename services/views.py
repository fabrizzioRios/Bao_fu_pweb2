from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import login
from services.forms import SupplierForm
from django.views import generic
from services.models import Supplier
from services.forms import UserForm


# Create your views here.
class SupplierList(generic.ListView):
    model = Supplier
    context_object_name = "supplier_list"
    template_name = "supplier_list.html"


def profile(request):
    return render(request, 'profile.html')

def home(request):
    return render(request, 'home.html')


def menu(request):
    return render(request, 'menu.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def supplier_register(request):
    form_supplier = SupplierForm()
    if request.method == 'POST':
        form_supplier = SupplierForm(request.POST)
        form_supplier.save()
    return render(request, 'supplier.html', {'form': form_supplier})


def signup(request):
    if request.method == 'POST':
        form_user = UserForm(request.POST)
        if form_user.is_valid():
            user = form_user.save()
            user.refresh_from_db()
            user.save()
            login(request, user)
            subject = 'Bienvenido a la familia Bao Fu!'
            message = f'Hola {user.username}!, estamos contentos de tenerte con nosotros <a href="http://127.0.0.1/">login<a>'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail(subject, message, email_from, recipient_list)
            return redirect('login')
    else:
        form_user = UserForm()
    return render(request, 'signup.html', {"form": form_user})

