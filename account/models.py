from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import uuid


class AccountManager(BaseUserManager):

    # Parameters must include USERNAME_FIELD and REQUIRED_FIELDS defined in Account
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address.")
        if not username:
            raise ValueError("Users must have a username.")
        user = self.model(email=self.normalize_email(email),
                          username=username,
                          )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email=email, username=username, password=password)
        if not password:
            raise ValueError("Superuser must have a password")
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email           = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username        = models.CharField(max_length=30, unique=True)
    avatar          = models.ImageField(upload_to='account/img/{0}/'.format(uuid.uuid4()), default=None, null=True)

    date_joined     = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name="last login", auto_now=True)

    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_admin        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)

    street          = models.CharField(max_length=50, blank=True, null=True)
    zip_code        = models.CharField(max_length=10, blank=True, null=True)
    city            = models.CharField(max_length=50, blank=True, null=True)
    country         = models.CharField(max_length=50, blank=True, null=True)

    # USERNAME_FIELD is used to log in
    USERNAME_FIELD  = "email"

    # REQUIRED_FIELDS must be filled in addition to USERNAME_FIELD to register an account.
    REQUIRED_FIELDS = ["username", ]

    # Tells custom user model (Account) the name of its manager.
    objects = AccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
