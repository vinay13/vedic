from django.conf.urls import patterns, include, url
from material.frontend import urls as frontend_urls
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import settings

admin.autodiscover()
media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')

urlpatterns = patterns('',
	# Examples:
	url(r'^$', 'survey.views.Index', name='home'),
	url(r'^arbit/','survey.views.ArbitView',name='ArbitView'),
	url(r'^survey/(?P<id>\d+)/$', 'survey.views.SurveyDetail', name='survey_detail'),
	url(r'^confirm/(?P<uuid>\w+)/$', 'survey.views.Confirm', name='confirmation'),
	#url(r'^complaints/', 'complaints.views.IndexView', name='index'),
	# url(r'^privacy/$', 'survey.views.privacy', name='privacy_statement'),

	#url(r'', include(frontend_urls)),
	# Uncomment the admin/doc line below to enable admin documentation:
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	url(r'^',include('complaints.urls')),
	url(r'^frontend/',include(frontend_urls)),
)


# media url hackery. le sigh. 
urlpatterns += patterns('',
    (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
     { 'document_root': settings.MEDIA_ROOT, 'show_indexes':True }),
)


admin.site.site_header = 'Vaidya - hospital quality management system'
