from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product, Category
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.shortcuts import redirect
from .forms import UserRegistrationForm
from .forms import ContactForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product-list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect('product-list')
    else:
        form = ContactForm()
    return render(request, 'store/contact.html', {'form': form})


def home(request):
    return render(request, 'home.html')



class ProductListView(ListView):
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'products'
    paginate_by = 10

class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product_detail.html'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'store/product_form.html'
    fields = ['name', 'description', 'price', 'image', 'category', 'is_active']

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'store/product_form.html'
    fields = ['name', 'description', 'price', 'image', 'category', 'is_active']

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'store/product_confirm_delete.html'
    success_url = reverse_lazy('product-list')

# Create your views here.
