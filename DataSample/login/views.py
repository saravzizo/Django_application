from django.shortcuts import render,redirect
from .models import sar
from django.http import HttpResponse
from django.template import loader
# def Login(request):
  
#     return render(request,"index.html")
def Home(request):
    return HttpResponse("home")
      

def Login(request):
        if request.method == 'POST':
            if request.POST.get('username') and request.POST.get('password'):
                post=sar()
                post.username= request.POST.get('username')
                post.password= request.POST.get('password')
                post.save()
                
                return redirect('/login_page') 

        else:
                return render(request,'index.html')

def view_data(request):
  mydata_members = sar.objects.all()
  template = loader.get_template('success.html')
  context = {
    'mydata': mydata_members,
    
  }
  return HttpResponse(template.render(context, request))