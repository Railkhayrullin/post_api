from rest_framework import serializers

from post_api.settings import ADD_COMMENTS_TO_POST
from apps.post.models import Post, Comment


class CommentCreateSerializer(serializers.ModelSerializer):
    """Добавление коментария"""
    class Meta:
        model = Comment
        exclude = ('level',)

    def validate(self, data):
        """Валидация комментария и присваивание ему уровня по parent"""
        if data['parent']:
            if data['parent'].post != data['post']:
                raise serializers.ValidationError({'Error': 'Статья родителя комментария не '
                                                            'совпадает с выбранной статьей!'})
            else:
                data['level'] = data['parent'].level + 1
        return data


class PostCommentSerializer(serializers.ModelSerializer):
    """Вывод коментариев для статьи"""
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
    """Вывод конкретной статьи"""
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    if ADD_COMMENTS_TO_POST:
        post_comments = PostCommentSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'
