from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request,'rango/index.html',context=context_dict)
def about(request):
    my_dict ={'insert_me':"BOO!"}
    return render(request,'rango/about.html',context=my_dict)
