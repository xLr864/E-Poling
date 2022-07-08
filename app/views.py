from django.shortcuts import render, HttpResponse
from .models import Registeration
def index(request):
    return render(request,'home.html')

def join(request):
    if request.method=="POST":
        if request.POST.get("login")=="Login":
            username = request.POST["user_name"]
            vid = request.POST["voterid"]
            dob = request.POST["dob"]
            

        if request.POST.get("signup")=="Signup":
            username = request.POST["user_name"]
            email = request.POST["email"]
            address = request.POST["address"]
            phone = request.POST["pno"]
            aadhar = request.POST["aadhar"]
            vid = request.POST["voterid"]
            dob = request.POST["dob"]
            dob = dob.split("/")
            formatted_date = dob[2]+"-"+dob[1]+"-"+dob[0]
            # print(f"\n\n\n\n=======>  {formatted_date}  <===========\n\n\n\n")
            record = Registeration(Name=username,Email=email,Mobile=phone,Address=address,Aadhar=aadhar,VoterID=vid,DOB=formatted_date) 
            record.save()          
            return render(request,'home.html')

    return render(request,'join.html')

def faq(request):
    return render(request,'faq.html')

def about(request):
    return render(request,'about.html')

def ad(request):
    return render(request,'admin.html')

def list(request):
    return render(request,'list.html')

def result(request):
    return render(request,'result.html')

def cn(request):
    return render(request,'cn.html')

def main(request):
    return render(request,'main.html')


