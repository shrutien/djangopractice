from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    message = 'You must be owner of this content to change it.'
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.

        if request.method in permissions.SAFE_METHODS:  #SAFE METHODS= ('GET', 'HEAD', 'OPTIONS')
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.user == request.user


class AnonPermissionOnly(permissions.BasePermission):
    """
    Non-Authenticated Users only
    """
    message = 'You are already authenticated.'
    def has_permission(self, request, view):
        return not request.user.is_authenticated