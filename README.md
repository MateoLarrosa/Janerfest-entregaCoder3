# Janerfest-entregaCoder3
-------------------------------------------------------------------------------------

pasos a seguir para acceder a la pagina web
--------------------------------------------------------------------------------------
1- clonar este repositorio de github. Entras a la terminal de git y ejecutas el siguiente comando:
"git clone https://github.com/MateoLarrosa/Janerfest-entregaCoder3.git"

2- Cuando ya tengas el proyecto tendras que implementar los paquetes que se requieren (los cuales estan en el archivo "requeriments.txt") a tu entorno virtual.Lo haras ejecutando lo siguiente en la terminal  =  "pip install -r requeriments.txt".

3- Levantar la base de datos: para poder levantar la base de datos tendras que ejecutar en la terminal el siguiente comando = "python manage.py migrate"

4- Por ultimo para levantar el servidor y acceder a la web tendras que ejecutar en la terminal el siguiente comando = "py manage.py runserver"

Acceso a la web
----------------------------------------------------------------------------------
para acceder a la pagina web, vas a tener que ingresar a continuacion de la URL "http://127.0.0.1:8000/" lo siguiente = "entradas/".

Esta pagina web esta creada con el fin de sacar entradas para un festival escolar.
Tambien tiene otros apartados para conocer a sus creadores y a sus sponsors pero se veran mas adelante.
Para poder completar el formulario podes acceder al mismo de dos formas y con dos simples pasos.

1- en la pantalla de inicio clikear en el boton "+ info sobre entradas" que te lleva a la seccion de "entradas" o ir directamente desde la barra de navegacion de la web al apartado "entradas"

2- clickea en el boton "saca tus entradas!!" que te lleva al formulario o scrolea para abajo.
pasos obligatorios para poder complterar el formulario:

1-nombre completo

2- mail al que quiera que le lleguen las entradas

3-cant de entradas que quiera comprar

4- si tiene un hijo/a que participa

Si desea consultar en que estado se encuentra su compra, una vez que complete el formulario y lo envie se la llevara al apartado de "mis entradas" donde usted podra por medio de su nombre con el que se registro saber en que estado se encuentra su compra. los estados pueden ser: "ASEGURADAS","YA ENVIADAS" o le puede aparecer que no esta en nuestra base de datos
