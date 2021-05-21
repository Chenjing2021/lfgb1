from django.urls import path

from . import views

urlpatterns = [
    # Leave as empty string for base url
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('comments/', views.comments, name="comments"),
    path('contact/', views.contact, name="contact"),
    path('category/', views.category, name="category"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),

]
