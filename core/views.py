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

def delete_meal_view(request, id):
	item_to_delete = Meal.objects.filter(pk=id)
	if item_to_delete.exists():
		item_to_delete[0].delete()
	return redirect('/meals')

def update_meal_view(request, id):
	unique_meal = get_object_or_404(Meal, id=id)
	form = MealModelForm(request.POST or None, instance=unique_meal)
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
    tables = Table.objects.all()
    form = TableModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/tables')
    context = {
		'form': form,
        'object_list': tables
	}
    return render(request, "tables.html", context)

def delete_table_view(request, id):
	item_to_delete = Table.objects.filter(pk=id)
	if item_to_delete.exists():
		item_to_delete[0].delete()
	return redirect('/tables')

def update_table_view(request, id):
	unique_table = get_object_or_404(Table, id=id)
	form = TableModelForm(request.POST or None, instance=unique_table)
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

def Dashboard(request):
	orders = Order.objects.all()
	context = {
		'object_list': orders
	}

	return render(request, 'index.html', context)

def Menu(request):
    meals = Meal.objects.all()
    context = {
        'object_list': meals
    }

    return render(request, 'menu.html', context)

# ++++++++++++++++ MEAL CATEGORY VIEWS +++++++
class MealCategoryList(ListView):
	model = MealCategory
	template_name = "meal_category.html"

	def create_meal_category(request):
		form = MealCategoryModelForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			form.save()
			return redirect('/meal_category')
		context = {
			'form': form
		}

		return render(request, "meal_category.html", context)

def delete_mealcategory_view(request, id):
	item_to_delete = MealCategory.objects.filter(pk=id)
	if item_to_delete.exists():
		item_to_delete[0].delete()
	return redirect('/meal_category')

def update_mealcategory_view(request, id):
	unique_mealcategory = get_object_or_404(MealCategory, id=id)
	form = MealCategoryModelForm(request.POST or None, instance=unique_mealcategory)
	if form.is_valid():
		form.save()
		return redirect('/meal_category')
	context = {
		'form': form
	}

	return render(request, "meal_category.html", context)




