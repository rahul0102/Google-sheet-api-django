from django.urls import path
from .views import FriendCreateView, FriendListView

app_name = 'friends'
urlpatterns = [
    path('create/', FriendCreateView.as_view(), name = 'create'),
    path('', FriendListView.as_view(), name = 'list'),

]
