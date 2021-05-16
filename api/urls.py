from django.urls import path
from .import views

urlpatterns = [
    # path('',views.api,name="api"),
    path('comm-list/', views.showall, name='comm-list'),
    path('comm-detail/<int:pk>/', views.viewcomm, name='comm-detail'),
    path('comm-add/', views.addcomm, name='comm-add'),
    path('comm-delete/<int:pk>/', views.deletecomm, name='comm-delete'),
]