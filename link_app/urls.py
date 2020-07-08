from django.contrib import admin
from django.urls import path
from links_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generate/', views.generate_short_url),
    path('all/', views.get_all_short_url),
    path('link/<str:url>/', views.get_long_url)
]
