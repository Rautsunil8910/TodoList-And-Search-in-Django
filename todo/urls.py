from collections import namedtuple
from django.urls import path
from .import views

urlpatterns = [ 
    path('',views.home,name='home'),
    path('update/<int:i>',views.update_data,name='update'),
    path('delete/<int:i>',views.delete_data,name='delete'),
    path('search/',views.search,name='search'),

]