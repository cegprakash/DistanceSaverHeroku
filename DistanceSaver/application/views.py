# pages/views.py
from django.views.generic import TemplateView

from rest_framework import generics
from rest_framework import status

from DistanceSaver.application.DistanceSerializer import DistanceSerializer
from DistanceSaver.application import json_response

# from application.DistanceSerializer import DistanceSerializer
# from application import json_response


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
            return json_response.error_response(errors=format_form_errors(serializer.errors.items()))

        validated_data = serializer.validated_data
        # print(validated_data)
        #DistanceClass.distance = validated_data['distance']

        f = open("storage.txt", "w")
        f.write(str(validated_data['distance']))
        f.close()

        # print(DistanceClass.distance)

        return json_response.success_response(message="created", code=status.HTTP_200_OK)

    def get(self, request):
        f = open("storage.txt", "r")
        distance = int(f.read())
        f.close()
        return json_response.success_response(message="", data={'distance': distance}, code=status.HTTP_200_OK)