from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MinLengthValidator


class playerManager(BaseUserManager):
    def create_user(self, email, name, phone, pimg, password=None):
        if not email:
            raise ValueError("email must be specified")
        if not phone:
            raise ValueError("phone must be specified")
        if not name:
            raise ValueError("name must be specified")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phone=phone,
            pimg=pimg
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, phone, pimg, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            name=name,
            phone=phone,
            pimg=pimg,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class player(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address", max_length=60, unique=True)
    name = models.CharField(verbose_name="name", max_length=200, unique=True)
    phone = models.CharField(verbose_name="phone", max_length=10, validators=[
                             MinLengthValidator(10)])
    pimg = models.FileField(upload_to="displaypic/",
                            default='defaultpic.png', null=True, max_length=250)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["name", "phone", "pimg"]

    objects = playerManager()

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Booking(models.Model):
    player = models.ForeignKey(player, on_delete=models.CASCADE)
    time = models.TimeField(verbose_name='time', blank=True)
    date = models.DateField(verbose_name='date', blank=True)
    bokked_d = models.DateTimeField(verbose_name='booked_d', null=True)

    def __str__(self):
        return self.player.name

# class Review(models.Model):
#     player=models.ForeignKey(player,on_delete=models.CASCADE)
#     rev=models.TextField(verbose_name='rev', blank=True)
#     rate=mo
