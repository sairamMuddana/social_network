from django.shortcuts import render

# Create your views here.
# friends/views.py
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FriendRequest, Friend
from .serializers import FriendRequestSerializer, FriendSerializer
from rest_framework import filters
from users.serializers import UserSerializer  # Import UserSerializer
from django.shortcuts import get_object_or_404



User = get_user_model()

class SendFriendRequestView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, to_user_id):
        to_user = User.objects.get(id=to_user_id)
        print(to_user)
        FriendRequest.objects.create(from_user=request.user, to_user=to_user)
        return Response({'message': 'Friend request send'}, status=201)

# class AcceptFriendRequestView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def post(self, request, request_id):
#         friend_request = FriendRequest.objects.get(id=request_id)
#         if friend_request.to_user == request.user:
#             friend_request.accept()
#             return Response(status=200)
#         else:
#             return Response({'error': 'You do not have permission to accept this friend request'}, status=status.HTTP_403_FORBIDDEN)

# class RejectFriendRequestView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def post(self, request, request_id):
#         friend_request = FriendRequest.objects.get(id=request_id)
#         if friend_request.to_user == request.user:
#             friend_request.reject()
#             return Response(status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'You do not have permission to reject this friend request'}, status=status.HTTP_403_FORBIDDEN)
 
class AcceptFriendRequestView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, request_id):
        friend_request = get_object_or_404(FriendRequest, id=request_id)
        if friend_request.to_user == request.user:
            friend_request.accept()
            return Response({'message': 'Friend request accepted'}, status=200)
        else:
            return Response({'error': 'You do not have permission to accept this friend request'}, status=403)

class RejectFriendRequestView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, request_id):
        friend_request = get_object_or_404(FriendRequest, id=request_id)
        if friend_request.to_user == request.user:
            friend_request.reject()
            return Response({'message': 'Friend request rejected'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'You do not have permission to reject this friend request'}, status=status.HTTP_403_FORBIDDEN) 
 
        
class FriendRequestsView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FriendRequestSerializer
    def get_queryset(self):
        return FriendRequest.objects.filter(to_user=self.request.user)

class FriendsListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FriendSerializer

    def get_queryset(self):
        return Friend.objects.filter(from_user=self.request.user)

class SearchFriendsView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email']