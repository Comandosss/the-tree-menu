from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True,
        blank=True, related_name='children'
    )
    menu = models.ForeignKey(
        Menu, blank=True, related_name='items', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
