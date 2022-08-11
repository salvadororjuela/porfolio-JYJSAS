from django.urls import path
from . import views


# Namespace para evitar conflicto entre urls llamadas igual pero en diferentes
# aplicaciones
app_name = "operaciones"

urlpatterns = [
     ############################ Paginas gerente ##############################
     path("", views.index, name="reportesinventario"),
     path("nuevomaterial", views.nuevomaterial, name="nuevomaterial"),
     path("nuevoproveedor", views.nuevoproveedor, name="nuevoproveedor"),
     path("nuevoproyecto", views.nuevoproyecto, name="nuevoproyecto"),
     path("nuevocontratista", views.nuevocontratista, name="nuevocontratista"),
     # Pagina de entradas de almacen
     path("entradaalmacen", views.entradaalmacen, name="entradaalmacen"),
     path("autsalidamaterial", views.autsalidamaterial,
          name="autsalidamaterial"),
     path("eliminarcontratista", views.eliminarcontratista,
          name="eliminarcontratista"),
     path("eliminarproducto", views.eliminarproducto, name="eliminarproducto"),
     path("eliminarproveedor", views.eliminarproveedor,
          name="eliminarproveedor"),
     path("eliminarproyecto", views.eliminarproyecto,
          name="eliminarproyecto"),
     # Pagina borrado exclusiva de un contratista
     path("borrarcontratista<int:codigo_contratista>", views.borrarcontratista,
          name="borrarcontratista"),
     # Pagina borrado exclusiva de un producto de almacen
     path("borrarproducto<int:codigo_producto>", views.borrarproducto,
          name="borrarproducto"),
     # Pagina borrado exclusiva de un proveedor
     path("borrarproveedor<int:codigo_proveedor>", views.borrarproveedor,
          name="borrarproveedor"),
     # Pagina borrado exclusiva de un proyecto
     path("borrarproyecto<int:codigo_proyecto>", views.borrarproyecto,
          name="borrarproyecto"),
     # Pagina para editar exclusivamente a un contratista
     path("editarcontratista<int:codigo_contratista>", views.editarcontratista,
          name="editarcontratista"),
     # Pagina de edicion exclusiva de un producto
     path("editarproducto<int:codigo_producto>", views.editarproducto,
          name="editarproducto"),     
     # Pagina de edicion exclusiva de un proveedor
     path("editarproveedor<int:codigo_proveedor>",
          views.editarproveedor, name="editarproveedor"),
     # Pagina de edicion exclusiva de un proyecto
     path("editarproyecto<int:codigo_proyecto>", views.editarproyecto,
          name="editarproyecto"),
     # Ruta para redirecionar al gerente al menu de el mismo
     path("redirecciongerente", views.redirecciongerente,
          name="redirecciongerente"),  # Redirecciona al menu del gerente
     
     # ######################### Paginas almacenista ########################
     path("almacenistanuevomaterial", views.almacenistanuevomaterial,
          name="almacenistanuevomaterial"),
     # Pagina que lista todos los productos del almacen
     path("almacenistalistaproductos", views.almacenistalistaproductos,
          name="almacenistalistaproductos"),
     # Pagina para editar un producto especifico de la base de datos
     path("almacenistaeditarproducto<int:codigo_producto>", views.almacenistaeditarproducto,
          name="almacenistaeditarproducto"),
     # Pagina que lista todos los proveedores
     path("almacenistalistaproveedores", views.almacenistalistaproveedores,
          name="almacenistalistaproveedores"),
     # Pagina para editar un proveedor especifico de la base de datos
     path("almacenistaeditarproveedor<int:codigo_proveedor>",
          views.almacenistaeditarproveedor, name="almacenistaeditarproveedor"),
     path("salidaalmacen", views.salidaalmacen, name="salidaalmacen"),
     path("almacenistaentrada", views.almacenistaentrada,
          name="almacenistaentrada"),
     path("solautsalida", views.solautsalida, name="solautsalida"),
     path("almacenistareporteinventarios", views.almacenistareporteinventarios,
          name="almacenistareporteinventarios"),
     path("almacenistanuevoproveedor", views.almacenistanuevoproveedor,
          name="almacenistanuevoproveedor"),
     path("redireccionalmacenista", views.redireccionalmacenista,
          name="redireccionalmacenista"),  # Redirecciona al menu almacenista

     # ##################### Paginas director operativo #######################
     path("operativoreporteinventarios", views.operativoreporteinventarios,
          name="operativoreporteinventarios"),
     path("solicitudmateriales", views.solicitudmateriales,
          name="solicitudmateriales"),
     path("operativonuevoproyecto", views.operativonuevoproyecto,
          name="operativonuevoproyecto"),
     path("operativolistaproyectos", views.operativolistaproyectos,
          name="operativolistaproyectos"),
     path("operativoeditarproyecto<int:codigo_proyecto>",
          views.operativoeditarproyecto, name="operativoeditarproyecto"),
     path("redireccionoperativo", views.redireccionoperativo,
          name="redireccionoperativo"),  # Redirecciona al menu del operativo

     # ######################## Paginas contratistas ##########################
     path("proyectoscontratista", views.proyectoscontratista,
          name="proyectoscontratista"),
     # path("proyectoscontratista<int:pk>", views.proyectoscontratista,
     #      name="proyectoscontratista"),
     path("novedades", views.novedades, name="novedades"),
     path("enviarnovedades", views.enviarnovedades, name="enviarnovedades"),
     path("redireccioncontratista", views.redireccioncontratista,
         name="redireccioncontratista"),  # Redirecciona al menu contratistas
     
     # ###################### Paginas de Reportes #############################
     path("reportedisponibilidad", views.reportedisponibilidad,
          name="reportedisponibilidad"),
     path("reportedisponibilidadalmacenista",
          views.reportedisponibilidadalmacenista,
          name="reportedisponibilidadalmacenista"),
     path("reportedisponibilidadoperativo",
          views.reportedisponibilidadoperativo,
          name="reportedisponibilidadoperativo"),
     path("reporteporproyecto", views.reporteporproyecto,
          name="reporteporproyecto"),
     path("almacenistareporteporproyecto", views.almacenistareporteporproyecto,
          name="almacenistareporteporproyecto"),
     path("operativoreporteporproyecto", views.operativoreporteporproyecto,
          name="operativoreporteporproyecto")
]
