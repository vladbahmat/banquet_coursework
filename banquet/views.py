import datetime

from django.shortcuts import render
from .forms import AuthForm, EditPersonForm, AddBalanceForm, CreateForm, CommentForm, RegisterForm, InviteForm
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Food, Customer, Banquet, Music, Comment
from django.contrib.auth.hashers import check_password, make_password
from django.core.mail import send_mail

login_user = ''

def index(request):
    return render(request,'index.html')

def service():
    f = open('user.txt', 'r')
    return int(f.read())

def login(request):
    if request.method == "POST":
        users = User.objects.all()
        login = request.POST.get("login")
        password = request.POST.get("password")
        for elem in users:
            if elem.username == login and check_password(password,elem.password):
                if not elem.is_staff:
                    f  = open('user.txt', 'w')
                    f.write(str(elem.id))
                    return render(request, 'main.html')
                else:
                    return render(request, 'admin/base.html')

        else:
            return render(request, 'login_failed.html')
    else:
        userform = AuthForm()
        return render(request, "login.html", {"form": userform})


def edit_person(request):
    if request.method == "POST":
        user_id = service()
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        person = Customer.objects.get(user__id=user_id)
        person.name = name
        person.surname = surname
        person.save()
        print(user_id)
        person = Customer.objects.get(user__id=user_id)
        #return HttpResponse("good")
        return render(request, 'person.html', {'person': person})
    else:
        userform = EditPersonForm()
        return render(request, "person_edit.html", {"form": userform})

def login_failed(request):
    return render(request, 'login_failed.html')

def register(request):
    if request.method == "POST":
        users = User.objects.all()
        login = request.POST.get("login")
        password = request.POST.get("password")
        email = request.POST.get("email")
        User.objects.create(username=login, password=make_password(password), email=email)
        send_mail('Create Account on GreenBanquet','Your account on GreenBanquet was created.','uservice589@gmail.com',
                  [email])
        return render(request, 'index.html')
    else:
        userform = RegisterForm()
        return render(request, "register.html", {"form": userform})

def person(request):
    user_id = service()
    print(user_id)
    person = Customer.objects.get(user__id=user_id)
    return render(request, 'person.html', {'person':person})

def main(request):
    return render(request, 'main.html', {'comments': Comment.objects.all()})

def banquets(request):
    if request.method == "POST":
        # user_id = service()
        # print(user_id)
        # banquets = Banquet.objects.filter(user__id=user_id, is_approved=True)
        # return render(request, 'banquet.html', {'banquets': banquets})
        banquet = Banquet.objects.get(id=request.POST.get('answer'))
        print(banquet)
        banquet.is_approved = False
        banquet.save()
        return HttpResponse("gee")
    else:
        user_id = service()
        print(user_id)
        banquets = Banquet.objects.filter(user__id=user_id, is_approved=True)
        return render(request, 'banquet.html', {'banquets': banquets})

def add_balance(request):
    if request.method == "POST":
        user_id = service()
        balance = request.POST.get("balance")
        person = Customer.objects.get(user__id=user_id)
        person.balance = person.balance + int(balance)
        person.save()
        person = Customer.objects.get(user__id=user_id)
        return render(request, 'person.html', {'person': person})
    else:
        userform = AddBalanceForm()
        return render(request, "add_balance.html", {"form": userform})

def create_banquet(request):
    if request.method == "POST":
        #request.POST.get("music")
        customer = Customer.objects.get(user_id=service())
        print(request.POST.get('date_day'))
        print(request.POST.getlist('food'))
        date = datetime.date(int(request.POST.get('date_year')),
                             int(request.POST.get('date_month'))
                             ,int(request.POST.get('date_day')))
        banquet = Banquet.objects.create(music_id=request.POST.get("music"),
                                 user_id=service(), money=request.POST.get("money"),
                               people=request.POST.get("people"), date=date)
        banquet.food.set(request.POST.getlist('food'))
        customer.balance = customer.balance - int(request.POST.get("money"))
        customer.save()
        return HttpResponse("hi")
    else:
        form = CreateForm()
        return render(request, 'create.html', {'form': form})


def leave_comment(request):
    if request.method == "POST":
        Comment.objects.create(title=request.POST.get("title"), text=request.POST.get("text"),
                               user_id=service())
        return HttpResponseRedirect("http://127.0.0.1:8000/banquet/main")
    else:
        form = CommentForm()
        return render(request, 'leave_comment.html', {'form': form})


def invite(request):
    if request.method == "POST":
        emails_list = str(request.POST.get("emails")).split(',')
        send_mail('Invite to banquet',request.POST.get("text"),
                  'uservice589@gmail.com',
                  emails_list)
        return render(request, 'main.html')
    else:
        form = InviteForm()
        return render(request, 'invite.html', {'form': form})
