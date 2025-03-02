from django.shortcuts import render,redirect




# Create your views here.
def home(request):
    return render(request, 'home.html')

def welcm(request):
    return render(request,"wc.html")


from .form import DeptForm


def dashbd(request):
    return render (request,"dashbd.html")



def adddept(request):
    if request.method == "POST":
        form = DeptForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course')  # Replace with your success page URL
    else:
        form = DeptForm()
    
    return render(request, 'dept.html', {'form': form})


from .form import CourseForm

def course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')  # Redirect to a success page after submission
    else:
        form = CourseForm()
    
    return render(request, 'course.html', {'form': form})

# from django.shortcuts import render, redirect
from .form import StudentForm

def students(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event')  # Redirect to a success page after submission
    else:
        form = StudentForm()
    
    return render(request, 'student.html', {'form': form})


# from django.shortcuts import render, redirect
from .form import EventForm

def event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('parti')  # Redirect to success page after submission
    else:
        form = EventForm()
    
    return render(request, 'event.html', {'form': form})


# from django.shortcuts import render, redirect
from .form import PartiForm

def parti(request):
    if request.method == "POST":
        form = PartiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to success page
    else:
        form = PartiForm()
    
    return render(request, 'parti.html', {'form': form})





#rudra