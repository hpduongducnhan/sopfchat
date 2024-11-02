from django.urls import path
from . import views

urlpatterns = [
    path('fchat/<str:name>/<str:environment>/', views.fchat_website_view, name='fchat_website_view'),
]
