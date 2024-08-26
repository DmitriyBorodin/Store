from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, \
    CreateView, UpdateView, DeleteView

from catalog.models import Product


class CatalogListView(ListView):
    model = Product

    # app_name/<model_name>_<action>
    # catalog/blog_list.html


class CatalogDetailView(DetailView):
    model = Product


class CatalogCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'preview', 'category', 'price')
    success_url = reverse_lazy('catalog:product_list')


class CatalogUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'preview', 'category', 'price')
    success_url = reverse_lazy('catalog:product_list')
    # def get_success_url(self):
    #     return reverse("catalog:product_list", args=[self.kwargs.get('pk')])


class CatalogDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class ContactsView(TemplateView):
    template_name = "catalog/contact_info.html"

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            name = request.POST.get("name")
            phone = request.POST.get("phone")
            message = request.POST.get("message")
            print(f"Пользователь - {name}\n"
                  f"Номер телефона - {phone}\nСообщение - {message}")

        return render(request, "catalog/contact_info.html")


# class CatalogCreateView(CreateView):
#     model = Product



# def product_list(request):
#     products = Product.objects.all()
#     context = {"product_list": products}
#     return render(request, 'blog_list.html', context)


# def contact_info(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         phone = request.POST.get("phone")
#         message = request.POST.get("message")
#         print(f"Пользователь - {name}\nНомер телефона - {phone}\nСообщение - {message}")
#     return render(request, "catalog/contact_info.html")


# def product_details(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {"product": product}
#     return render(request, 'blog_detail.html', context)
