from rest_framework.permissions import BasePermission




class AdminOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        
<<<<<<< HEAD
        return request.user == obj.creator
=======
        return request.user == obj.creator





>>>>>>> 666863c11b68235bec8d9eba0ee954ed67988ba4
