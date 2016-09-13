from django.conf.urls import patterns,include,url
#from capp.views import IndexView

urlpatterns = patterns('',
	# Examples:
	url(r'^complaints/', 'complaints.views.IndexView', name='index'),


	)