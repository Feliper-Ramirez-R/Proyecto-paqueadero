from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib import messages
from mainapp.forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from mainapp.models import Transporte, Usuario, Imagen, Area
from django.contrib.auth.decorators import login_required
from datetime import date
from datetime import datetime
from django.contrib.auth.decorators import permission_required




# Create your views here.


def index(request):

    return render(request, 'mainapp/index.html', {
        'title': 'Inicio'
    })

# vista para registrar un usuario nuevo
@permission_required('polls.can_vote', login_url='page')
@login_required(login_url="inicio")
def register(request):

    register_form = RegisterForm()

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            register_form.save()

            messages.success(request, 'Registro exitoso !!')

            return redirect('register')
        
    return render(request, 'users/register.html', {
        'title': 'Registro',
        'register_form': register_form
    })

# vista para el login de ingreso
def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        Usuario = authenticate(request, username=username, password=password)

        if Usuario is not None:
            login(request, Usuario)
            return redirect('page')

        else:
            messages.warning(
                request, 'El usuario o la contraseña son incorrectas')

    return render(request, 'users/login.html', {
        'title': 'Ingresar'

    })


# vista para el inicio donde se muestra el usuario logueado
@login_required(login_url="inicio")
def page(request):
   

   
   
    return render(request, 'pages/page.html', {
        'title': 'Paginas'
       
             
    })


# vista para el registro diario de transporte
@login_required(login_url="inicio")
def transporte(request):
   
    return render(request, 'pages/registrar_transporte.html', {
        'title': 'Transporte',

    })

# vista para guardar el registro diario de transporte, no devuelve nada
@login_required(login_url="inicio")
def save_trans(request):

    if request.method == 'POST':

        tipo_transporte = request.POST['tipo_transporte']
        user_id = request.POST['user_id']
        
        arr = user_id.split()
        ar = arr[1]
        

        user = Transporte(
            tipo_transporte=tipo_transporte,
            user_id=ar
        )
        user.save()

        messages.success(request, ' exitoso !!')

        return redirect('transporte')

    

# vista para consultar el parqueadero por usuario
@login_required(login_url="inicio")
def prueba(request):
    bici = ""
    moto = ""
    carro = ""
    mensaje = "No tienes ningun registro"
    dias_bici = 0
    dias_carro = 0
    dias_moto = 0
    precio_carro = 10000
    precioBici = 7000
    precio_moto = 5000
    usuario = ""

    if request.method == 'POST':

        id = request.POST.get('user_id')

        fecha = datetime.now()
        mes = fecha.month 

        bici = Transporte.objects.filter(user_id=id, tipo_transporte="bici",date__month=mes)
        moto = Transporte.objects.filter(user_id=id, tipo_transporte="moto",date__month=mes)
        carro = Transporte.objects.filter(user_id=id, tipo_transporte="carro",date__month=mes)
        dias_bici = bici.__len__
        dias_carro = carro.__len__
        dias_moto = moto.__len__
        usuario = usuario = User.objects.get(id=id)
       

    return render(request, 'pages/prueba.html', {
        'title': 'Prueba',
        'bici': bici,
        'carro': carro,
        'moto': moto,
        'mensaje': mensaje,
        'dias_bici': dias_bici,
        'dias_carro': dias_carro,
        'dias_moto': dias_moto,
        'precioBici': precioBici,
        'precio_carro': precio_carro,
        'precio_moto': precio_moto,
        'usuario': usuario

    })

# vista para consultar todo el historico de todos los usuarios
@login_required(login_url="inicio")
def reportes(request):

    trans = ""
    user = ""

    trans = Transporte.objects.all()
    user = User.objects.all()

    return render(request, 'pages/reporte.html', {
        'title': 'reportes',
        'trans': trans,
        'user': user


    })

# vista para consultar imagenes de los usuarios
@login_required(login_url="inicio")
def consultar(request):

    usuario = ""
   

    if request.method == 'POST':
        id = request.POST.get('user_id')
        usuario = Imagen.objects.get(user_id=id)

    return render(request, 'pages/consultar.html', {
        'title': 'consultar',
        'usuario': usuario


    })
