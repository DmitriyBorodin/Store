from django.urls import path

from catalog.views import index, contact_info

urlpatterns = [
    path('', index),
    path('contacts/', contact_info),
]
