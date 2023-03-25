from django.contrib.auth import get_user_model
from django.db import models

class Review(models.Model):
    author = models.ForeignKey(verbose_name='автор',to=get_user_model(), related_name='reviews', on_delete=models.CASCADE)
    product = models.ForeignKey(to='webapp.Product', related_name='reviews', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='текст_отзыва', max_length=2000, null=False,blank=False)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return f"{self.text} - {self.rating}"