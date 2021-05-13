from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import wallet
from . forms import formsignup, formlogin, formCredit, formDebit


min_balance = 100
balance = 100
user = None


def create_log():
    pass


def login(request):

    if request.method == "POST":
        print(request.POST)
        m = request.POST.get("mobile_number")
        p = request.POST.get("password")
        print(m)
        global user
        user = wallet.objects.filter(mobile_number=str(m))
        if len(user):
            user = wallet.objects.filter(mobile_number=str(m)).values()[0]
            print(user, "-----------------")
            print("lgoni  :::", user)

            if user is None:
                return False
            if user["password"] != p:
                return False
            global balance
            balance = user["balance"]
            data = user
            return render(request, 'dashboard.html', {'data': data, "formDebit": formDebit(), "formCredit": formCredit()})

    return redirect("")


def signup(request):

    if request.method == 'POST':
        form = formsignup(request.POST)
        if form.is_valid():
            form.save()
            m = request.POST.get("mobile_number")
            global user
            user = wallet.objects.filter(mobile_number=str(m)).values()[0]
            print("signup  :::", user)
        return render(request, 'dashboard.html', {'data': user, "formDebit": formDebit(), "formCredit": formCredit()})

    else:
        render(request, "forms.html", {
               "signup": formsignup(), "login": formlogin()})
    return render(request, 'dashboard.html', {'data': user, "formDebit": formDebit(), "formCredit": formCredit()})


def home(request):

    return render(request, "forms.html", {"signup": formsignup(), "login": formlogin()})


def debit(request):
    money = request.POST.get("balance")
    m = request.POST.get("mobile_number")
    user = wallet.objects.filter(mobile_number=str(m))[0]

    if(money >= 0):
        val = user.balance - money

        limit = get_bal(request) - 100
        if(val < min_balance):
            print("you can't debit more than {} ", limit)
            return HttpResponse("you cant debit more than {} ", limit)

        else:
            user.balance = user.balance - money
            user.save()
            return render(request, 'dashboard.html', {'data': user, "formDebit": formDebit(), "formCredit": formCredit()})

    else:
        print("You can't debit negative money")

    return HttpResponse("debit")


def dashboard(request):

    l = user
    if l:
        if(request.method == "POST"):
            pass
        data = l
        print("lllllllllllll", l)
        return render(request, 'dashboard.html', {'data': data, "formDebit": formDebit(), "formCredit": formCredit()})
    else:
        data = signup(request)
        return render(request, 'dashboard.html', {'data': data, "formDebit": formDebit(), "formCredit": formCredit()})


def credit(request, money):
    if(money >= 0):
        balance += money
        user.balance = user.balance - money
        user.save()
    return render(request, 'dashboard.html', {'data': user, "formDebit": formDebit(), "formCredit": formCredit()})


def get_bal(request):
    return balance
