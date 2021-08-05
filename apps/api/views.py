from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics

from post_api.settings import ADD_COMMENTS_TO_POST
from apps.post.models import Post, Comment
from .filters import CommentLevelFilter
from .service import PaginationPosts
from .serializers import PostListSerializer, \
    PostDetailSerializer, \
    PostCreateSerializer, \
    CommentCreateSerializer, \
    PostCommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    """Вывод списка статей/конкретной статьи с комментариями/создание статьи"""
    pagination_class = PaginationPosts

    def get_queryset(self):
        if self.action == 'list':
            posts = Post.objects.all().prefetch_related('author')
        elif self.action == 'retrieve' and ADD_COMMENTS_TO_POST:
            posts = Post.objects.all().prefetch_related('post_comments__user').select_related('author')
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


class CommentsView(generics.ListAPIView):
    """Получение комментариев"""
    queryset = Comment.objects.all()
    serializer_class = PostCommentSerializer
    filter_backends = [DjangoFilterBackend, ]
    filter_class = CommentLevelFilter
    filterset_fields = ('level',)
