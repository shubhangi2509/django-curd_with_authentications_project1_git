from django import  forms

from .models import  Student



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        labels = {
        "roll": "ROLL NUMBER",
        "fname": "FIRST NAME",
        "lname":"LAST NAME",
        "marks": "MARKS",
        "mail": "EMAIL",
        "address": "ADDRESS",
        "password": "PASSWORD",
        "c_password": "C_PASSWORD",
    }