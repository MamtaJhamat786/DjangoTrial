from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic, Webpage,AccessRecord

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict= {'access_record': webpages_list}
    my_dict = {'insert_me': "hello I am from view.py"}
    return render(request, 'first_app\index.html',context=date_dict)

def help(request):
    my_dict2= {'help_page': "Hello I am here to help? pleaese feel free to ask any questions"}
    return render(request,'first_app\help.html',context=my_dict2)
