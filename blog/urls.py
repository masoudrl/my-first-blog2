from django.urls import path
from . import views
urlpatterns = [
    path('',views.post_list,name='post_list'),
    path('jm1/',views.jm,name='jm'),
    path('post_details/<int:pk>',views.post_details,name='pd'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
