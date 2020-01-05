from django.utils.translation import ugettext
from rest_framework import status
from django.http import JsonResponse


def success_response(data=None, message=None, code=status.HTTP_200_OK):
    return JsonResponse({
        "message": message,
        "data": data
    }, status=code)


def error_response(errors=None, message=None, code=status.HTTP_422_UNPROCESSABLE_ENTITY):
    return JsonResponse({
        "errors": errors,
        "message": message
    }, status=code)


def page_not_found_view(request, exception):
    return JsonResponse({
        "errors": None,
        "message": ugettext("Page not found")
    }, status=status.HTTP_404_NOT_FOUND)