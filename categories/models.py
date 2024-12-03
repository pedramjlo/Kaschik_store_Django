from django.db import models


class Category(models.Model):
    class CategoryType(models.TextChoices):
        MALE = "male", "Male"
        FEMALE = "female", "Female"
        COUPLE = "couple", "Couple"
        NEUTRAL = "Neural", "Neural"

    title = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=7, choices=CategoryType.choices, default=CategoryType.NEUTRAL)


    def __str__(self):
        return self.title