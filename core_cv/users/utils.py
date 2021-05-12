from django.contrib import messages
from .models import Profile
from django.core.mail import EmailMessage
from django.contrib.auth.models import User


def check_name(name: str, request) -> str or None:
    # check if select word in (sql injection)

    if name and name != '?q=' and 'select' in name.lower().split() \
            or name and len(name) > 30:
        messages.warning(request, f"What you trying to find with this {name} ?")
        #  send mail to admin
        return None
    else:
        if name:
            if Profile.objects.filter(user__username=name).exists():
                return name
            else:
                messages.info(request, f"cant find this name {name} ?")
                return None


def mail_send(sender_email: str, sender_msg: str, request):
    # if uname or q is exists then send message to user that profile belongs to

    if request.session.get('uname'):
        user_email = User.objects.get(username=request.session.get('uname')).email
        email = EmailMessage(
            subject='New message from GreatCV',
            body=sender_msg,
            from_email=sender_email,
            to=[user_email]
        )
        email.send()
        del request.session['uname']  # clear session key

    elif request.session.get('q'):
        user_email = User.objects.get(username=request.session.get('q')).email
        email = EmailMessage(
            subject='New message from GreatCV',
            body=sender_msg,
            from_email=sender_email,
            to=[user_email]
        )
        email.send()
        del request.session['q']  # clear session key

    else:
        # sent to main user
        email = EmailMessage(
            subject='New message from GreatCV',
            body=sender_msg,
            from_email=sender_email,
            to=['anton6896@gmail.com']
        )
        email.send()
