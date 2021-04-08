from django.shortcuts import render
from django.views.generic import TemplateView

# from django.shortcuts import render, redirect
# from django.views.generic import ListView
# from django.contrib.auth.forms import UserCreationForm
# from .forms import RegisterForm
# from django.contrib import messages
# from django.contrib.auth import authenticate,login, logout
#from cap2.models import Imagen

# Create your views here.


class HomePageView(TemplateView):
    template_name = "cap2/index.html"
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = "Mi super web"
    #     return context
    def get(self, request,*args, **kwargs):
        return render(request, self.template_name,{'title':"Víctor Hernández"})

# def index(request):
#     return render(request,"cap2/index.html")


def register_page(request):

    register_form = RegisterForm()

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            register_form.saved()

            redirect ('')

    return render (request,'users/register.html',{
                    'title':'Registro',
                    'register_form':register_form
                        }
                        )
def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
      
        if user is not None:
            login(request,user)
            return redirect('/fichas')
        else:
            messages.warning(request, 'No te has identificado')
    return render (request,'users/login.html',{'title':'Iniciar sesión'})

def logout_user(request):
    logout(request)
    return redirect('/login')

# def formularios(request):
#     return render(request,"cap2/formularios.html")

# class ImagenList(ListView):
#     model = Imagen

# def FigurasList(request):
#     figuras = Imagen.objects.all()
#     return render(request,"cap2/galeria_list.html",{'figuras':figuras})