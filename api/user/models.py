from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext as _
from autor.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email"), unique=True)
    username = models.CharField(_("username"), max_length=50, primary_key=True)
    data_joined = models.DateTimeField(_("data_joined"), auto_now_add=True)
    is_active = models.BooleanField(_("is_active"), default=True)
    is_staff = models.BooleanField(_("is_staff"), default=True)

    objects = UserManager()
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

    class Meta:
        verbose_name = _("username")
        verbose_name_plural = _("usernames")

    def get_name(self):
        return self.username.strip()
