from django.db import models
from django.contrib.auth.models import User
import datetime



class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    balance = models.IntegerField(default=1000)
    spend_money = models.IntegerField(default=0)
    discount = models.FloatField(default=0)
    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'

    def __str__(self):
        return self.user.username


class Music(models.Model):
    genre = models.CharField(max_length=30)
    class Meta:
        verbose_name = 'Музыка'
        verbose_name_plural = 'Музыка'


    def __str__(self):
        return self.genre


class FoodCategory(models.Model):
    name = models.CharField(max_length=30)
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(FoodCategory,on_delete=models.CASCADE,default=1)
    class Meta:
        verbose_name = 'Еда'
        verbose_name_plural = 'Еда'


    def __str__(self):
        return self.name


class Banquet(models.Model):
    date = models.DateField(default=datetime.date.today())
    music = models.ForeignKey(Music, on_delete=models.CASCADE,default=0)
    food = models.ManyToManyField(Food, related_name='banquets', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=0)
    money = models.IntegerField()
    people = models.IntegerField()
    is_approved = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'Банкет'
        verbose_name_plural = 'Банкеты'

    def __str__(self):
        return str(self.user)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'