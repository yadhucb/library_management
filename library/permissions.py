from rest_framework.permissions import BasePermission
from library.models import User

class IsAdminOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_admin:
            return True