from django.db import models
from ckeditor.fields import RichTextField

def image_upload_path(instance, filename):
        return f"static/eventos/img/{filename}"

class Page(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    image1 = models.ImageField(verbose_name="Imagen 1", null=True, upload_to=image_upload_path)
    image2 = models.ImageField(verbose_name="Imagen 2", null=True, upload_to=image_upload_path)
    image3 = models.ImageField(verbose_name="Imagen 3", null=True, upload_to=image_upload_path)
    image4 = models.ImageField(verbose_name="Imagen 4", null=True, upload_to=image_upload_path)
    image5 = models.ImageField(verbose_name="Imagen 5", null=True, upload_to=image_upload_path)
    image6 = models.ImageField(verbose_name="Imagen 6", null=True, upload_to=image_upload_path)
    content = models.TextField(verbose_name="Contenido")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['-created', '-updated']

    def __str__(self):
        return self.title
