from rest_framework import serializers
from question.models import Question
class QuestionSerializers(serializers.ModelSerializer):

    class Meta :

        modle = Question

        fields = '__all__'

        read_only_fields = ['id','created_at','updated_at']