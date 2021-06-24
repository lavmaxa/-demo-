from django.urls import path
from . import views

urlpatterns = [
    path('rating',views.index, name='rating'),
    path('1sem', views.sem1, name='1sem'),
    path('2sem', views.sem2, name='2sem'),
    path('3sem', views.sem3, name='3sem'),
    path('4sem', views.sem4, name='4sem'),
    path('5sem', views.sem5, name='5sem'),
    path('6sem', views.sem6, name='6sem'),
    path('7sem', views.sem7, name='7sem'),
    path('8sem', views.sem8, name='8sem'),
    path('all', views.all, name='all'),
    path('rating_for_teacher',views.fillratings, name='rating_for_teacher'),
]