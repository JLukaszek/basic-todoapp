from django.urls import path
from .views import (
    HomePageView, EditPageView, DeletePageView, CreatePageView,
)

urlpatterns = [
    path('schedule/<int:pk>/edit/', EditPageView.as_view(),
         name='schedule_edit'),
    path('schedule/<int:pk>/delete/', DeletePageView.as_view(),
         name='schedule_delete'),
    path('schedule/new/', CreatePageView.as_view(), name='schedule_new'),
    path('', HomePageView.as_view(), name='home')
]
