from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from send.models.Infomation import Information
from send.serializers.serializer import InformationSerializer


class InformationView(APIView):

    def get(self, request, format=None):
        informations = Information.objects.all()
        serializer = InformationSerializer(informations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InformationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)