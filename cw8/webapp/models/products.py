from django.db import models



class Product(models.Model):
    CATEGORY_CHOICES = [
        ('FOOTBALL', 'football'),
        ('BASKETBALL', 'basketball'),
        ('BOX', 'box'),
    ]

    name = models.CharField(verbose_name='название', max_length=200, null=False, blank=False)
    category = models.CharField(verbose_name='категория',max_length=100, choices=CATEGORY_CHOICES, null=False, blank=False)
    description = models.TextField(verbose_name='описание', max_length=2000,blank=True, null=True)
    picture = models.ImageField(verbose_name='изображение', upload_to='images/', default='images/default.png', blank=True)

    def __str__(self):
        return self.name