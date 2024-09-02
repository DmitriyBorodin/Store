import secrets

from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, TemplateView

from catalog.forms import StyleMixin
from users.forms import UserRegisterForm
from users.models import User

from config.settings import EMAIL_HOST_USER


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email-confirm/{token}/"
        send_mail(
            subject="Подтверждение почты",
            message=f"Добрый день, перейдите по ссылке чтобы подтвердить почту {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


class UserPasswordResetView(PasswordResetView, StyleMixin):
    form_class = PasswordResetForm
    template_name = "users/password_reset.html"
    success_url = reverse_lazy("users:password_reset")

    def form_valid(self, form):
        email = form.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
            if user:
                password = User.objects.make_random_password(length=8)
                user.set_password(password)
                user.save()
                send_mail(
                    subject="Ресет пароля",
                    message=f"Ваш новый пароль - {password}",
                    from_email=EMAIL_HOST_USER,
                    recipient_list=[email]
                )
            return redirect(reverse('users:login'))
        except:
            return redirect(reverse('users:mail_not_found'))


class NoMailView(TemplateView):
    template_name = "users/mail_not_found.html"


