from rest_framework import serializers
from movielist_app.models import WatchList, StreamPlatform, Review

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review      
        fields = "__all__"

class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only= True)
    class Meta:
        model = WatchList
        fields = "__all__"



class StreamPlatformSerializer(serializers.ModelSerializer): 
    
    watchlist = WatchListSerializer(many=True, read_only= True)
    #watchlist = serializers.StringRelatedField(many=True)
    #serializers.HyperlinkedRelatedField(
    #    many=True,
    #    read_only=True,
    #    view_name='movie-detail'
    #)

    class Meta:
        model = StreamPlatform
        fields = "__all__"