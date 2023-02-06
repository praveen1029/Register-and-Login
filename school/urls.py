from . import views
from django.urls import path

urlpatterns = [
    path('',views.home_page,name='home'),
    path('register/form/',views.form_view,name ='register_form'),
    path('login/form/',views.student_login,name ='login_form'),

]
