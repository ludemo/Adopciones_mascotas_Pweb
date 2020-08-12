from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,View
from .models import Direcciones,Mascotas,Usuario
from .forms import MascotasForm,UsuarioForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings
from django.http import HttpResponse
from .utils import render_to_pdf
# Create your views here.
#Envio del pdf 
class DetalleMascota_pdf(View):
    def get(self,request,*args,myID):
            obj = get_object_or_404(Mascotas, id = myID)
            context = {
                'objeto':obj,
            }
            pdf = render_to_pdf('detalleMascota_pdf.html',context)
            return HttpResponse(pdf,content_type='application/pdf')
#Fin del envio del pdf
#Empieza el envio de correos
def  enviar(request,myID):
    form = UsuarioForm(request.POST)
    obj = get_object_or_404(Mascotas, id = myID)
    if form.is_valid():
        form.save()
        mail =request.POST.get('correo')
        send_email(mail,obj)
    context = {
        'form' : form,
        "url":Direcciones,
        'objeto':obj,
    }
    return render(request,"enviar.html",context)
def send_email(mail,obj):
    email = EmailMultiAlternatives(
        'Adopción-No eres tú soy yo',
        'Gracias,por aceptarl, le estamos confirmando',
        settings.EMAIL_HOST_USER,
        [mail],
    )
    context = {
        'mail':mail,
        'objeto':obj
    }
    template = get_template('correo.html')
    content = template.render(context)
    email.attach_alternative(content,"text/html")
    email.send()
    ##Termina el envio de correos
def Home(request):
    context = {
        "url":Direcciones
    }
    return render(request,'index.html',context)
#Mascotas
def DetallesMascotas(request,myID):
    obj = get_object_or_404(Mascotas, id = myID)
    context = {
        'objecto':obj,
        'url':Direcciones
    }
    return render(request,'detalles.html',context)
def ListaMascotas(request):
    obj = Mascotas.objects.all()
    context = {
    "obj":obj
    }
    return render(request,"mascotas.html",context)
#Fin Mascotas
#Mascotas para Admin
def ListaMascotas_admin(request):
    obj = Mascotas.objects.all()
    context = {
    "obj":obj,
    "url":Direcciones
    }
    return render(request,"mascota/listado_mascotas.html",context)
def MascotasCreateView(request):
    form = MascotasForm(request.POST,files = request.FILES)
    if form.is_valid():
        form.save()
        form = MascotasForm
    context = {
        'form' : form,
        'url' :Direcciones,
    }
    return render(request,'usuario/createMascotas.html',context)
def eliminarMascota(request, myID):
    obj = get_object_or_404(Mascotas, id = myID)
    if request.method == 'POST':
        obj.delete()
        return redirect('../')
    context = {
        'obj':obj,
        "url":Direcciones,
    }
    return render(request,'usuario/eliminar.html', context)
def ActualizarDatos_Mascotas(request,myID):
    obj = Mascotas.objects.get( id = myID)
    form = MascotasForm(request.POST, instance=obj)
    if form.is_valid():
        form.save()
        form = MascotasForm()
    context = {
        'form':form,
        'url':Direcciones
    }
    return render(request,'mascota/actualizar_mascotas.html',context)
#Fin de Mascotas para admin
#Usuario
def editarUsuario(request, myID):
    obj = Usuario.objects.get(id = myID)
    form = UsuarioForm(request.POST, instance=obj)
    if form.is_valid():
        form.save()
        form = UsuarioForm()
    context = {
        'form' : form,
        "url":Direcciones,
    }
    return render(request, 'usuario/editarUsuario.html', context)
def eliminarUsuario(request, myID):
    obj = get_object_or_404(Usuario, id = myID)
    if request.method == 'POST':
        obj.delete()
        return redirect('../')
    context = {
        'obj':obj,
        "url":Direcciones,
    }
    return render(request,'usuario/eliminar.html', context)
def listaUsuarios(request):
    obj = Usuario.objects.all()
    context = {
        "obj":obj,
        "url":Direcciones,
    }
    return render(request, "usuario/listaUsuario.html", context)
def mostrarUsuario(request, myID):
    obj = get_object_or_404(Usuario, id = myID)
    context = {
        'obj':obj,
        "url":Direcciones,
    }
    return render(request,'usuario/detallesUsuario.html', context)
def user(request):
    context = {
        "url":Direcciones,
    }
    return render(request,'usuario/operacionesUsuario.html', context)
#Fin Usuario