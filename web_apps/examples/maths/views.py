from django.shortcuts import render
from django.http import HttpResponse
from maths.models import Math
# Create your views here.
def obliczenia(request, operacja, a, b ):
    a, b = int(a), int(b)
    if operacja =='add':
        wynik = a + b
    elif operacja =='sub':
        wynik = a - b

    m = Math(operacja= operacja, a=a, b=b, wynik=wynik)
    m.save()
    print(m.a, m.b, m.operacja)

    return HttpResponse(wynik)