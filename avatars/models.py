from django.db import models

from PIL import Image 
from io import BytesIO 
from django.core.files.base import ContentFile



class Avatar(models.Model):
    image = models.ImageField(upload_to='media/avatars/')
    is_main_image = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)

            if img.format != "WEBP":
                img_io = BytesIO()
                img.save(img_io, format='WEBP') 
                img_content = ContentFile(img_io.getvalue(), f'{self.image.name.split(".")[0]}.webp') 
                self.image.save(img_content.name, img_content, save=False)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Avatar {self.pk}"
