from datetime import time
from django.shortcuts import render,redirect
from django.http.response import JsonResponse
from django.contrib import messages
from first_app.models import Post_1, User
from django.contrib.auth import authenticate
from django.utils import timezone


def show(request):
    return render(request, 'first.html')


def authenticate_1(request):
    global id_1
    em = request.POST.get('i1')
    pa = request.POST.get('i2')
    print(em)
    print(pa)
    if request.method=='POST':
        check_if_user_exist = User.objects.filter(username=em).exists()
        if check_if_user_exist:
            user = authenticate(username=em, password=pa)
            man=User.objects.get(username=em)
            id_1=man.id
            if user is None:
                print('false')
                messages.error(request, 'Invalid Credentials')
                return redirect('/show/')
          
            else:
                return render(request,'second.html')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('/show/')




def save_1(request):
    if request.method=='POST':
        written=request.POST.get('t1')
        print(written)
        print(id_1)
        one=Post_1()
        one.user_id=id_1
        one.text=written
        one.save()
  
       
        return JsonResponse({'context':'completed'})


