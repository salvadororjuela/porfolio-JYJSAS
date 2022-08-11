from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import ManyToManyField
# Para hacer suma de productos en almacen
from django.db.models import Sum

# Create your models here.
# Modelo modificado para usuarios en admin


class CustomUser(AbstractUser):
    identificacion = models.PositiveBigIntegerField(
        default="0000000000")
    # Diccionario de las opciones de cargos para mostrar en admin
    cargos = [
        ("Gerente General", "Director General"),
        ("Director Operacional", "Director Operacional"),
        ("Almacenista", "Almacenista"),
        ("Contratista", "Contratista")
    ]
    # choices toma los valores de la lista cargos (arriba declarada) y crea una
    # lista desplegable de los cargos en admin
    cargo_empleado = models.CharField(
        max_length=50, choices=cargos, default="Contratista")
    telefono_empleado = models.PositiveBigIntegerField(default="0000000000")
    correo_empleado = models.EmailField(default="ejemplo@ejemplo.com")


# Registro de proveedores
class Proveedores(models.Model):
    codigo_proveedor = models.AutoField(primary_key=True)  # llave primaria
    nombre_proveedor = models.CharField(max_length=50)
    direccion_proveedor = models.CharField(max_length=100)
    barrio_proveedor = models.CharField(max_length=50)
    ciudad_proveedor = models.CharField(max_length=50)
    telefono_proveedor = models.PositiveBigIntegerField()
    website_proveedor = models.CharField(max_length=50)
    email = models.EmailField(default="ejemplo@ejemplo.com")
    # Diccionario de las opciones disponibles de crédito para mostrar en admin
    credito = [
        ("Si", "Si Maneja Crédito"),
        ("No", "No Ofrece Crédito"),
    ]
    # choices toma los valores de la lista cargos (arriba declarada) y crea una
    # lista desplegable de las opciones de crédito
    maneja_credito = models.CharField(
        max_length=20, choices=credito, default="No")

    def __str__(self):
        return f"{self.nombre_proveedor}"


# Usada para registrar los ingresos de materias primas al almacén
class Materia_prima (models.Model):
    codigo_producto = models.AutoField(primary_key=True)  # llave primaria
    nombre_producto = models.CharField(max_length=100)
    fecha_ingreso_materiaprima = models.DateTimeField(auto_now_add=True)
    unidades = [
        ("Un", "Unidad"), ("Lb", "Libras"), ("Kg", "Kilogramos"),
        ("In", "Pulgadas"), ("Cm", "Centimetros"), ("Mt", "Metros"),
        ("Pi", "Pies"), ("M2", "Metros Cuadrados"), ("M3", "Metros Cubicos"),
        ("Lt", "Litros"), ("Ml", "Mililitros"), ("Gl", "Galones"),
        ("1/16", "1/16 de Galón"), ("1/8", "1/8 de Galón"),
        ("1/4", "1/4 de Galón"), ("1/2", "1/2 Galón"),
    ]
    unidad_de_medida = models.CharField(
        max_length=15, choices=unidades, default="Un")
    precio_unitario = models.PositiveIntegerField()
    marca = models.CharField(max_length=100, null=True)

    # Muchas materias primas pueden tener muchos proveedores
    Proveedores_cod_proveedor = ManyToManyField(Proveedores)

    # Para poder mostrar un campo many to many en el admin se usa una funcion
    # que obtenga la informacion como una cadena y la deje leer por la class
    # MateriaPrimaAdmin en inventarios/admin.py
    def Proveedor(self):
        return ', '.join([Proveedores.nombre_proveedor for Proveedores in self.Proveedores_cod_proveedor.all()])
    Proveedor.short_description = "Proveedores"

    def __str__(self):
        return f"{self.nombre_producto} - cod: {self.codigo_producto} U.med: {self.unidad_de_medida}"


