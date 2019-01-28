from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
  template_name = 'core/index.html'


class IndexTownView(TemplateView):
  template_name = 'core/index_town.html'
# Create your views here.


class LoginView(TemplateView):
  template_name = 'core/login.html'


class NewLoginView(TemplateView):
  template_name = 'core/new_login.html'


class ManufactureView(TemplateView):
  template_name = 'core/manufacture.html'


class MasterView(TemplateView):
  template_name = 'core/master.html'
