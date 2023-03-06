from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.



user_list = [
    {'username':'雪之下雪乃','password':'5201314'},
    {'username':'yukino','password':'520'},
    {'username':'由比滨结衣','password':'1314'},
]

def index(request):
    # return HttpResponse('hello!django...')
    if request.method == 'POST':
        if request.POST.get('username') != '' and  request.POST.get('password') != '':
            user = {'username':request.POST.get('username'),'password':request.POST.get('password')}
            user_list.append(user)
    return render(request,'index.html',{'data':user_list})