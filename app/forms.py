from django import forms

class StudentForm(forms.Form):
    sname=forms.CharField(max_length=100)
    sid=forms.IntegerField()
    semail=forms.EmailField()