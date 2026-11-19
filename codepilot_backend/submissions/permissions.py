from rest_framework.permissions import BasePermission
from submissions.models import Submission

class OwnerOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user==obj.student