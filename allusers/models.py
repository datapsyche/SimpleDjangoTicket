from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.contrib.auth.models import PermissionsMixin

# Create your models here.
ROLES = (
    ('PUBLIC', 'PUBLIC'),
    ('EMPLOYEE', 'EMPLOYEE'),
    ('ADMIN', 'ADMIN'),
)


class allUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_public = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(('date joined'), auto_now_add=True)
    manager = models.ForeignKey('self', null=True, related_name="department_head", on_delete=models.DO_NOTHING, blank=True)
    role = models.CharField(max_length=50, choices=ROLES, default='PUBLIC')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def _str_(self):
        return f"<User : {self.first_name} {self.last_name}>"


