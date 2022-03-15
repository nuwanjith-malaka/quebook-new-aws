from rest_framework import serializers
from question.models import Question, QuestionComment

class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Question
        fields = '__all__'

    def create(self, validated_data):
        return Question.objects.create(**validated_data, user=self.context['request'].user)

class QuestionCommentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = QuestionComment
        fields = '__all__'

    def create(self, validated_data):
        return Question.objects.create(**validated_data, user=self.context['request'].user)