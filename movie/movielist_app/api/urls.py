from django.urls import path, include
from rest_framework.routers import DefaultRouter
from movielist_app.api.views import WatchListAV, WatchDetailAV,StreamPlatformVS, StreamPlatformAV, StreamPlatformDetailAV, ReviewList, ReviewCreate, ReviewDetail


router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name = 'movie-list'),
    path('<int:pk>', WatchDetailAV.as_view(), name = 'movie-detail'),
    path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-detail'),

    path('', include(router.urls)),


    path('stream/<int:pk>/review/', ReviewList.as_view(), name='review-list'),
    path('stream/<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),

    #path('review/', ReviewList.as_view(), name = 'revie_list'),
    #path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
]