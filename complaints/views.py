
# Create your views here.
from django.shortcuts import render
# Create your views here.
from forms import CheckoutForm,CheckForm
from django.http import HttpResponse
from complaints.models import Complaint

def IndexView(request):

	#form = CheckoutForm() 
	#complaints2 =  Complaint.objects.get(id=id)
	if request.method == 'POST':
		form = CheckForm(request.POST)
		if form.is_valid():
			response = form.save()
			#sendEmail()
			return HttpResponse("Thank you")
	else:
		form = CheckForm()
	return render(request, 'complaints.html',{'form':form })