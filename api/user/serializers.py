from rest_framework import serializers
from user.models import AskerProfile

class AskerProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = AskerProfile
        fields = '__all__'

    def create(self, validated_data):
        return AskerProfile.objects.create(**validated_data, user=self.context['request'].user)