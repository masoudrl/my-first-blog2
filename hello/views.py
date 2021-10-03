from django.shortcuts import render
from django.http import HttpResponse
def view_salam(request):
    return HttpResponse("سلام")
def bye(request):
    return HttpResponse("Bye")
def print_factorial(request):
    s=""
    for i in range(1,1001):
        s+=f"<br>{i}!={get_factorial(i)}"
    return HttpResponse(s)
def get_factorial(n):
    r=1
    for i in range(1,n+1):
        r*=i
    return r
def get_fib(n):
    if n==1 or n==2:
        return 1
    f=[0,1,1]
    for i in range(3,n+1):
        f.append(sum(f[-2:]))
    return f
def get_fibN(n):
    f=get_fib(n)
    return f[-1]
def print_fibonachi(request):
    f=get_fib(1000)
    s=""
    for i in f:
        s+=str(i)+"<br>"
    return HttpResponse(s) 
def print_fibonachiN(request,m):
    f=get_fibN(m)
    return HttpResponse(str(f))
def details(request):
    cars={'color':'red',
    'year':1990,
    'brand':'pride',
    'fib':get_fib(100)}
    return render(request,'hello\details.html',cars)
