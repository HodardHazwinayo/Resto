from django.urls import path

from .views import *

urlpatterns = [
    path('', Dashboard, name='dashboard'),

    # links for meals
    path('meals/', MealList.as_view(), name='meals'),
    path('create_meal/', create_meal_view, name='create_meal'),
    path('meals/<id>/delete/', delete_meal_view, name='delete_meal'),
    path('meals/<id>/update/', update_meal_view, name='update_meal'),

    # links for employees
    path('employees/', EmployeeList.as_view(), name='employees'),
    path('create_employee/', create_employee_view, name='add_employee'),

    # links for tables
    path('tables/', create_table_view, name='tables'),
    path('tables/<id>/delete/', delete_table_view, name='delete_table'),
    path('tables/<id>/update/', update_table_view, name='update_table'),

    # links for orders
    path('orders/', OrderList.as_view(), name='orders'),
    path('order_now/', order_view, name='order_now'),
    path('orders/<id>/delete/', delete_order_view, name='delete_order'),
    path('orders/<id>/update/', update_order_view, name='update_order'),

    # links for meal categories
    path('meal_category/', MealCategoryList.as_view(), name='meal_category'),
    path('MealCategories/<id>/delete/', delete_mealcategory_view, name='delete_meal_category'),
    path('MealCategories/<id>/update/', update_mealcategory_view, name='update_meal_category'),

    # other links
    path('tips/', Help.as_view(), name='tips'),
    path('login/', LoginPageView.as_view(), name='login'),
    # path('devices/', DevicesPageView.as_view(), name='devices'),
    path('lock/', LockPageView.as_view(), name='lock'),
    path('menu/', Menu, name='menu'),

]