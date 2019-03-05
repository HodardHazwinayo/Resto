from django.urls import path
from django.views.generic import TemplateView

from .views import Dashboard,EmployeeList ,TableList , LockPageView ,MealList , LoginPageView, OrderList, DevicesPageView

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('meals/', MealList.as_view(), name='meals'),
    path('employees/', EmployeeList.as_view(), name='employees'),
    path('tables/', TableList.as_view(), name='tables'),
    path('orders/', OrderList.as_view(), name='orders'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('devices/', DevicesPageView.as_view(), name='devices'),
    path('lock/', LockPageView.as_view(), name='lock'),

]