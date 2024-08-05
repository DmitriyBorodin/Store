from django.urls import path

from catalog.views import contact_info, product_details, product_list

app_name = 'catalog'

urlpatterns = [
    path("", product_list, name='product_list'),
    path("contacts/", contact_info),
    path("products/<int:pk>/", product_details, name='product_details'),
]
