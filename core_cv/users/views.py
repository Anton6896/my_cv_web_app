from django.shortcuts import render
from django.views.generic import View


class HomeUsers(View):

    def get(self, *args, **kwarg):
        context = {
            "title": 'CV Page'
        }

        return render(self.request, "home_users.html", context)

    def post(self, *args, **kwarg):
        pass
