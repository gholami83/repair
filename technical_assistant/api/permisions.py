from rest_framework import permissions
from pair.models import Pair


class IsAssistantConfirmed(permissions.BasePermission):
    def  has_object_permission(self, request, view,pairId):
        if Pair.objects.get(pairId).confimed_assistant:
            return True