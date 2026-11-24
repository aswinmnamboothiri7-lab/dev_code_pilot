from submissions.models import Submission
from rest_framework import serializers

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Submission
        fields="__all__"
        read_only_fields=["id","student","start_time","created_at","updated_at"]