from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import TemplateView
from core.forms import SignUpForm



# Create your views here.

def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })
    
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            identification = form.cleaned_data.get('identification') #FUNCIONA!!!!
            user = authenticate(username=username, password=raw_password, identification=identification)
            login(request, user)
            return redirect('home')
    else:
        form = Sign()
    return render(request, 'registration/signup.html', {'form': form})

@login_required(redirect_field_name='justforMagic')
# To decorate the views that we want to protect
# it is suppose it protects the login page 
def secret_page(request):
    return render(request, 'secret_page.html')

class SecretPage(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'secret_page.html'

