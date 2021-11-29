from django.db import models
from django.conf import settings
# Create your models here.


class CallLog(models.Model):
    caller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        help_text='Customer who made the call',
        related_name='logs',
        on_delete=models.DO_NOTHING,
        null=False,
        blank=False
    )
    rate_per_minute = models.DecimalField(
        decimal_places=7,
        max_digits=12,
        null=False,
        blank=False
    )
    # Will use fixed number of minutes or will round to the nearest while calculating total cost of call
    duration = models.DecimalField(
        decimal_places=7,
        max_digits=12,
        null=False,
        blank=False
    )
    prefix = models.CharField(
        max_length=10,
        null=False,
        blank=False

    )