#vista para consultar los historicos y los registros actuales
@login_required(login_url="inicio")
def parqueadero(request):
    bici = ""
    moto = ""
    carro = ""
    precio_carro = 10000
    precioBici = 7000
    precio_moto = 5000
    usuario = ""
    mes = ""
    acum_bici = ""
    acum_moto = ""
    acum_carro = ""
    total = 0
    mensaje = ""
    agosto = ""
    agostoM = ""
    agostoC = ""
    
   
   

    id = request.user.id

    fecha = datetime.now()
    mes = fecha.month 
   

    bici = Transporte.objects.filter(user_id=id, tipo_transporte="bici",date__month=mes)
    moto = Transporte.objects.filter(user_id=id, tipo_transporte="moto",date__month=mes)
    carro = Transporte.objects.filter(user_id=id, tipo_transporte="carro",date__month=mes)
    
    agosto = Transporte.objects.filter(user_id=id, tipo_transporte="bici", date__month='08')
    agostoM = Transporte.objects.filter(user_id=id, tipo_transporte="moto", date__month='08')
    agostoC = Transporte.objects.filter(user_id=id, tipo_transporte="carro", date__month='08')

    usuario = usuario = User.objects.get(id=id)
  
    acum_bici = len(bici) * precioBici
    acum_moto = len(moto) * precio_moto
    acum_carro = len(carro) * precio_carro

    pago = acum_carro + acum_moto

    if acum_carro + acum_moto - acum_bici > 0:
        total = pago - acum_bici
        mensaje = (f"Su valor a pagar es ${total}")
    else:
        total = acum_bici - pago
        mensaje = (f"Su beneficio es de ${total}")   
    
    
    
    
          
     
    return render(request, 'pages/parqueadero.html', {
        'title': 'Parqueadero',
        'bici': bici,
        'carro': carro,
        'moto': moto,
        'precioBici': precioBici,
        'precio_carro': precio_carro,
        'precio_moto': precio_moto,
        'usuario': usuario,
        'mes':mes,
        'acum_bici':acum_bici,
        'acum_moto':acum_moto,
        'acum_carro':acum_carro,
        'total': total,
        'mensaje':mensaje,
        'agosto':agosto,
        'agostoM':agostoM,
        'agostoC':agostoC
            

    })
#vista para consultar el total de los pagos mensuales 
@login_required(login_url="inicio")
def pagos_mes(request):

    precioCarro = 10000
    precioBici = 7000
    precioMoto = 5000
    pagoAgostoB = ""
    AgostoB = ""
    AgostoM = ""
    AgostoC = ""
    mensaje = ""

    AgostoB = Transporte.objects.filter(tipo_transporte="bici", date__month='08')
    AgostoM = Transporte.objects.filter(tipo_transporte="moto", date__month='08')
    AgostoC = Transporte.objects.filter(tipo_transporte="carro", date__month='08')

    pagoAgostoB = len(AgostoB) * precioBici
    pagoAgostoM = len(AgostoM) * precioMoto
    pagoAgostoC = len(AgostoC) * precioCarro

    pago = pagoAgostoC + pagoAgostoM

    if pagoAgostoM + pagoAgostoC - pagoAgostoB > 0:
        total = pago - pagoAgostoB
        mensaje = (f"El mes de agosto se cobró ${total}")
    else:
        total = pagoAgostoB - total
        mensaje = (f"El mes de agosto se pagó ${total}")    
   
    return render(request, 'pages/pagos_mes.html', {
        'pagos_mes': 'Pagos_mes',
        'pagoAgostoB':pagoAgostoB,
        'pagoAgostoM':pagoAgostoM,
        'pagoAgostoC':pagoAgostoC,
        'AgostoB':AgostoB,
        'AgostoM':AgostoM,
        'AgostoC':AgostoC,
        'mensaje':mensaje
         })
        
#vista para cerrar sesion
def logout_user(request):
    logout(request)
    return redirect('inicio')    

#vista para cambiar la imagen
def editar_imagen(request):

    id = request.user.id

    if request.method == 'POST':

        
        imagen = Imagen.objects.get(user_id=id)
        
        imagen.image = request.FILES['myfile']
        
        imagen.save()

        return redirect('page')

  #vista de tarifas 
@login_required(login_url="inicio")
def tarifas(request):
   
   
    return render(request, 'pages/tarifas.html', {
        'title': 'Tarifas'
             
    })
