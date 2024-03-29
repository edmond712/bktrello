from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MyUserManager(BaseUserManager):
    def create_user(self, phone, username, password=None):
        user = self.model(
            phone=phone,
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, username, password=None):
        user = self.create_user(
            phone=phone,
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    username = models.CharField(
        max_length=123,
        unique=True
    )
    email = models.EmailField(
        unique=True,
        blank=True,
        null=True
    )
    phone = models.CharField(
        unique=True,
        max_length=30,
    )
    avatar = models.ImageField(
        upload_to='media/avatars',
        blank=True,
        null=True
    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )
    is_admin = models.BooleanField(
        default=False
    )

    objects = MyUserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ('username', )

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Task(models.Model):
    title = models.CharField(
        max_length=200
    )
    description = models.TextField(
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    due_date = models.DateField()
    completed = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.title

