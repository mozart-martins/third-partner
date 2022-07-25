from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.utils import timezone


class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, user_name, name_coworker, password,
                         **other_fields):

        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Super user must be active, staff")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Super user must be active, staff")

        return self.create_user(email, user_name, name_coworker, password,
                                **other_fields)

    def create_user(self, email, user_name, name_coworker, password,
                    **other_fields):
        if not email:
            raise ValueError("You must provide an email address")

        email = self.normalize_email(email)
        user = self.model(
            email=email, user_name=user_name, name_coworker=name_coworker,
            **other_fields
        )
        user.set_password(password)
        user.save()
        return user


class CoworkerModel(AbstractBaseUser, PermissionsMixin):

    user_name = models.CharField(max_length=150, unique=True)
    name_pj = models.CharField(max_length=200, blank=False)
    name_coworker = models.CharField(max_length=100, blank=False)
    cnpj = models.CharField(max_length=17, blank=False)
    specialty = models.CharField(max_length=100, default="Developer")
    about = models.TextField(max_length=500, blank=True)
    email = models.EmailField(default="asd@asd.com", unique=True)
    phone_number = models.CharField(max_length=20, blank=False)
    whatsapp = models.BooleanField(default=True)
    address = models.CharField(max_length=300)
    working_place = models.CharField(max_length=200)
    start_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(default="profile.jpg",
                              upload_to="profile_picture")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['name_pj', 'name_coworker', 'email', 'phone_number']

    class Meta:
        verbose_name = "Colaborador"
        verbose_name_plural = "Colaboradores"

    def __str__(self) -> str:
        return f"{self.name_coworker}"
