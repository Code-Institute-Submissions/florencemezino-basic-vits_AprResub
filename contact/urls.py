from django.urls import path
from . import views
from contact import views as contact_views

urlpatterns = [
    path('', views.contact_view, name='contact_view'),
]
