from rest_framework import viewsets, filters
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from django.shortcuts import get_object_or_404

from reviews.models import Group, Post, Follow
from .serializers import CommentSerializer
from .permission import AuthorAccessPermission
from rest_framework.pagination import LimitOffsetPagination


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AuthorAccessPermission, IsAuthenticatedOrReadOnly)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user, id=self.kwargs['post_id'])

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        post = get_object_or_404(Post, id=post_id)
        return post.comments