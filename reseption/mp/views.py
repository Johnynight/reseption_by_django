from django.shortcuts import render
from .forms import Form_mp
from django.views.generic import DetailView, ListView, TemplateView, CreateView


class Main(CreateView):
    form_class = Form_mp
    template_name = 'mp/index.html'