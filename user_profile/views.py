from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from user_profile.forms import ProfileUserForm


# def view_profile(request):
#     context = {
#         'user': request.user
#     }
#     return render(request, 'user_profile/profile.html', context)

class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'user_profile/profile_update.html'

    def get_success_url(self):
        return reverse_lazy('user_profile:profile')

    def get_object(self, queryset=None):
        return self.request.user


def profile(request):
    context = {
        'username': request.user,
        'first_name': request.user,
        'last_name': request.user,
        'email': request.user,
    }
    return render(request, 'user_profile/profile.html', {'context':context})