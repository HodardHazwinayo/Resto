from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from core.models import Meal, Employee, Table, Order


# Create your views here.

class MealList(ListView):
	model = Meal
	template_name = "meals.html"

class EmployeeList(ListView):
	model = Employee
	template_name = "employees.html"

class TableList(ListView):
	model = Table
	template_name = "tables.html"

class OrderList(ListView):
	model = Order
	template_name = "orders.html"


class Dashboard(TemplateView):
	template_name = "index.html"

class LoginPageView(TemplateView):
    	template_name = "login.html"



class DevicesPageView(TemplateView):
    	template_name = "devices.html"

class LockPageView(TemplateView):
    	template_name = "lock_screen.html"

