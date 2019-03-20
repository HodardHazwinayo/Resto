from django.urls import path

from .views import *

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('tips/', Help.as_view(), name='tips'),
    path('meals/', MealList.as_view(), name='meals'),
    path('employees/', EmployeeList.as_view(), name='employees'),
    path('tables/', create_table_view, name='tables'),
    path('orders/', OrderList.as_view(), name='orders'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('devices/', DevicesPageView.as_view(), name='devices'),
    path('lock/', LockPageView.as_view(), name='lock'),
    path('create_meal/', create_meal_view, name='create_meal'),
    path('order_now/', order_view, name='order_now'),
    path('orders/<id>/delete/', delete_order_view, name='delete_order'),
    path('orders/<id>/update/', update_order_view, name='update_order'),
    path('create_employee/', create_employee_view, name='add_employee'),

]