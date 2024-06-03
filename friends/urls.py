# friends/urls.py
from django.urls import path
from .views import SendFriendRequestView, FriendRequestsView, FriendsListView, SearchFriendsView,AcceptFriendRequestView,RejectFriendRequestView

urlpatterns = [
    path('send-request/<int:to_user_id>/', SendFriendRequestView.as_view(), name='send_friend_request'),
    path('requests/', FriendRequestsView.as_view(), name='friend_requests'),
    path('list/', FriendsListView.as_view(), name='friends_list'),
    path('search/', SearchFriendsView.as_view(), name='search_friends'),
    path('accept_request/<int:request_id>/', AcceptFriendRequestView.as_view(), name='accept_friend_request'),
    path('reject_request/<int:request_id>/', RejectFriendRequestView.as_view(), name='reject_friend_request')
]
