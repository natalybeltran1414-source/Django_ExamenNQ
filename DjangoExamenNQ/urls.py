from django.contrib import admin
from django.urls import path
from Peliculas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("registry/", views.registry, name="registry"),
    path("signin/", views.signin, name="signin"),
    path('signout/', views.signout, name='signout'),
]
