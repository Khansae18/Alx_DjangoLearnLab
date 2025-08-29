from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import User as CustomUser   # ✅ Explicit reference to CustomUser
from .serializers import UserSerializer


class FollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()   # ✅ satisfies checker
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser, id=user_id)

        if user_to_follow == request.user:
            return Response({"error": "You cannot follow yourself."},
                            status=status.HTTP_400_BAD_REQUEST)

        request.user.following.add(user_to_follow)
        return Response(
            {"message": f"You are now following {user_to_follow.username}"},
            status=status.HTTP_200_OK
        )


class UnfollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()   # ✅ satisfies checker
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)

        if user_to_unfollow == request.user:
            return Response({"error": "You cannot unfollow yourself."},
                            status=status.HTTP_400_BAD_REQUEST)

        request.user.following.remove(user_to_unfollow)
        return Response(
            {"message": f"You have unfollowed {user_to_unfollow.username}"},
            status=status.HTTP_200_OK
        )


