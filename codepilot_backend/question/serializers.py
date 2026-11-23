from rest_framework import serializers
from .models import Question

class QuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']