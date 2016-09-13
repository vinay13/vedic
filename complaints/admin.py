from django.contrib import admin
from complaints.models import Complaint
# Register your models here.
class ComplaintAdmin(admin.ModelAdmin):
	list_display = ('title', 'body', 'category','user_name','emailid')



admin.site.register(Complaint,ComplaintAdmin) 