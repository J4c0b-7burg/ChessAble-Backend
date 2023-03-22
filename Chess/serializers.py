from .models import Chess
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class ChessSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

        model = Chess

        fields = ['id', 'title', 'date', 'type', 'notes', 'link', 'image']