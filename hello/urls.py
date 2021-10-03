from django.urls import path
from . import views
urlpatterns = [
    path('', views.view_salam,name='view_salam'),
    path('bye/', views.bye,name='view_bye'),
    path('f/', views.print_factorial,name='print_factorial'),
    path('fib/', views.print_fibonachi,name='print_fibonachi'),
    path('fib/<int:m>/', views.print_fibonachiN,name='print_fibonachi'),
    path('details/', views.details,name='details'),

]

