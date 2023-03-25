from django.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    user = models.OneToOneField(to=get_user_model(), related_name='profile', on_delete=models.CASCADE, verbose_name='пользователь')
    avatar = models.ImageField(verbose_name='Аватар', null=True, blank=True, upload_to='avatars', )
    birthday = models.DateField(verbose_name='Дата рождения',null=True, blank=True,)

    def __str__(self):
        return self.user.get_full_name() + "'s Profile"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'













