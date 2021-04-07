from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, Orderplaced
from .forms import CustomerRegistrationForm
from django.contrib import messages


def home(request):
    return render(request, 'app/home.html')


class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html', {'product': product})


def add_to_cart(request):
    return render(request, 'app/addtocart.html')


def buy_now(request):
    return render(request, 'app/buynow.html')


def profile(request):
    return render(request, 'app/profile.html')


def address(request):
    return render(request, 'app/address.html')


def orders(request):
    return render(request, 'app/orders.html')


def mobile(request):
    return render(request, 'app/mobile.html')


def login(request):
    return render(request, 'app/login.html')


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html',
                      {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(
                request, 'Congratulations!! Rgistered Successfully')
            form.save()
        return render(request, 'app/customerregistration.html',
                      {'form': form})


def checkout(request):
    return render(request, 'app/checkout.html')
