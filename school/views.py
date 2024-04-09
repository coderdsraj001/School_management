from django.shortcuts import render, redirect
from .forms import StudentForm, NewUserForm, ClassForm
from .models import Student, Class, File
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm 
from django.views.decorators.csrf import csrf_protect

def redirect_to_school(request):
    return redirect('index')

# Authentication System
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successful.")
            return redirect("index")
        messages.error(request, "Unsuccessful Registration. Invalid Creadentials.")
    form = NewUserForm()
    return render(request, "authentication/register.html", context={"register_form":form})

@csrf_protect
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "authentication/login.html", context={"login_form": form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("index")

# Home   
def index(request):
    if request.user.is_superuser:
        classes = Class.objects.all()
    else:
        classes = Class.objects.filter(teacher=request.user.id)
    return render(request, "home/index.html", {"classes": classes})

# classes
def create_class(request):
    if request.method == "POST":
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Class Created Successfully.")
            return redirect("index")
    else:
        form = ClassForm()
    return render(request, "classes/create_class.html", {"form":form})

def edit_class(request, id):  
    clas = Class.objects.get(id=id)
    if request.method == "POST":
        form = ClassForm(request.POST, instance=clas)
        if form.is_valid():
            clas.save()
            messages.success(request, "Class Updated Successfully.")
            return redirect('index')
    else:
        form = ClassForm(instance=clas)
    return render(request,'classes/class_edit.html', {'form':form})

def delete_class(request, id):
    clas = Class.objects.get(id=id)  
    clas.delete() 
    messages.success(request, "class Delted Successfully.") 
    return redirect("index") 

# Student 
def student(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('myfile')
            student = form.save(commit=False)
            student.save()
            for file in files:
                file = File.objects.create(student=student, file=file)
            form.save()
            messages.success(request, "Student Created Successfully.")
            return redirect('show')
    else:
        form = StudentForm()
    return render(request, 'student/student.html', {'form':form})

def show(request):  
    students = Student.objects.all()
    student_with_file = []
    for student in students:
        file = File.objects.filter(student=student)
        student_with_file.append({'student': student, 'files': file}) 
    return render(request, "student/show.html",{'students_with_file':student_with_file}) 

def class_wise_students(request, pk):
    clas = Class.objects.get(pk=pk)
    student_list = Student.objects.filter(clas=clas)
    return render(request, 'student/class_wise_students.html', {'student_list': student_list})

def edit(request, id):  
    student = Student.objects.get(id=id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student.save()
            messages.success(request, "Student Updated Successfully.")
            return redirect('show')
    else:
        form = StudentForm(instance=student)
    return render(request,'student/edit.html', {'form':form})  

def destroy(request, id):  
    student = Student.objects.get(id=id)  
    student.delete() 
    messages.success(request, "Student Delted Successfully.") 
    return redirect("show")  


# Teacher
def teacher_list(request):
    teachers_with_classes = []
    teachers = User.objects.all()  
    for teacher in teachers:
        classes = Class.objects.filter(teacher=teacher)
        teachers_with_classes.append({'teacher': teacher, 'classes': classes})

    return render(request, "teachers/teacher.html", {'teachers_with_classes': teachers_with_classes})  
 