# Se usa para ingresar al almacen materia prima que ya ha sido registrada en el modelo
# Materia_prima
class EntradasAlmacen(models.Model):
    id = models.AutoField(primary_key=True)
    numero_factura_compra = models.CharField(
        max_length=100, default="0000000000")
    fecha_entrada = models.DateTimeField(auto_now_add=True)
    cantidad = models.PositiveIntegerField(default="1")
    codigo_material = models.ForeignKey(
        Materia_prima, null=False, on_delete=models.CASCADE, default="0")

    def __str__(self):
        return f"{self.numero_factura_compra}"


# Usada cuando el empleado encargado de un proyecto solicita materia prima al
# alamacén
class ordenes_pedido_materiaprima (models.Model):
    codigo_orden_pedido = models.AutoField(
        primary_key=True)  # llave primaria
    codigo_producto = models.ForeignKey(
        Materia_prima, null=False, on_delete=models.CASCADE)  # llave foranea
    cantidad_pedida = models.PositiveIntegerField()
    fecha_orden_pedido = models.DateTimeField(auto_now_add=True)
    # llave foranea
    empleado_solicitante = models.ForeignKey(
        CustomUser, null=False, on_delete=models.CASCADE, default="-------")


# Registro de los proyectos que tiene la compañía
class Proyectos (models.Model):
    codigo_proyecto = models.AutoField(primary_key=True)  # llave primaria
    nombre_proyecto = models.CharField(max_length=100)
    direccion_proyecto = models.CharField(max_length=100)
    descripcion_proyecto = models.TextField()
    estado = [
        ("Act", "Activo"),
        ("Ter", "Terminado"),
        ("Na", "No Asignado"),
    ]
    estado_proyecto = models.CharField(
        max_length=12, choices=estado, default="Na")
    empleado_responsable = models.ForeignKey(
        CustomUser, null=False, on_delete=models.CASCADE)  # llave foranea

    def __str__(self):
        return f"{self.nombre_proyecto}"


# Usada para registrar las salidas de material del almacén
# Solamente puede haber una orden de salida por proyecto a la vez.
# No se puede tener una orden de salida para varios proyectos
class ordenes_salida_materiaprima (models.Model):
    codigo_orden_salida = models.AutoField(
        primary_key=True)  # llave primaria
    # Una orden de salida puede tener muchos materiales.
    producto = ManyToManyField(Materia_prima)
    cantidad_entregada = models.PositiveIntegerField()
    fecha_entrega_materiaprima = models.DateTimeField(auto_now_add=True)
    proyecto_destino = models.ForeignKey(
        Proyectos, null=False, on_delete=models.CASCADE)  # llave foranea
    empleado_responsable = models.ForeignKey(
        CustomUser, null=False, on_delete=models.CASCADE)  # llave foranea

    # Para poder mostrar un campo many to many en el admin se usa una funcion
    # que obtenga la informacion como una cadena y la deje leer por la class
    # OrdenesSalidaMateriaPrimaAdmin en inventarios/admin.py.
    def material(self):
        return ', '.join([Materia_prima.nombre_producto for Materia_prima in self.producto.all()])
    material.short_description = "Materia_prima"
   

# Registro de contratistas
class Contratistas (models.Model):
    codigo_contratista = models.AutoField(
        primary_key=True)  # llave primaria
    nombre_contratista = models.CharField(max_length=50)
    apellido_contratista = models.CharField(max_length=50, default="")
    identificacion = models.PositiveIntegerField(default="000000000")
    direccion_contratista = models.CharField(max_length=100)
    correo_contratista = models.EmailField(default="ejemplo@ejemplo.com")
    telefono_contratista = models.PositiveBigIntegerField()
    especialidad_contratista = models.CharField(max_length=50)
    # Un contratista puede tener muchos proyectos asignados
    proyecto_asignacion = ManyToManyField(Proyectos)

    # Para poder mostrar un campo many to many en el admin se usa una funcion
    # que obtenga la informacion como una cadena y la deje leer por la class
    # ProyectosAdmin en inventarios/admin.py
    def proyectos_asignados(self):
        return ', '.join([Proyectos.nombre_proyecto for Proyectos in self.proyecto_asignacion.all()])
    proyectos_asignados.short_description = "Proyectos"

    def __str__(self):
        return f"{self.nombre_contratista} {self.apellido_contratista}"
