from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import ContactsView, CatalogDetailView, CatalogListView, \
    CatalogCreateView, CatalogUpdateView, CatalogDeleteView

app_name = 'catalog'

urlpatterns = [
    path("", CatalogListView.as_view(), name='product_list'),
    path("contacts/", ContactsView.as_view()),
    path("products/<int:pk>/", cache_page(60)(CatalogDetailView.as_view()), name='product_detail'),
    path('create/', CatalogCreateView.as_view(), name='product_create'),
    path('<int:pk>/update/', CatalogUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete/', CatalogDeleteView.as_view(), name='product_delete'),
]
