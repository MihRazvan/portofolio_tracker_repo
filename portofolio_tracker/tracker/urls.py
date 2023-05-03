from django.urls import path
from tracker import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/<int:portfolio_id>/', views.dashboard, name='dashboard'),
    path('transactions/', views.transactions, name='transactions'),
    path('settings/', views.settings, name='settings'),
    path('api/transactions/', views.Transaction, name='Transaction'),
    path('add_crypto/', views.add_crypto, name='add_crypto')
    
]