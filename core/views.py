from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView 

# Create your views here.
class Dashboard(TemplateView):
	template_name = "index.html"

class MealsPageView(TemplateView):
	template_name = "meals.html"

