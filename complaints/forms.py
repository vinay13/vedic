

from django import forms
#from material import Layout,Row,Span5,Span
from material import *
from complaints.models import Complaint



class CheckForm(forms.ModelForm):

	class Meta:
		model = Complaint
		fields = ('title','body','category','user_name','emailid')


	layout = Layout(
	Fieldset("Complaints",
	Row(Span5('title')),
	Row('body'),
	Row('category')),
	Fieldset("Give Personal Detail",
	Row('user_name'),
	Row('emailid')))



class CheckoutForm(forms.Form):
	COUNTRY_CHOICES = (('1','ADMISSION'),('2','STAFF'),('3','FACILITIES'))
	title = forms.CharField()
	description = forms.CharField()
	against = forms.ChoiceField(choices=COUNTRY_CHOICES)
	name = forms.CharField()
	email = forms.EmailField()
	phoneno = forms.CharField()
	anonymous = forms.BooleanField()
	

	layout = Layout(
		Fieldset("Complaints"),
		Row('against'),
		Row('title'),
		Row('description'),
		
		#Row('anonymous'),
		Fieldset("Give your details",
		Row(Span5('name'), Span5('email'), Span2('phoneno'))))

