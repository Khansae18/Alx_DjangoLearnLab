from rest_framework import viewsets, permissions, filters
from rest_framework import generics, status
from .models import Post, Comment, Like
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .serializers import PostSerializer, CommentSerializer
from notifications.models import Notification
from notifications.utils import create_notification
from .serializers import NotificationSerializer



class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of a post/comment to edit or delete it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to anyone
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions only to the owner
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "content"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Get users that the current user follows
        following_users = request.user.following.all()

        # Get posts by those users
        posts = Post.objects.filter(author__in=following_users).order_by("-created_at")

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    class LikePostView(generics.GenericAPIView):
     permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            return Response({'detail': 'Already liked'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a notification
        create_notification(actor=request.user, recipient=post.author, verb='liked your post', target=post)
        return Response({'detail': 'Post liked'}, status=status.HTTP_201_CREATED)

class UnlikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(user=request.user, post=post)
        if like.exists():
            like.delete()
            return Response({'detail': 'Post unliked'}, status=status.HTTP_200_OK)
        return Response({'detail': 'You have not liked this post'}, status=status.HTTP_400_BAD_REQUEST)
    def create_notification(actor, recipient, verb, target=None):
     if actor != recipient:  # avoid self-notifications
        Notification.objects.create(
            actor=actor,
            recipient=recipient,
            verb=verb,
            target=target
        )

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-timestamp')
