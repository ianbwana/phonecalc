from celery import shared_task
from call.models import CallLog
from djqscsv import write_csv
from django.core.mail import EmailMessage
import os
from io import StringIO






@shared_task(name="generate csv and email")
def generate_csv_send():
    emails = CallLog.objects.values('caller__email').all()
    weekly_logs_qs = CallLog.objects.values('id', 'rate_per_minute', 'duration', 'caller__first_name', 'caller__last_name').all()
    csvfile = StringIO()
    with open('logs.csv', 'wb') as csv_file:
        write_csv(weekly_logs_qs, csv_file)

    for email in emails:
        message = EmailMessage(
            "Your weekly report",
            "Heres a report generated about the calls you made",
            os.environ.get('EMAIL_HOST_USER'),
            [email['caller__email']]
        )
        message.attach('logs.csv', csvfile.getvalue(), 'text/csv')
        message.send()

generate_csv_send.delay()
