from rest_framework import serializers
from call.models import CallLog


class CallLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallLog
        fields = '__all__'




