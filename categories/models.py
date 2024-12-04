from django.db import models
from avatars.models import Avatar


class Category(models.Model):
    class CategoryType(models.TextChoices):
        MALE = "male", "Male"
        FEMALE = "female", "Female"
        COUPLE = "couple", "Couple"
        NEUTRAL = "Neural", "Neural"

    image = models.OneToOneField(Avatar, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=7, choices=CategoryType.choices, default=CategoryType.NEUTRAL)


    def __str__(self):
        return self.title