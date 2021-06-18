from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):


    def create_user(self, email, username, password=None):
        """Создание пользователя."""
        if not username:
            raise ValueError('У пользователя должен быть указан username')

        user = self.model(
            email=self.normalize_email(email),
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        """Создание суперпользователя."""
        user = self.create_user(
            email,
            username,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
