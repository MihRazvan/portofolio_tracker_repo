# myapp/views.py
from django.shortcuts import render
from django.views.generic import ListView
from .models import MyModel

class MyModelListView(ListView):
    model = MyModel
    template_name = 'myapp/my_model_list.html'