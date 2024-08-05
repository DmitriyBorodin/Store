from django.urls import path

from catalog.views import index, contact_info, product_details

urlpatterns = [
    path("", index),
    path("contacts/", contact_info),
    path("products/<int:pk>/", product_details, name='product_details')
]
