from rest_framework import serializers
from votes.models import QuestionUpVote, QuestionDownVote, AnswerUpVote, AnswerDownVote

class QuestionUpVoteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = QuestionUpVote
        fields = '__all__'

    def create(self, validated_data):
        return QuestionUpVote.objects.create(**validated_data, user=self.context['request'].user)

class QuestionDownVoteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = QuestionDownVote
        fields = '__all__'

    def create(self, validated_data):
        return QuestionDownVote.objects.create(**validated_data, user=self.context['request'].user)

class AnswerUpVoteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = AnswerUpVote
        fields = '__all__'

    def create(self, validated_data):
        return AnswerUpVote.objects.create(**validated_data, user=self.context['request'].user)

class AnswerDownVoteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = AnswerDownVote
        fields = '__all__'

    def create(self, validated_data):
        return AnswerDownVote.objects.create(**validated_data, user=self.context['request'].user)