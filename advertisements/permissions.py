from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return request.user == obj.user