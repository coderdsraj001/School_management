from django.urls import path
from django.conf import settings
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create-class', views.create_class, name="create_class"),
    path('edit-class/<int:id>', views.edit_class, name="edit_class"),
    path('delete-class/<int:id>', views.delete_class, name="delete_class"),  
    path('student/', views.student, name="student"),
    path('students/', views.show, name="show"),
    path('class/<int:pk>/class-wise-students/', views.class_wise_students, name='class_wise_students'),
    path('stu-edit/<int:id>', views.edit, name="edit"),  
    path('stu-delete/<int:id>', views.destroy, name="delete"),  
    path('teachers/', views.teacher_list, name="teacher_list"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
]
