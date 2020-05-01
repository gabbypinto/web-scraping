from django import forms

class CreateNewList(forms.Form):
    #there are plenty of field
    name = forms.CharField(label="Name",max_length=200)
    check = forms.BooleanField(required=False)


#to create another form you can create another class
