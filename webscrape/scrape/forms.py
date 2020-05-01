from django.forms import ModelForm
from django import forms
from .models import Item

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name",max_length=200)
    check = forms.BooleanField(required=False)


#to create another form you can create another class
class EditForm(ModelForm):
    itemTitle = forms.CharField(label="Name",max_length=200,required = False)
    itemPrice = forms.CharField(label="Name",max_length=200, required = False)
    class Meta:
        model = Item
        fields = ["itemTitle","itemPrice"]
        # required = False
    # title = forms.CharField(label="Name",max_length=200,required = False)
    # price = forms.CharField(label="Name",max_length=200, required = False)


    #productTitle = forms.CharField(label="Name",max_length=200)
    #price = forms.CharField(label="Name",max_length=200)
    #checker = forms.BooleanField(required=False)
