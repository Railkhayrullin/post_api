from django_filters import rest_framework as filters

from apps.post.models import Comment


class CommentLevelFilter(filters.FilterSet):
    level = filters.CharFilter(field_name='level', lookup_expr='lte')

    class Meta:
        model = Comment
        fields = ('level',)
