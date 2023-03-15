# Django - models import:
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Celery - application import:
from autocli2.celery import app

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet

class CeleryRegisteredTasks(ViewSet):
    """
    Xxx.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Xxx.
        """
        try: # Try to collect Celery related data:
            celery_data = app.control.inspect().report()
        except: # Return false if the process has failed:
            celery_data = False
        result = {
            'page_results': celery_data}
        # Prepare API response:
        return JsonResponse(result, status=200)

# View functions:
@csrf_exempt
def get_celery_report(request):
    try: # Try to collect Celery related data:
        celery_data = app.control.inspect().report()
    except: # Return false if the process has failed:
        celery_data = False
    result = {
        'page_results': celery_data}
    # Prepare API response:
    return JsonResponse(result, status=200)

@csrf_exempt
def get_celery_stats(request):
    try: # Try to collect Celery related data:
        celery_data = app.control.inspect().stats()
    except: # Return false if the process has failed:
        celery_data = False
    # Prepare API return response:
    result = {
        'page_results': celery_data}
    # Prepare API response:
    return JsonResponse(result, status=200)

@csrf_exempt
def get_celery_registered_tasks(request):
    try: # Try to collect Celery related data:
        celery_data = app.control.inspect().registered()
    except: # Return false if the process has failed:
        celery_data = False
    # Prepare API return response:
    result = {
        'page_results': celery_data}
    # Prepare API response:
    return JsonResponse(result, status=200)

@csrf_exempt
def get_celery_reserved_tasks(request):
    try: # Try to collect Celery related data:
        celery_data = app.control.inspect().reserved()
    except: # Return false if the process has failed:
        celery_data = False
    # Prepare API return response:
    result = {
        'page_results': celery_data}
    # Prepare API response:
    return JsonResponse(result, status=200)

@csrf_exempt
def get_celery_revoked_tasks(request):
    try: # Try to collect Celery related data:
        celery_data = app.control.inspect().revoked()
    except: # Return false if the process has failed:
        celery_data = False
    # Prepare API return response:
    result = {
        'page_results': celery_data}
    # Prepare API response:
    return JsonResponse(result, status=200)

@csrf_exempt
def get_celery_scheduled_tasks(request):
    try: # Try to collect Celery related data:
        celery_data = app.control.inspect().scheduled()
    except: # Return false if the process has failed:
        celery_data = False
    # Prepare API return response:
    result = {
        'page_results': celery_data}
    # Prepare API response:
    return JsonResponse(result, status=200)
