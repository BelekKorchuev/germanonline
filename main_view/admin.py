from django.contrib import admin
from .models import OurInformations, ListOfLevels, ListOfTheme
# Register your models here.

admin.site.register(OurInformations)
admin.site.register(ListOfLevels)
admin.site.register(ListOfTheme)