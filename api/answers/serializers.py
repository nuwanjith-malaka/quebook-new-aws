from rest_framework import serializers
from answer.models import Answer, AnswerComment

class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Answer
        fields = '__all__'

    def create(self, validated_data):
        return Answer.objects.create(**validated_data, user=self.context['request'].user)

class AnswerCommentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = AnswerComment
        fields = '__all__'

    def create(self, validated_data):
        return AnswerComment.objects.create(**validated_data, user=self.context['request'].user)