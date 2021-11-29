from call.models import CallLog
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from call.cache_utils import (
refresh_call_log_cache,
add_call_logs_to_cache
)

@receiver(post_save, sender=CallLog)
def refresh_cache(sender, instance=None, created=False, **kwargs):
    add_call_logs_to_cache()
    print('refreshed')


@receiver(post_delete, sender=CallLog)
def remove_call_from_cache(sender, instance=None, created=False, **kwargs):
    try:
        refresh_call_log_cache()
        print("refreshed")
    except:
        pass