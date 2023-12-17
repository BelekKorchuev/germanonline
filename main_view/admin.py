from django.contrib import admin
from .models import OurInformations, ListOfLevels, ListOfTheme
# Register your models here.


class ThemeAdmin(admin.StackedInline):
	model = ListOfTheme


class LevelAdmin(admin.ModelAdmin):
	inlines = [ThemeAdmin]


admin.site.register(OurInformations)
admin.site.register(ListOfLevels, LevelAdmin)
admin.site.register(ListOfTheme)

