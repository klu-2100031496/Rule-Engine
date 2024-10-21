from django import forms

class RuleForm(forms.Form):
    rule_string = forms.CharField(widget=forms.Textarea, label="Enter Rule")

class UserDataForm(forms.Form):
    age = forms.IntegerField(label="Age")
    department = forms.CharField(label="Department")
    salary = forms.IntegerField(label="Salary")
    experience = forms.IntegerField(label="Experience")
