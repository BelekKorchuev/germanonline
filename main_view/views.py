from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import OurInformations, ListOfLevels, ListOfTheme, Comment
from .forms import CommentForm
# Create your views here.


class AboutUs(generic.View):
    def get(self, request):
        creaters_list = OurInformations.objects.all()

        return render(request, 'main_view/about.html', {'creaters_list': creaters_list})


class LevelList(LoginRequiredMixin, generic.View):
    login_url = 'users:login'

    def get(self, request):
        level_list = ListOfLevels.objects.all()

        return render(request, 'main_view/levels.html', {'level_list': level_list})


class ThemesForLevel(generic.View):

    def get(self, request, level_id):
        level = get_object_or_404(ListOfLevels, pk=level_id)
        themes = ListOfTheme.objects.filter(choose_level=level)

        return render(request, 'main_view/level_detail.html', {'level': level, 'themes': themes})


def comments(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main_view/home.html')
    else:
        form = CommentForm()
    comment = Comment.objects.all()
    return render(request, 'main_view/home.html', {'form': form, 'comment': comment})
