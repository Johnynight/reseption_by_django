from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginuserForm
def login_user(request):
    if request.method == 'POST':
        form = LoginuserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],
                                password=cd['password']
                                )
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('main'))
    form = LoginuserForm()
    return render(request, 'users/login.html', {'form': form})

def logout_user(request):
    return HttpResponse('logout')
# Create your views here.



class LoginUser(LoginView):
    form_class = LoginuserForm
    template_name = 'users/login.html'
    extra_context = {
        'title' : 'Авторизация'
    }
    def get_success_url(self):
        return reverse_lazy('main')


