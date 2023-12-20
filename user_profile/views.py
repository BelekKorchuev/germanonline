from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from lesson.utils import get_level_progress
from user_profile.forms import ProfileUserForm
from user_profile.models import ThemeProgress
from main_view.models import ListOfTheme, ListOfLevels


class ProfileUser(UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'user_profile/profile_update.html'

    def get_success_url(self):
        return reverse_lazy('user_profile:profile')

    def get_object(self, queryset=None):
        return self.request.user


def profile(request):
    user_progress = ThemeProgress.objects.filter(user=request.user)
    levels = ListOfLevels.objects.all()
    level_progress = []

    for level in levels:
        progress = get_level_progress(request.user, level)
        level_progress.append({'level': level, 'progress': progress})

    context = {
        'username': request.user.username,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email,
        'level_progress': level_progress,
    }
    return render(request, 'user_profile/profile.html', context)


#
# def view_progress(request):
#     user_progress = ThemeProgress.objects.filter(user=request.user)
#     return render(request, 'user_profile/profile.html', {'user_progress': user_progress})