from django import forms
from .models import Dept

class DeptForm(forms.ModelForm):
    class Meta:
        model = Dept
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Enter Department Name'})
            
        }


from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'dept']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Enter Course Name'}),
            'dept': forms.Select(attrs={'class': 'form-select'})
        }
        
# from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'contact', 'course', 'dept']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Enter Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Enter Email'}),
            'contact': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Enter Contact Number'}),
            'course': forms.Select(attrs={'class': 'form-select'}),
            'dept': forms.Select(attrs={'class': 'form-select'}),
        }

# from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date_time', 'venue']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Enter Event Name'}),
            'date_time': forms.DateTimeInput(attrs={'class': 'form-input', 'type': 'datetime-local'}),
            'venue': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Enter Venue'}),
        }


# from django import forms
from .models import Parti

class PartiForm(forms.ModelForm):
    class Meta:
        model = Parti
        fields = ['name', 'event', 'course']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Enter Name'}),
            'event': forms.Select(attrs={'class': 'form-select'}),
            'course': forms.Select(attrs={'class': 'form-select'}),
        }

