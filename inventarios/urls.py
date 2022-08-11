from django.urls import path
from . import views


# Namespace para evitar conflicto entre urls llamadas igual pero en diferentes
# aplicaciones
app_name = "inventarios"

urlpatterns = [
    # Camino a la pagina principal de la empresa
    path("", views.index, name="index"),
    path("mision", views.mision, name="mision"),
    path("vision", views.vision, name="vision"),
    path("contacto", views.contacto, name="contacto"),
    path("enviarcorreogeneral", views.enviarcorreogeneral,
         name="enviarcorreogeneral"),
    path("ingresar", views.ingresar, name="ingresar"),
    path("salir", views.salir_view, name="salir"),
    path("gerente", views.gerente, name="gerente"),
    path("almacenista", views.almacenista, name="almacenista"),
    path("directoroperativo", views.directoroperativo,
         name="directoroperativo"),
    path("contratista", views.contratista, name="contratista"),
    path("signup", views.signup_view, name="signup")
]
