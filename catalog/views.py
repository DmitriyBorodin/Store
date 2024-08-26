from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, \
    CreateView, UpdateView, DeleteView

from catalog.forms import CatalogForm, VersionForm
from catalog.models import Product, Version


class CatalogListView(ListView):
    model = Product

    # app_name/<model_name>_<action>
    # catalog/blog_list.html


class CatalogDetailView(DetailView):
    model = Product


class CatalogCreateView(CreateView):
    model = Product
    form_class = CatalogForm
    success_url = reverse_lazy('catalog:product_list')


class CatalogUpdateView(UpdateView):
    model = Product
    form_class = CatalogForm
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(
            Product, Version, VersionForm, extra=1)

        if self.request.method == 'POST':
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

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
