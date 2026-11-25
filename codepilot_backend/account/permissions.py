from rest_framework.permissions import BasePermission

from account.models import StudentProfile

class OwnerOnly(BasePermission):

    def has_object_permission(self, request, view, obj):

        return request.user ==obj.student


# from rest_framework.permissions import BasePermission

# class OwnerOnly(BasePermission):

#     def has_object_permission(self, request, view, obj):

#         print("Logged-in user ID:", request.user.id)
#         print("Profile student ID:", obj.student.id)
#         print("User role:", request.user.role)

#         return request.user == obj.student