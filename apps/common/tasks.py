from __future__ import absolute_import

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task(name='send_mail_async')
def send_mail_async(*args, **kwargs):
    """ Using celery to send email async

    You can use it as django send_mail function

    Example:
    send_mail_sync.delay(subject, message, from_mail, recipient_list, fail_silently=False, html_message=None)

    Also you can ignore the from_mail, unlike django send_mail, from_email is not a require args:

    Example:
    send_mail_sync.delay(subject, message, recipient_list, fail_silently=False, html_message=None)
    """
    if len(args) == 3:
        args = list(args)
        args[0] = settings.EMAIL_SUBJECT_PREFIX + args[0]
        args.insert(2, settings.EMAIL_HOST_USER)
        args = tuple(args)

    send_mail(*args, **kwargs)


# def send_mail_async(subject, message, from_mail, recipient_list, fail_silently=False, html_message=None):
#     if settings.CONFIG.MAIL_SUBJECT_PREFIX:
#         subject += settings.CONFIG.MAIL_SUBJECT_PREFIX
#     send_mail(subject, message, from_mail, recipient_list, fail_silently=fail_silently, html_message=html_message)
