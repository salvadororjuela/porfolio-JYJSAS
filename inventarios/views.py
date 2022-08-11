from django.shortcuts import render, redirect
# Importa para crear el formulario de autenticacion de usuarios.
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
# Importa para usar las funciones de log in y log out.
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
# Importa el modelo de usuarios para despues enviarlo como argumento a las
# paginas en que se requiera
from operaciones.models import CustomUser
from django.contrib.auth.decorators import login_required
# Importa el formulario para registrar un nuevo usuario
from operaciones.forms import SignUpForm
# Importa el archivo settings.py para poder enviar el correo.
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def index(request):
    return render(request, "inventarios/index.html")


def mision(request):
    return render(request, "inventarios/mision.html")


def vision(request):
    return render(request, "inventarios/vision.html")


def contacto(request):
    return render(request, "inventarios/contacto.html")


# Funcion para enviar correos al correo registrado
def enviarcorreogeneral(request):
    if request.method == "POST":
        asunto = request.POST["txtAsunto"]
        mensaje = request.POST["txtMensaje"] + \
            " / Email: " + request.POST["txtEmail"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["salvadorexamplemail@gmail.com"]
        send_mail(asunto, mensaje, email_desde,
                  email_para, fail_silently=False)
        return render(request, "inventarios/contacto.html", {
            "mensaje": "Su mensaje ha sido enviado exitosamente. Pronto nos pondremos en contacto con usted!"
        })
    else:
        return render(request, "inventarios/contacto.html")


# Funcion para crear nuevos usuarios (Exclusiva Gerente)
@login_required(login_url="inventarios/ingresar")
def signup_view(request):
    if request.method == "POST":
        # Formulario de creacion de usuario creado en operaciones/forms.py
        form = SignUpForm(request.POST)
        # Validacion
        if form.is_valid():
            # Guarda el usuario creado
            form.save()
            # Retorna a la pagina del menu del gerente
            return render(request, "inventarios/gerente.html", {
                "mensaje": "Nuevo Usuario Creado Exitosamente. Recuerde Diligenciar el Formulario del Nuevo Contratista"
            })
        # Si la validacion no pasa
        else:
            form = SignUpForm()
            return render(request, "inventarios/signup.html", {
                "form": form,
                "mensaje": "Verfique los datos ingresados e intente nuevamente!"
            })
    # Si el metodo es GET
    else:
        # Muestra el formulario de creacion de usuario por defecto de django
        form = SignUpForm()
        return render(request, "inventarios/signup.html", {
            "form": form
        })


# Funcio para ingresar usuarios y autenticar credenciales
def ingresar(request):
    # Si el usuario accede via POST
    if request.method == "POST":
        # Crea el formulario de autenticacion. Este requiere incluir el
        # parametro (data=request.POST)
        formulario = AuthenticationForm(data=request.POST)
        # Validacion
        if formulario.is_valid():
            # Permite el ingreso al usuario
            # Obtiene los datos del usuario de las variables del formulario
            usuario = formulario.get_user()
            # Ingresa en la pagina web usando la variable usuario como
            # parametro
            if usuario.cargo_empleado == "Gerente General":  # Perfil del Gerente
                login(request, usuario)
                # Como solo se redirecciona se usa redirect. Esto evita que se
                # tenga que volver a iniciar sesion en caso de recargar la
                # pagina
                return redirect("inventarios:gerente")
            # Ingresa al perfil del almacenista
            elif usuario.cargo_empleado == "Almacenista":
                login(request, usuario)
                # Como solo se redirecciona se usa redirect. Esto evita que se
                # tenga que volver a iniciar sesion en caso de recargar la
                # pagina
                return redirect("inventarios:almacenista")
            # Ingresa al perfil del director operativo
            elif usuario.cargo_empleado == "Director Operacional":
                login(request, usuario)
                # Como solo se redirecciona se usa redirect. Esto evita que se
                # tenga que volver a iniciar sesion en caso de recargar la
                # pagina
                return redirect("inventarios:directoroperativo")
                # Ingresa al perfil de cada contratista
            else:
                # Como solo se redirecciona se usa redirect. Esto evita que se
                # tenga que volver a iniciar sesion en caso de recargar la
                # pagina
                login(request, usuario)
                return redirect("inventarios:contratista")

        # Si la validacion del formulario no es correcta, se retorna a la
        # pagina de inicio de sesion
        else:
            return render(request, "inventarios/ingresar.html", {
                "formulario": formulario,
                "mensaje": "Upss. Algo salió mal. Su usuario o contraseña no son correctos.Vuelva a Intentar!",
            })

    # Si el usuario accede via GET
    else:
        # Crea y muestra el formulario de inicio de sesion
        formulario = AuthenticationForm()
        return render(request, "inventarios/ingresar.html", {
            "formulario": formulario,
        })


# Funcion para cerrar sesion
def salir_view(request):
    if request.method == "POST":
        logout(request)
        return render(request, "inventarios/index.html", {
            "mensaje": "Sesión cerrada con éxito!",
        })


@login_required(login_url=ingresar)
def gerente(request):
    usuario = CustomUser.objects.all()
    return render(request, "inventarios/gerente.html", {
        'usuario': usuario,
    })


@login_required(login_url=ingresar)
def almacenista(request):
    usuario = CustomUser.objects.all()
    return render(request, "inventarios/almacenista.html", {
        'usuario': usuario,
    })


@login_required(login_url=ingresar)
def directoroperativo(request):
    usuario = CustomUser.objects.all()
    return render(request, "inventarios/directoroperativo.html", {
        'usuario': usuario,
    })


@login_required(login_url=ingresar)
def contratista(request):
    usuario = CustomUser.objects.all()
    return render(request, "inventarios/contratista.html", {
        'usuario': usuario,
    })
