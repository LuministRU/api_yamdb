from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Reviews(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [models.UniqueConstraint(
            Fields=['author, title'],
            name='unique_review')
        ]
        ordering = ('-created',)
