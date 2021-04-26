from django.shortcuts import render

# Create your views here.
# old
# from django.contrib.auth import get_user_model
# from django.contrib.auth.views import LoginView
# from django.shortcuts import render, get_object_or_404
# from django.urls import reverse_lazy
# from django.views import View
# from django.views.generic import CreateView
#
# from account.forms import RegistrationForm

# new
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
# from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Поздравляем, {username}, вы успешно создали аккаунт!')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'account/registration.html', {'form': form})

# old
# User = get_user_model()
#
#
# class RegistrationView(CreateView):
#     model = User
#     form_class = RegistrationForm
#     template_name = 'account/registration.html'
#     success_url = reverse_lazy("successful-registration")
#
#
# class SuccessRegistrationView(View):
#     def get(self, request):
#         return render(request, 'account/success_registration.html', {})
#
# # http://127.0.0.1:8000/account/activate/?u=2wad3r33r
# class ActivationView(View):
#     def get(self, request):
#         code = request.GET.get('u')
#         # try:
#         #     user = User.objects.get(activation_code=code)
#         # except User.DoesNotExist:
#         #     raise Http404
#         user = get_object_or_404(User, activation_code=code)
#         user.is_active = True
#         user.activation_code = ''
#         user.save()
#         return render(request, 'account/activation.html', {})
#
#
# class SigninView(LoginView):
#     template_name = 'account/login.html'
#     success_url = reverse_lazy('index-page')