from rest_framework import viewsets
from rest_framework.response import Response

from apps.post.models import Post
from .serializers import PostListSerializer, PostDetailSerializer, CommentCreateSerializer, PostCreateSerializer
from .service import PaginationPosts


class PostViewSet(viewsets.ModelViewSet):
    """Вывод списка статей/конкретной статьи с комментариями/создание статьи"""
    pagination_class = PaginationPosts

    def get_queryset(self):
        if self.action == 'list':
            posts = Post.objects.all().prefetch_related('author')
        elif self.action == 'retrieve':
            posts = Post.objects.all().prefetch_related('post_comments__user')
        else:
            posts = Post.objects.all()
        return posts

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        elif self.action == 'retrieve':
            return PostDetailSerializer
        else:
            return PostCreateSerializer


class CommentCreateViewSet(viewsets.ModelViewSet):
    """Добавление комментария"""
    serializer_class = CommentCreateSerializer
