from django.urls import path

from . import views
app_name = 'currency_conv'
urlpatterns = [
    path('', views.index, name='index'),
    #path('<int:currency_id>/', views.detail, name='detail'),
    path('<int:currency_id>/converted/', views.converted, name='converted'),
    path('<int:currency_id>/converted/show_result/', views.show_result, name='show_result'),

]