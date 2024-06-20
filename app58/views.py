from django.shortcuts import render
from math import factorial

def factorial_view(request):
    factorials = {i: factorial(i) for i in range(3, 9)}
    return render(request, 'app58/index.html', {'factorials': factorials})