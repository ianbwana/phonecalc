from django.core.cache import cache
from call.models import CallLog
from api.serializers.logs import CallLogSerializer


def generate_cache_key():
    key = "call_log_cache"
    return key

def refresh_call_log_cache(request):
    cache_key = "call_log_cache"
    print("refreshing call log cache")
    queryset = CallLog.objects.all()
    serializer = CallLogSerializer(queryset, many=True, context={"request": request})
    data = serializer.data
    cache.delete(cache_key)
    cache.set(cache_key, data, None)

def add_call_logs_to_cache():
    logs = CallLog.objects.all()
    serializer = CallLogSerializer(logs, many=True)
    data = serializer.data
    key = generate_cache_key()
    cache.delete(key)
    cache.set(key, data, None)
    return data