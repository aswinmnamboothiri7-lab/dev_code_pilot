from rest_framework.permissions import BasePermission

from assessments.models import Assessment

class AdminOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.creator