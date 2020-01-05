# pages/views.py
from django.views.generic import TemplateView

from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

from DistanceSaver.application import DistanceSerializer, DistanceClass


def format_form_errors(data):
    result = []
    for param, message in data:
        result.append({"param": param, "message": message[0]})
    return result


class HomePageView(TemplateView):
    template_name = 'home.html'


class DistanceView(generics.GenericAPIView):
    serializer_class = DistanceSerializer

    def post(self, request):
        serializer = DistanceSerializer(data=request.data)

        if not serializer.is_valid():
            return Response.error_response(errors=format_form_errors(serializer.errors.items()))

        validated_data = serializer.validated_data
        DistanceClass.distance = validated_data.distance
        print(DistanceClass.distance)

        return Response.success_response(message="created", code=status.HTTP_200_OK)

    def get(self, request):
        return Response.success_response(message="", data=DistanceClass.distance, code=status.HTTP_200_OK)