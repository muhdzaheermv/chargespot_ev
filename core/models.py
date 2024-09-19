from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe

class Category(models.Model):
    cid=ShortUUIDField(unique=True,length=10,max_length=10,prefix="CCS2",alphabet="abcdefghijklm")
    title=models.CharField(max_length=100)
    image = models.ImageField(upload_to="Category")

    class Meta:
        verbose_name_plural = "Categories"

    def category_image(self):
        return mark_safe('<img src="%s width="50" height="50>' % {self.image})
