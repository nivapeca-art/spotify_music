from rest_framework import serializers
from .models import User, MusicPreference

class UserSerializer(serializers.ModelSerializer):
    preferences = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'preferences']


class MusicPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicPreference
        fields = "__all__"
        read_only_fields = ["top_tracks"]
