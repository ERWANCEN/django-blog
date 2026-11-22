from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "Brouillon"
        PUBLISHED = "published", "Publié"

    title = models.CharField("titre", max_length=200)
    slug = models.SlugField("slug", max_length=200, unique=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="posts",
        verbose_name="auteur",
    )
    content = models.TextField("contenu")
    status = models.CharField(
        "statut",
        max_length=10,
        choices=Status.choices,
        default=Status.DRAFT,
    )
    published_at = models.DateTimeField("date de publication", default=timezone.now)
    created_at = models.DateTimeField("date de création", auto_now_add=True)
    updated_at = models.DateTimeField("date de modification", auto_now=True)

    class Meta:
        ordering = ["-published_at"]
        indexes = [
            models.Index(fields=["-published_at"]),
        ]
        verbose_name = "article"
        verbose_name_plural = "articles"

    def __str__(self):
        return self.title
