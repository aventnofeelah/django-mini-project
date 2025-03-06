from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainRender, name='main_path'),
    path('registration/', views.registrationRender, name='register_path'),
    path('login/', views.loginRender, name='login_path'),
    path('logout/', views.logoutView, name='logout_path'),
    path('profile/<int:user_id>/', views.profileRender, name='profile_path'),
    path('profile/<int:user_id>/add-product', views.add_productRender, name='add_product_path'),

]
