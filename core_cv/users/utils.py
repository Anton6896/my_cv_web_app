from django.contrib import messages


def check_name(name: str, request):
    # check if select word in (sql injection)

    if name and name != '?q=' and 'select' in name.lower().split():
        messages.warning(request, f"What you trying to find with this {name} ?")
        #  send mail to admin
        return None
    else:
        return name
