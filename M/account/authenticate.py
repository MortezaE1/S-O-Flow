from django.contrib.auth.models import User


class EmailBackend:

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            password_valid = user.check_password(password)
            if password_valid:
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

