from django.urls import path
from . import views
urlpatterns =[
path('', views.index , name='index'),
path('home/', views.index, name='home'),
path('contact/', views.contact , name='contact'),
path('about/', views.aboutus , name='about'),
path('donate/', views.donate, name ='donate'),
path('gallery/', views.gallery, name='gallery'),
path('success/', views.success, name='success'),
path('visitus/', views.visitus, name='visitus'),
path('successvisit/', views.visitusaction, name='visitusaction'),
]
