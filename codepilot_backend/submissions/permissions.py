from rest_framework.permissions import BasePermission



class OwnerOnly(BasePermission):

    def has_object_permission(self, request, view, obj):

        return request.user==obj.student



class SubmissionAdminOnly(BasePermission):

    def has_permission(self, request, view):

        return request.user.is_superuser

# class SubmissionAdminOnly(BasePermission):

#     def has_permission(self, request, view):

#         return request.user.is_authenticated and request.user.creator




