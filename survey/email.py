from django.core.mail import send_mail
 

complaint_message = 'Thank you for taking survey. Your opinion does matter to us.'

def sendEmail():
	send_mail('Survey Completed', complaint_message , 'pythonistvinay@gmail.com', ['vxixnxaxy@gmail.com'], fail_silently=False)