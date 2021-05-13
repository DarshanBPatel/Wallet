
from django.contrib import admin
from django.urls import path
from payzolve.views import get_bal, debit, credit, signup, login, home, dashboard
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),

    path('signup/', signup),
    path('login/', login),
    path('dashboard/', dashboard),
    path('get-bal/', get_bal),
    path('debit/', debit),
    path('credit/', credit),
]
