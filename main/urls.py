from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('accounts', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='main_view/home.html'), name='home'),
    path('user/', include('user_profile.urls'), name='profile'),
]
