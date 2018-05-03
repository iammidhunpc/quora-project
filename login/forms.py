from django import forms
from .models import *

class NameForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NameForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {'class': 'form-control'}
    class Meta:
        model = Register
        fields = "__all__"
class LogForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(LogForm, self).__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs = {'class': 'form-control'}
	class Meta:
   		model = Logs
   		fields = "__all__"

class QuestForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(QuestForm, self).__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs = {'class': 'form-control'}
	class Meta:
   		model = Quest
   		fields = "__all__"

class ActForm(forms.Form):
	stats=forms.CharField(max_length=1)
class AnsForm(forms.Form):
	txta=forms.CharField(max_length=500)
