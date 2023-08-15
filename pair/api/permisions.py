from rest_framework import permissions
from ..models import Pair



class IsAssistantConfirmed(permissions.BasePermission):
    def  has_object_permission(self, request, view,obj):
        if Pair.objects.get(obj).assistant_confirm:
            return True
