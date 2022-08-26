from rest_framework import serializers
from .models import StickynoteInput

class StickynoteInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = StickynoteInput
        fields = ('id', 'name', 'weblink', 'date', 'time', 'description')