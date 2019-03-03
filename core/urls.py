from django.urls import path
from django.views.generic import TemplateView

from .views import Dashboard, MealsPageView

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('meals/', MealsPageView.as_view(), name='meals'),
]