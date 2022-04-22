from functools import wraps
from rest_framework.response import Response

def has_permissions(permissions=[]):
    def decorator(func):
        @wraps(func)
        def _wrapped_view(instance, request, *args, **kwargs):
            required_permissions = [str(perm) for perm in permissions]
            if request.user.has_permissions(required_permissions):
                return func(instance, request, *args, **kwargs)
            else:
                return Response(data={'messege':'Permission denied'}, status=403)
        return _wrapped_view

    return decorator
