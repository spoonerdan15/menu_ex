from django.db import models


class Menu(models.Model):

    LABELS = {
        'name': 'Name',
        'path': 'Link',
        'parent': 'Parent element'
    }

    class Meta:
        verbose_name = 'Menu item'

    name = models.CharField(LABELS['name'], max_length=255, blank=True, null=False)


    path = models.CharField(LABELS['path'], max_length=1000, blank=True, null=False)

    parent = models.ForeignKey(
        'self',
        verbose_name=LABELS['parent'],
        on_delete=models.SET_DEFAULT,
        null=True,
        blank=True,
        default=0
    )

    def __str__(self):
        return self.name

# Create your models here.
