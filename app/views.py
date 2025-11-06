from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout 
from django.shortcuts import get_object_or_404


# Create your views here.


def index(request):
    movies=Movie.objects.all()
    user = request.user
    if not user.is_authenticated:
        return redirect(loginuser)  
     
    return render(request, 'index.html', {'user': user,'movies':movies})

def loginuser(request):
    if request.method=='POST':
        name=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(request,username=name,email=email,password=password)
        print(user)
        if user is not None:
         login(request, user)
         return redirect(index)

        
    return render(request,'login.html')
def registeruser(request):
    if request.method=='POST':
        name=request.POST['name']
        emails=request.POST['email']
        password=request.POST['password']
        data=User.objects.create_user(username=name,email=emails,password=password)
        data.save()
        print(data)
        return redirect(loginuser)
    return render(request,'register.html')
def logoutuser(request):
    logout(request)
    return redirect(loginuser)

def vieww(request ,id):
    movie = get_object_or_404(Movie,id=id)
    movies=Movie.objects.filter(id=id) 
    
  
      
   
    abouts = Abouts.objects.filter(movie=movie)
    casts = Cast.objects.filter(about__in=abouts) 
    crews = Crew.objects.filter(about__in=abouts)
    print(casts,crews)


  

    

    


   
    
    


   
    return render(request, 'view.html',{'movies':movies,'abouts':abouts,'casts':casts,'crews':crews})


 