from django.shortcuts import render, redirect
import uuid
from .models import Url
# Create your views here.
def home(request):
    return render(request, 'urlhandler/home.html')


def search(request,id):
    link=Url.objects.get(uid=id)
    return redirect(link.link)

def result(request):
    link=''
    uid=''
    data={}
    if request.method=="POST":
        link=request.POST['link']
        uid= str(uuid.uuid4())[:5]
        url=Url(link=link,uid=uid)
        url.save()
        data={
            'uid':uid,
            'link':link,
        }
        return render(request, 'urlhandler/home.html', data)
    
    

    
        