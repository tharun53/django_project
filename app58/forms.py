from django import forms
class inputform(forms.Form):
    input1=forms.IntegerField(min_value=1,max_value=10,label="Enter a number")