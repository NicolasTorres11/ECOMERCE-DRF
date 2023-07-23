from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from datetime import timedelta, datetime
from django.utils import timezone
from django.conf import settings
from django.contrib.sessions.models import Session


class ExpiredTokenAuthentication(TokenAuthentication):
    expired = False

    def expires_in(self, token):
        if token is None:
            return timedelta(seconds=0)

        time_elapsed = timezone.now() - token.created
        left_time = timedelta(seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
        return left_time

    def is_token_expired(self, token):
        return self.expires_in(token) < timedelta(seconds=0)

    def token_expire_handler(self, token):
        is_expired = self.is_token_expired(token)
        if is_expired:
            self.expired = True
            user = token.user
            # all_session = Session.objects.filter(expire_date__gte=datetime.now())
            # if all_session.exists():
            #     for session in all_session:
            #         session_data = session.get_decoded()
            #         if user.id == int(session_data.get('_auth_user_id')):
            #             session.delete()
            token.delete()
            token = self.get_model().objects.create(user=user)
        return is_expired, token

    def authenticate_credentials(self, key):
        message, token, user = None, None, None
        try:
            token = self.get_model().objects.select_related('user').get(key=key)
            user = token.user
        except self.get_model().DoesNotExist:
            message = 'Token Invalido'
            self.expired = True

        if token is not None:
            if not token.user:
                message = 'Usuario Invalido o Inactivo'

            is_expired = self.token_expire_handler(token)
            if is_expired:
                message = 'Su Token y su Sesion ha Expirado'

        return token, user, message, self.expired
