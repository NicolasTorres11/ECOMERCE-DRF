import random
from twilio.rest import Client
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.base.models import Code
from apps.base.serializer.code_serializer import CodeSerializer


def send_verification_code(phone_number, code):
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    twilio_phone_number = settings.TWILIO_PHONE_NUMBER

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f'Tu código de verificación es: {code}',
        from_=twilio_phone_number,
        to=phone_number
    )

