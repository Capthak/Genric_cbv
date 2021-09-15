from django.db import models
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import Laptop
from .forms import LaptopModelForm


class LaptopListView(ListView):
    model=Laptop

class LaptopCreateView(CreateView):
    model=Laptop
    form_class=LaptopModelForm
    success_url='/crud/list/'

class LaptopUpadateView(UpdateView):
    model=Laptop
    form_class=LaptopModelForm
    success_url='/crud/list/'

class LaptopDelete(DeleteView):
    model=Laptop
    success_url='/crud/list/'
