from django.shortcuts import render
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

# Create your views here.
def index(request):
    return render(request, 'automail2/index.html')

def success(request):
    if request.method == 'POST':
        template = render_to_string('automail2/tempp.html', {'name': request.POST['yname'], 'item': request.POST['itemp']})
    
        email = EmailMessage(
            'Order is being processed',
            template,
            settings.EMAIL_HOST_USER,
            [request.POST['yemail']])
        email.fail_silently = False
        email.send()
        return render(request, 'automail2/success.html')