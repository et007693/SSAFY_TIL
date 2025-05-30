from rest_framework import serializers
from .models import Artist


class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = '__all__'

class ArtistsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ('name', 'debut_date', )