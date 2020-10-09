from django.shortcuts import render,redirect,HttpResponse
from .models import Register
# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == "POST":
        fullname=request.POST.get('fullname')
        email=request.POST.get('email')
        phoneno=request.POST.get('num')
        state=request.POST.get('state')
        gender=request.POST.get('gender')
        
        print(fullname,email,phoneno,state,gender)
        query=Register(fullname=fullname,email=email,phoneno=phoneno,state=state,gender=gender)
        query.save()
        return HttpResponse("Registration Successful!")
        
        
        return redirect('/')
    
    
    
    return render(request,'index.html')