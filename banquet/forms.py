from django import forms
from .models import *


class AuthForm(forms.Form):
    login = forms.CharField(label = 'Логин',max_length = 30)
    password = forms.CharField(label = 'Пароль',max_length = 30,
                                widget = forms.PasswordInput())


class RegisterForm(forms.Form):
    login = forms.CharField(label = 'Логин',max_length = 30)
    password = forms.CharField(label = 'Пароль',max_length = 30,
                                widget = forms.PasswordInput())
    email = forms.EmailField(label='Email')

class EditPersonForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=30)
    surname = forms.CharField(label = 'Фамилия',max_length = 30)


class AddBalanceForm(forms.Form):
    balance = forms.IntegerField()


class CreateForm(forms.Form):
    musics = Music.objects.all().values_list( 'id', 'genre')
    #foods = Food.objects.all().values_list('id', 'name')
    date = forms.DateField(label='Дата проведение',initial=datetime.date.today, widget=forms.SelectDateWidget())
    music = forms.CharField(label='Музыка',widget=forms.Select(choices=musics))
    #foods = Food.objects.all().values_list('id','name')
    food = forms.MultipleChoiceField(label='Еда',choices=Food.objects.all().values_list('id','name'))
    money = forms.IntegerField(label='Стоимость')
    people = forms.IntegerField(label='Персоны',min_value=10)


class CommentForm(forms.Form):
    title = forms.CharField(label='Заголовок', max_length=30)
    text = forms.CharField(label='Отзыв', max_length=300)


class InviteForm(forms.Form):
    emails = forms.CharField(max_length=150)
    text = forms.CharField(max_length=100)