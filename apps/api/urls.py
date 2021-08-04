from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import PostViewSet, CommentCreateViewSet

urlpatterns = [
    path('post/create/', PostViewSet.as_view({'post': 'create'})),
    path('post/', PostViewSet.as_view({'get': 'list'})),
    path('post/<int:pk>/', PostViewSet.as_view({'get': 'retrieve'})),
    path('comment/create/', CommentCreateViewSet.as_view({'post': 'create'})),
]
