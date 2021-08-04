from django.db import models
from django.conf import settings


class Post(models.Model):
    """Модель статьи"""
    title = models.CharField('заголовок статьи', max_length=50, blank=False)
    content = models.TextField('текст статьи', max_length=1000, blank=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='автор', on_delete=models.CASCADE)
    created_at = models.DateField('дата создания', auto_now=True)
    update_at = models.DateField('дата обновления', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'


class Comment(models.Model):
    """Модель комментария"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='пользователь', on_delete=models.CASCADE)
    text = models.TextField('текст комментариия', max_length=255, blank=False)
    parent = models.ForeignKey('self',
                               verbose_name='родительский комментарий',
                               blank=True, null=True,
                               related_name='comment_children',
                               on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name='пост', related_name='post_comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField('дата создания', auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.post} - {self.pk}"

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
