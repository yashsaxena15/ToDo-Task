from django.urls import path 
from todo import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.todopage,name='todo'),
    path('create_task/',views.create,name='create_task'),
    path('list_task/',views.list,name = 'list_task'),
    path('update_task/<int:pk>',views.update,name='update_task'),
    path('delete_task/<int:pk>',views.delete,name='delete_task'),
    
    path("register/",views.register, name = 'register'),
    path("login/",auth_views.LoginView.as_view(template_name ="todo/login.html"), name="login"),
    path("logout/",auth_views.LogoutView.as_view(next_page = "login"), name="logout"),

]
