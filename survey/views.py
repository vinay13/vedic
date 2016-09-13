from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core import urlresolvers
from django.contrib import messages
import datetime
import settings
from survey.models import Question, Survey , Category
from forms import ResponseForm , ABCForm
from survey.email import sendEmail


def Index(request):
	return render(request, 'index.html')

def ArbitView(request):
	return render(request,'arbit.html')
	

def SurveyDetail(request, id):
	survey = Survey.objects.get(id=id)
	category_items = Category.objects.filter(survey=survey)
	#categories = ['arbit','nonarbit','qerty','facilities']
	categories = [c.name for c in category_items]
	print 'categories for this survey:'
	print categories
	if request.method == 'POST':
		form = ABCForm(request.POST, survey=survey)
		if form.is_valid():
			response = form.save()
			sendEmail()
			return HttpResponseRedirect("/confirm/%s" % response.interview_uuid)
	else:
		form = ABCForm()
		#form = ABCForm(survey=survey)
		#print form
	return render(request, 'survey.html', {'response_form': form, 'survey': survey,'categories':categories})



def Confirm(request, uuid):
	email = settings.support_email
	return render(request, 'confirm.html', {'uuid':uuid, "email": email})



# def privacy(request):
# 	return render(request, 'privacy.html')

