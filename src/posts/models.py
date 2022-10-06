from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify 
from django.urls import reverse

# posts/models.py
User = get_user_model()


class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_on = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name="Publié")
    content = models.TextField(blank=True, verbose_name="Contenu")

    def get_absolute_url(self):
        return reverse("posts:home")

    @property
    def author_or_default(self):
        return self.author.username if self.author else "L'auteur inconnu"


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

        print(self.slug)
