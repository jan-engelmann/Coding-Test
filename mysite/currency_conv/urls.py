from django.urls import path

from . import views
app_name = 'currency_conv'
urlpatterns = [
    path('calculator', views.calculator, name='calculator')
]