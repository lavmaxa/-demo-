from django.urls import path
from . import views
urlpatterns = [
    path('',views.my_view,name='main'),
    path('about',views.about, name='about'),
    path('register', views.register, name='register'),
    path('vedomost', views.vedomost, name='vedomost'),
    path('all_student_group', views.all_student_group, name='all_student_group'),
]
