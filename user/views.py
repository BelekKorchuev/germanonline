from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserAuthenticated, UserRegistration


# Create your views here.

class LoginUser(LoginView):
    form_class = UserAuthenticated
    template_name = 'user/login.html'

    # def get_success_url(self):
    #     return reverse_lazy('home')

def logout(request):
    logout(request)
    return render(request, 'user/login.html')


class RegisterUser(CreateView):
    form_class = UserRegistration
    template_name = 'user/signup.html'
    success_url = reverse_lazy('users:login')

# def signup(request):
#     if request.method == 'POST':
#         form = UserRegistration(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             return render(request, 'user/signup_done.html')
#     else:
#         form = UserRegistration()
#     return render(request, 'user/signup.html', {'form': form})




