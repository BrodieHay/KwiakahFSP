from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='stewardshipProgram-home'),
    path('primary', views.primary, name='stewardshipProgram-primary'),
    path('preschool', views.preschool, name='stewardshipProgram-preschool'),
    path('toddler', views.toddler, name='stewardshipProgram-toddler'),
    path('resources', views.resources, name='stewardshipProgram-resources'),

]
