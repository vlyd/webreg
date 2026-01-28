
from django.shortcuts import render
from django.views import View
from .forms import SigUpForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect

class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'index.html'
        )

class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = SigUpForm()
        return render(request, 'DjangoProject1/signup.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = SigUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'DjangoProject1/signup.html', context={
            'form': form,
        })