from django.db import models

# Create your models here.
class OurInformations(models.Model):
    name = models.CharField(max_length=20,)
    role = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'information'
        verbose_name_plural = 'informations'


class ListOfLevels(models.Model):
    level = models.CharField(max_length=15)
    description = models.TextField(max_length=2000)


    def __str__(self):
        return self.level

    class Meta:
        verbose_name = 'level'
        verbose_name_plural = 'levels'

class ListOfTheme(models.Model):
    choose_level = models.ForeignKey(ListOfLevels, on_delete=models.CASCADE)
    theme = models.CharField(max_length=500)

    def __str__(self):
        return self.theme

    class Meta:
        verbose_name = 'theme'
        verbose_name_plural = 'themes'
