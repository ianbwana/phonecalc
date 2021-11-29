import pandas as pd
from rest_framework import status
from call.models import CallLog
from rest_framework.decorators import api_view
from asgiref.sync import sync_to_async
from api.serializers.logs import CallLogSerializer
from rest_framework.response import Response

@sync_to_async
@api_view(['POST','GET'])
def call_log_list(request):

    '''
        This view is accepts a both GET and POST requests either returns a list of call logs or
        creates/updates a call log.
        '''
    if request.method == 'GET':
        logs = CallLog.objects.all()
        serializer = CallLogSerializer(logs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        data = request.data
        serializer = CallLogSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

