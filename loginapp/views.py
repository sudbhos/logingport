from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import singup
# Create your views here.
def home(request):
    return render(request,"testapp/demo.html")
@login_required
def java(request):
    return render(request,"testapp/javaex.html")

def pytho(request):
    return render(request,"testapp/pythonex.py.html")

def sql(request):
    return render(request,"testapp/sqlex.html")

def singi(request):
    form=singup()
    if request.method=="POST":
        form=singup(request.POST)
        # if form.is_valid():
        #     form.save()
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect("/accounts/login")
    return render(request,"testapp/singup.html",{'form':form})