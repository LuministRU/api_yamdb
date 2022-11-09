from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, GroupViewSet, CommentsViewSet, FollowViewSet, ReviewsViewSet


router = DefaultRouter()

router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentsViewSet,
    basename=r'posts/(?P<post_id>\d+)/comments'
)
router.register(r'follow', FollowViewSet, basename='follow')
router.register(r'reviews', ReviewsViewSet, basename='reviews')

urlpatterns = [
    path(r'v1/', include(router.urls)),
    path(r'v1/', include('djoser.urls')),
    path(r'v1/', include('djoser.urls.jwt')),
]