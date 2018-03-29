from django.urls import path
from .views import FriendCreateView, FriendListView, FriendChartView

app_name = 'friends'
urlpatterns = [
    path('create/', FriendCreateView.as_view(), name = 'create'),
    path('data-chart/', FriendChartView.as_view(), name = 'data_chart'),
    path('', FriendListView.as_view(), name = 'list'),

]
