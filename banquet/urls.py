from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login',views.login, name = 'login'),
    path('login_failed', views.login_failed, name = 'login_failed'),
    path('login/register', views.register, name = 'register'),
    path('main', views.main, name = 'main'),
    path('person', views.person, name = 'person'),
    path('person/edit', views.edit_person, name = 'person_edit'),
    path('person/add_balance', views.add_balance, name = 'person'),
    path('person/banquets', views.banquets, name = 'banquets'),
    path('create', views.create_banquet, name = 'create'),
    path('comment', views.leave_comment, name = 'comment'),
    path('invite', views.invite, name = 'invite')
]