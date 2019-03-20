from django.views.generic import TemplateView, ListView
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *

# ++++++++++++++ MEAL VIEWS ++++++++++++++

class MealList(ListView):
	model = Meal
	template_name = "meals.html"

def create_meal_view (request):
	form = MealModelForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('/meals')
	context = {
		'form': form
	}

	return render(request, "create_meal.html", context)

# ++++++++++++++ EMPLOYEE VIEWS ++++++++++++++
class EmployeeList(ListView):
	model = Employee
	template_name = "employees.html"

def create_employee_view (request):
	form = EmployeeModelForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/employees')
	context = {
		'form': form
	}

	return render(request, "create_employee.html", context)

# ++++++++++++++ TABLE VIEWS ++++++++++++++
def create_table_view (request):
	form = TableModelForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/tables')
	context = {
		'form': form
	}

	return render(request, "tables.html", context)

# ++++++++++++++ ORDER VIEWS ++++++++++++++
class OrderList(ListView):
	model = Order
	template_name = "orders.html"

def order_view (request):
	form = OrderModelForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/meals')
	context = {
		'form': form
	}

	return render(request, "order_now.html", context)

def delete_order_view(request, id):
	item_to_delete = Order.objects.filter(pk=id)
	if item_to_delete.exists():
		item_to_delete[0].delete()
	return redirect('/orders')

def update_order_view(request, id):
	unique_order = get_object_or_404(Order, id=id)
	form = OrderModelForm(request.POST or None, instance=unique_order)
	if form.is_valid():
		form.save()
		return redirect('/orders')
	context = {
		'form': form
	}

	return render(request, "order_now.html", context)

# ++++++++++++++ OTHERS ++++++++++++++
class Help(TemplateView):
	template_name = "tips.html"

class Dashboard(TemplateView):
	template_name = "index.html"

class LoginPageView(TemplateView):
	template_name = "login.html"


class DevicesPageView(TemplateView):
	template_name = "devices.html"

class LockPageView(TemplateView):
	template_name = "lock_screen.html"







