from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView,UpdateView,DetailView, DeleteView
from django.urls import reverse_lazy

from .models import Address
from .forms import AddressForm

def 

class AddressCreate(CreateView):
    model = Address
    form_class = AddressForm
    context_object_name = 'CreatAddressForm'
    template_name = 'usuarios/addressForm.html'
    success_url = reverse_lazy('usuarios:listar')

class AddressList(ListView):
    model = Address
    template_name = 'usuarios/addressList.html'
    context_object_name = 'addresses'

class AddressUpdate(UpdateView):
    model = Address
    form_class = AddressForm
    context_object_name = 'address'
    template_name = 'usuarios/addressForm.html'
    success_url = reverse_lazy('usuarios:listar')

class AddressDetail(DetailView):
    model = Address
    context_object_name = 'address'
    template_name = 'usuarios/addressDetail.html'

class AddressDelete(DeleteView):
    model = Address
    template_name = 'usuarios/addressDelete.html'
    success_url = reverse_lazy('usuarios:listar')

   
# Create your views here.
