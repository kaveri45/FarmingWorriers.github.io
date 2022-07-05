from django.core.checks import messages
from django.shortcuts import render
from Home.models import Register
from django.shortcuts import redirect
from django.urls import reverse
# Create your views here.
from django.http  import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.


def admin_login(request):
    msg=''
    context={}
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
      

        if username=='root123@gmail.com' and password=='root':
           request.session['username']=username 
           return redirect('register')
           
            
            
        else:
            context["status"] = "Invalid Credentials! Try again...."    

    return render(request,"admin_login.html",context)


def admin_Logout(request):
    try:
        del request.session['username']
        

    except:
        return render(request,'admin_Login.html')
    return render(request,'admin_Login.html')#work after try because there is no render(),if except block is true then this render() not executing
        
    
def home(request):
    return render(request,'index.html')

def register(request):
    return render(request,'register.html')


def Add_Worker_Data(request):
    if request.method=='POST':
        First_Name=request.POST['First_Name']
        Last_Name=request.POST['Last_Name']
        Email=request.POST['Email']
        Password=request.POST['Password']
        Mobile=request.POST['Mobile']
        Gender=request.POST['Gender']
        City=request.POST['City']
        Worker_Type=request.POST['Worker_Type']
        Rate=request.POST['Rate']
        r=Register()
        r.First_Name=First_Name
        r.Last_Name=Last_Name
        r.Email=Email
        r.Password=Password
        r.Mobile=Mobile
        r.Gender=Gender
        r.City=City
        r.Worker_Type=Worker_Type
        r.Rate=Rate
        r.save()
    
        return redirect('view_Worker_Data')
        
    else:
        return HttpResponse("<h1> 404 Not found</h1>")
    return render(request,'register.html')

def worker_Login(request):
    msg=" "
    context={}
    if request.method=='POST':
        try:
            Userdetails=Register.objects.get(Email=request.POST['username'],Password=request.POST['password'])
            request.session['Email']=Userdetails.Email
            request.session['Email'] = Userdetails.Email
            Worker_id = Userdetails.id
            Worker_name = Userdetails.First_Name
            return render(request, 'GoToPage.html', {'Worker_id': Worker_id, 'Worker_name': Worker_name})
        except Register.DoesNotExist as e:
             context["status"] = "Invalid Credentials! Try again...." 
             
    return render(request,'worker_Login.html',context)#Only Execute when except block true bcoz there is no render()..in try blcok there is render so it not come to another render()  
         
        
def worker_Logout(request):
    try:
        del request.session['Email']
    except:
        return render(request,'worker_Login.html')
    return render(request,'worker_Login.html')
    


def view_Worker_Data(request):
    worker_Data=Register.objects.all()
    
    return render(request,"view_Worker_Data.html",{'worker_Data':worker_Data})


def delete_Worker(request,id):
    worker_Data=Register.objects.get(id=id)
    worker_Data.delete()
    msg="Deleted Successfully!"
    return render(request,"view_Worker_Data.html",{'msg':msg})

def search(request):
    formdata=''
    msg=''
    if request.method=="GET":
        cname=request.GET.get("City")
        wtype=request.GET.get("Worker_Type")
       
        formdata=Register.objects.filter(City=cname).filter(Worker_Type=wtype)
          
       
        return render(request,'viewsearch.html',{'formdata':formdata}) 

            
    




def edit(request, id):
    context = {}
    Worker = Register.objects.get(id=id)
    context["Worker"] = Worker
    if request.method == 'POST':
        First_Name = request.POST['First_Name']
        Last_Name = request.POST['Last_Name']
        Email = request.POST['Email']
        Password = request.POST['Password']
        Mobile = request.POST['Mobile']
        City = request.POST['City']
        Worker_Type = request.POST['Worker_Type']
        Rate = request.POST['Rate']
        Worker.First_Name = First_Name
        Worker.Last_Name = Last_Name
        Worker.Email = Email
        Worker.Password = Password
        Worker.Mobile = Mobile
        Worker.City = City
        Worker.Worker_Type = Worker_Type
        Worker.Rate = Rate
        Worker.save()
        context["status"] = "Data has been Edited Successfully...."
    return render(request, 'editProfile.html', context)
