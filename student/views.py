from django.shortcuts import redirect, render

from student.form import PostForm
from student.models import Student, StudentForm




# Create your views here.
def index(request):
    
    if request.method =="POST":   
        name= request.POST['name']
        father_name=request.POST['father']
        mother_name=request.POST['mother']
        email=request.POST['email']
        phone=request.POST['phone']
        address=request.POST['present']
        image=request.FILES['file']
        
        StudentForm.objects.create(
        name=name,
        father_name=father_name,
        mother_name=mother_name,
        email=email,
        phone=phone,
        address=address,
        image=image,   
        )
            
        
    return render(request,'student/index.html')
    

            
            



    









def form(r):
    if r.method == "POST":
        p = PostForm(r.POST,r.FILES)
        if p.is_valid():
            print(p)
            p.save()
        return redirect('index')

    return render(r,"student/form.html",{"form":PostForm})

    