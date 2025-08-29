from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Post, Like
from .serializers import PostSerializer, LikeSerializer
from notifications.utils import create_notification

# List all posts or create a post
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# Retrieve, update, delete a single post
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

# Like a post
class LikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            return Response({'detail': 'Already liked'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a notification for the post author
        create_notification(
            actor=request.user,
            recipient=post.author,
            verb='liked your post',
            target=post
        )
        return Response({'detail': 'Post liked'}, status=status.HTTP_201_CREATED)

# Unlike a post
class UnlikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(user=request.user, post=post)
        if like.exists():
            like.delete()
            return Response({'detail': 'Post unliked'}, status=status.HTTP_200_OK)
        return Response({'detail': 'You have not liked this post'}, status=status.HTTP_400_BAD_REQUEST)

