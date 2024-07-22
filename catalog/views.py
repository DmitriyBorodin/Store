from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def contact_info(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Пользователь - {name}\nНомер телефона - {phone}\nСообщение - {message}')
    return render(request, 'contact_info.html')
