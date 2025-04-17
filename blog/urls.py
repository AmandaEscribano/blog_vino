from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blogs/nuevo/', views.create_blog, name='create_blog'),
    path('accounts/signup/', views.signup_view, name='signup'),
    path('pages/', views.pages_view, name='pages'),
    path('blogs/<int:pk>/editar/', views.edit_blog, name='edit_blog'),
    path('blogs/<int:pk>/eliminar/', views.delete_blog, name='delete_blog'),

]
