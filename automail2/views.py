from smtplib import SMTPConnectError
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

# Create your views here.
def index(request):
    return render(request, 'automail2/index.html')

def success(request):
    if request.method == 'POST':
        name = request.POST['yname']
        item = request.POST['itemp']
        email = request.POST['yemail']   
         
        subject = f'Order is being processed'
        message = render_to_string('automail2/tempp.html', {
                'name': name,
                'item': item,
            })
        email = EmailMessage(
            subject, message, to=[email],
        )
        email.content_subtype = 'html'
        try:
            email.send()
        
        except:
            return HttpResponse('something went wrong!')
        else:
            return render(request, 'automail2/success.html')
        
        
        
        
        
        