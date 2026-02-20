# models.py
from django.db import models
from django.conf import settings

class Memo(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="memos",
    )
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likescount = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class Like(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="likes",
    )
    memo = models.ForeignKey(
        Memo,
        on_delete=models.CASCADE,
        related_name="likes",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'memo'], 
                name='unique_like_per_user_per_memo'
            )
        ]