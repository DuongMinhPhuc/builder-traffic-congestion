from rest_framework import serializers

from send.models.Infomation import Information


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'




