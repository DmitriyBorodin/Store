from django.shortcuts import render
from catalog.models import Product


def product_list(request):
    products = Product.objects.all()
    context = {"product_list": products}
    print(context)
    return render(request, 'product_details.html', context)


def contact_info(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"Пользователь - {name}\nНомер телефона - {phone}\nСообщение - {message}")
    return render(request, "contact_info.html")


def product_details(request, pk):
    product = Product.objects.get(pk=pk)
    context = {"product": product}
    return render(request, 'product_details.html', context)