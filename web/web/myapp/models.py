from django.db import models

class Item(models.Model):
    title = models.CharField('Название', max_length=20)
    text = models.TextField('Описание')
    photo =models.ImageField('Фото', upload_to='photo/%Y/%m/')
    price = models.DecimalField('ЦЕна', max_digits= 10, decimal_places=2)
    data =models.DateField("Дата",auto_now_add=True)

    



# Create your models here.
