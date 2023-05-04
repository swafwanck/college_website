from django import forms

from django.forms import ModelForm
from django.forms.widgets import EmailInput, TextInput
from web.models import COURSE, GENDER, Contact


EMPTY_COURSE = (("", "Select your course"),) + COURSE
EMPTY_GENDER = (("", "Select your gender"),) + GENDER

class ContactForm(ModelForm):
    course = forms.ChoiceField(choices=EMPTY_COURSE)
    gender = forms.ChoiceField(choices=EMPTY_GENDER)

    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            "full_name": TextInput(attrs={"placeholder": "First name"}),
            "email": EmailInput(attrs={"placeholder": "Your Email"}),
            "cap_id": TextInput(attrs={"placeholder": "cap id"}),
            "dob": TextInput(attrs={"placeholder": "Date of Birth"}),
            "student_number": TextInput(attrs={"placeholder": "Enter your number"}),
            "father_name": TextInput(attrs={"placeholder": "Father name"}),
            "mother_name": TextInput(attrs={"placeholder": "Mother name"}),
            "parent_number": TextInput(attrs={"placeholder": "Enter your parent number"}),
            "institution": TextInput(attrs={"placeholder": "Institution last attended"}),
            "month_and_year": TextInput(attrs={"placeholder": "Month and year of passing"}),
            "course_selected_for_plus_two": TextInput(attrs={"placeholder": "eg: science"}),
            "percentage_obtained": TextInput(attrs={"placeholder": "eg: 75% "}),
        }
        error_messages = {
            "full_name" : {
                "required": "Your full name is required"
            },
            "email" : {
                "required": "Email address is required"
            },
            "cap_id" : {
                "required": "CAP ID is required"
            },
            "dob" : {
                "required": "Short description field is required"
            },
            "student_number" : {
                "required": "Student number is required"
            },
            "father_name" : {
                "required": "Father name is required"
            },
            "mother_name" : {
                "required": "Mother name is required"
            },
            "parent_number" : {
                "required": "Parent number is required"
            },
            "institution" : {
                "required": "Last attended Institution is required"
            },
            "month_and_year" : {
                "required": "Month and Year of passing your plus two is required"
            }, 
            "course_selected_for_plus_two" : {
                "required": "Course selected for plus two is required"
            },
            "percentage_obtained" : {
                "required": "Percentage Obtained is required"
            },
            "downloaded_date" : {
                "required": "Downloaded Date is required"
            },
        } 