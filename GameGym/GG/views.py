from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, path
from django.views import generic
from .models import *
from .forms import *
from django.views.generic import CreateView
from .forms import AddbackConnection


def index(request):
    return render(request, "home.html")

# class BronPc(ListView):
#     model = Pc
#     template_name = 'hotel\hotel.html'


# class LoginUser(LoginView, DataMixin):
#     template_name = "login.html"
#     form_class = AuthenticationForm
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_user_context(title="Авторизация")
#         return dict(list(context.items()) + list(c_def.items()))

class SignUpView(generic.CreateView):
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def Map(request):
    return render(request, "maps.html")

def bron(request):
    return render(request, "bron.html")

def info(request):
    # pc = Pc.object.all()
    # context = {
    #     'pr' : pc
    # }
    return render(request, "info.html")

# fields = '__all__'

class Bron(generic.CreateView):
    model = Time_base
    fields = '__all__'
    template_name = 'bron.html'
    success_url = reverse_lazy('base.html')

class PCListView(generic.ListView):
    model = Type_pc
    template_name = 'maps.html'

def connect(request):
    return render(request, "connect.html")

class back_connect(CreateView):
    form_class = AddbackConnection
    template_name = 'connect.html'
    success_url = reverse_lazy('home')
