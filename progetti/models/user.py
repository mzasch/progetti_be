from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Reference dei campi
    # - id
    # - username
    # - first_name, last_name
    # - password
    # - email
    # - is_staff, is_active, is_superuser
    # - date_joined, last_login

    def __str__(self):
        return self.last_name + " " + self.first_name
