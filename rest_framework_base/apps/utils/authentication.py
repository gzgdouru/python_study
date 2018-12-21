from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib.auth.hashers import check_password

User = get_user_model()


class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            # if check_password(password, user.password):
            if user.check_password(password):
                return user
        except Exception as e:
            print(str(e))
            return None
