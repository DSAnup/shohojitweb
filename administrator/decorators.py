from django.contrib.auth.decorators import permission_required
from functools import wraps
from django.shortcuts import render

def staff_or_permission_required(perm=None, login_url=None, raise_exception=False):
    """
    Decorator for views that checks if the user is staff.
    If the user is staff, access to the view is granted without permission checks.
    Otherwise, it delegates to the permission_required decorator.

    Usage:
    @staff_or_permission_required('app.change_model')
    def my_view(request):
        # View logic here
    """

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_staff:
                # If user is staff, grant access without further permission checks
                return view_func(request, *args, **kwargs)
            if isinstance(perm, (list, tuple)):
                for p in perm:
                    if request.user.has_perm(p):
                        return view_func(request, *args, **kwargs)
            else:
                # Delegate to permission_required decorator
                return permission_required(perm, login_url=login_url, raise_exception=raise_exception)(view_func)(request, *args, **kwargs)

        return _wrapped_view

    return decorator

def admin_only(view_func):
    """
    Decorator for views that checks that the user is staff.
    Usage:
    @admin_only
    def my_view(request):
        # View logic here
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        elif request.user.is_staff:
            return view_func(request, *args, **kwargs)
        elif request.user.userrole.role == 'admin':
            return view_func(request, *args, **kwargs)
        else:
            return render(request, '403.html', status=403)
    return _wrapped_view

def manager_only(view_func):
    """
    Decorator for views that checks that the user is manager or higher.
    Usage:
    @manager_only
    def my_view(request):
        # View logic here
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        elif request.user.is_staff:
            return view_func(request, *args, **kwargs)
        elif request.user.userrole.role in ['admin', 'manager']:
            return view_func(request, *args, **kwargs)
        else:
            return render(request, '403.html', status=403)
    return _wrapped_view


def staff_only(view_func):
    """
    Decorator for views that checks that the user is staff or higher.
    Usage:
    @staff_only
    def my_view(request):
        # View logic here
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        elif request.user.is_staff:
            return view_func(request, *args, **kwargs)
        elif request.user.userrole.role in ['admin', 'manager', 'staff']:
            return view_func(request, *args, **kwargs)
        else:
            return render(request, '403.html', status=403)
    return _wrapped_view

