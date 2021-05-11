from django.contrib import messages
from .models import Profile


def check_name(name: str, request):
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
