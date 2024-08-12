from django.urls import path

from catalog.views import ContactsView, CatalogDetailView, CatalogListView

app_name = 'catalog'

urlpatterns = [
    path("", CatalogListView.as_view(), name='product_list'),
    path("contacts/", ContactsView.as_view()),
    path("products/<int:pk>/", CatalogDetailView.as_view(), name='product_detail'),
]
