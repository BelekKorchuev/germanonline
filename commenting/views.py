# comments/views.py
from django.shortcuts import render

from .forms import CommentForm


# def comments(request):
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = CommentForm()
#     comment = Comment.objects.all()
#     return render(request, 'main_view/home.html', {'form': form, 'comment': comment})
