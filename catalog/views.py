from django.shortcuts import render, get_object_or_404
from catalog.models import Product


def product_list(request):
    products = Product.objects.all()
    context = {"product_list": products}
    return render(request, 'product_list.html', context)


def contact_info(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"Пользователь - {name}\nНомер телефона - {phone}\nСообщение - {message}")
    return render(request, "contact_info.html")


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'product_details.html', context)