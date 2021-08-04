from rest_framework import serializers
from apps.post.models import Post, Comment


class CommentCreateSerializer(serializers.ModelSerializer):
    """Добавление коментариев"""
    class Meta:
        model = Comment
        fields = '__all__'


class PostCommentSerializer(serializers.ModelSerializer):
    """Вывод коментариев"""
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comment
        exclude = ('post',)


class PostCreateSerializer(serializers.ModelSerializer):
    """Добавление статьи"""
    class Meta:
        model = Post
        fields = '__all__'


class PostListSerializer(serializers.ModelSerializer):
    """Вывод списка статей"""
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'author')


class PostDetailSerializer(serializers.ModelSerializer):
    """Вывод конкретной статьи с коментариями"""
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    post_comments = PostCommentSerializer(many=True)

    @classmethod
    def setup_eager_loading(cls, queryset):
        return queryset.prefetch_related('post_comments')

    class Meta:
        model = Post
        fields = '__all__'
