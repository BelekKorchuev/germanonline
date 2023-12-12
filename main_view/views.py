from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import OurInformations, ListOfLevels, ListOfTheme


# Create your views here.

class AboutUs(generic.View):
    def get(self, request):
        creaters_list = OurInformations.objects.all()

        return render(request, 'main_view/about.html', {'creaters_list': creaters_list})

class LevelList(generic.View):
    def get(self, request):
        level_list = ListOfLevels.objects.all()

        return render(request, 'main_view/levels.html', {'level_list': level_list})

# class LevelDetail(generic.DetailView):
#     template_name = 'main_view/levels_detail.html'
#
#     def get_object(self, **kwargs):
#         level_id = self.kwargs.get('id')
#         return get_object_or_404(ListOfLevels, id=level_id)

def themes_for_level(request, level_id):
    level = get_object_or_404(ListOfLevels, pk=level_id)
    themes = ListOfTheme.objects.filter(choose_level=level)

    return render(request, 'main_view/level_detail.html', {'level': level, 'themes': themes})

