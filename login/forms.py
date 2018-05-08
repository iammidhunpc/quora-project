from django import forms
from .models import *

class NameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
         super(NameForm, self).__init__(*args, **kwargs)
         for field in self.fields.values():
         	field.widget.attrs = {'class': 'form-control'}
    class Meta:
    	model = Register
    	fields = ['name','email','password','username']
class LogForm(forms.Form):

	def __init__(self, *args, **kwargs):
	 	super(LogForm, self).__init__(*args, **kwargs)
	 	for field in self.fields.values():
	 		field.widget.attrs = {'class': 'form-control'}
	name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'name'}),label='name', max_length=50)
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
   		model = Logs
class LogadminForm(forms.Form):

	def __init__(self, *args, **kwargs):
	 	super(LogadminForm, self).__init__(*args, **kwargs)
	 	for field in self.fields.values():
	 		field.widget.attrs = {'class': 'form-control'}
	name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'name'}),label='name', max_length=50)
	password = forms.CharField(widget=forms.PasswordInput)


class QuestForm(forms.Form):
	ques=forms.CharField(max_length=100)



class ActForm(forms.Form):
	stats=forms.CharField(max_length=1)
class AnsstatForm(forms.Form):
	statans=forms.CharField(max_length=1)
class AnsForm(forms.Form):
	txta=forms.CharField(max_length=500)
class ComForm(forms.Form):
	txtc=forms.CharField(max_length=500)
