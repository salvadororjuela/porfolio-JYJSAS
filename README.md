# porfolio-JYJSAS
This application was developed and taylored specifically for a company under business rules. These include: 1) Only the superuser can create new users. 2) Certain IDs are designated specifically for certain company positions (ie. 1=Managing Director, 2=Storer, 3= Operations Manager, 4 and on=contractors). 3) The application is designed to display some company general information to the general public and the functions of the page are only accesable to authorized employees with access credentials.


La aplicación está enfocada a dos grandes grupos de usuarios, el primero es el publico en general que puede ver en los enlaces información general de la empresa como la presentación, misión y visión de la empresa, así como  un formulario de contacto a través del cual se pueden recibir a un correo establecido preguntas, quejas y reclamos y que como se vé en la capacidad de enviar correos al email designado para tal fin

Para el segundo grupo de usuarios con credenciales de acceso, la aplicación determina el perfil del usuario con base en el cargo con que aparece registrado en la base de datos y lo redirecciona al menú específico de cada usuario.

Para el caso del perfíl del gerente, tiene permisos espciales que le facilitan acceder a la sección de la administración de la aplicación y otras acciones como la de crear usuarios nuevos, que son únicas para él.

En el caso de los nuevos usuarios, se crean al diligenciar los datos del formulario destinado para esta tarea y en el cual se puede determinar el perfil de cada usuario.

Una tarea importante es la creación de nuevas materias primas en la base de datos, y la aplicacion tiene formularios que funcionan eficientemente en este sentido.

Acá se puede ver cómo la información del ejemplo de nueva materia prima queda registrada en la base de datos y se evidencia en pantalla.

Una vez un producto es guardado en la base de datos, se puden registrar movimientos de ingreso o salida de material, como cuando se hace reabastecimiento de una materia prima o cuando ella sale para un determinado proyecto y es entregada al funcionario responsible.

Ocurre igual con el ingreso de nuevos proveedores, proyectos y contratistas.

Una función muy importante que se comparte con los perfiles del almacenista y parcialmente el director operativo, es la disponibilidad de formularios de edición de productos de inventario, proyectos y de contratistas.

Sin embargo la opción de borrar cualquier información de las tablas en las bases de datos, es exclusiva del gerente, quien puede hacerlo desde la sección de administración o de los formularios destinados para tal fin en la página web.

En este momento ustedes pueden ver cómo las funciones de la pagina web cambian de acuerdo con el perfil de usuario, en este caso del director operacional, que puede crear realizar actividades como crear y editar proyectos.

Finalmente, una opción muy importante que comparten el gerente, el director operativo y el almacenista, es la de generar reportes tanto de movimientos de material, cantidades de productos usadas por proyecto e imprimirlos en un documento pdf o en físico.
