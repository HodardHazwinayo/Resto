from django import forms
from .models import *

class MealModelForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['title', 'description', 'category', 'price']

class OrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['Table', 'Meal', 'note', 'waiter']

class TableModelForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ['name','note']

class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'phone', 'email', 'serving_Tables']

class MealCategoryModelForm(forms.ModelForm):
    class Meta:
        model = MealCategory
        fields = ['name', 'description']