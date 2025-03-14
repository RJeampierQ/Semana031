<?php
    session_start();

    $busqueda = [];
    $busqueda['nombre'] = '';
    $busqueda['dni'] = '';
    $busqueda['sexo'] = '';
    $busqueda['edad'] = '';
    $busqueda['estado_civil'] = '';
    $busqueda['sueldo'] = '';
    $busqueda['descuento'] = '';

    $msg = "";

    if(isset($_GET['dni'])) {

        $dni_buscado = $_GET['dni'];

        foreach ($_SESSION['empleados'] as $empleado) {
            
            if ($empleado['dni'] == $dni_buscado) {

                $busqueda['nombre'] = $empleado['nombre'];
                $busqueda['dni'] = $empleado['dni'];
                $busqueda['sexo'] = $empleado['sexo'];
                $busqueda['edad'] = $empleado['edad'];
                $busqueda['estado_civil'] = $empleado['estado_civil'];
                $busqueda['sueldo'] = $empleado['sueldo'];
                $busqueda['descuento'] = $empleado['descuento'];
                
                break; 
            }
        }

        if(count($busqueda) > 0) {
            $msg = "Empleado encontrado";
        } else {
            $msg = "No se encontró al empleado, por favor verifique.";
        }
    }
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Buscar Empleado</title>
</head>
<body>
    <h1>Buscar Empleado</h1>
    <form action="" method="GET">
        <label for="dni">DNI del Empleado:</label>
        <input type="text" id="dni" name="dni" required>
        <button type="submit">Buscar</button>
        <a href="index.php">Regresar al menú</a>
    </form>
    <table border="1">
        <tr>
            <th>Nombres</th>
            <th>DNI</th>
            <th>Sexo</th>
            <th>Edad</th>
            <th>Estado Civil</th>
            <th>Sueldo</th>
            <th>Descuento</th>
            <th>Sueldo Neto</th>
        </tr>
        <tr>
            <td><?=$busqueda['nombre']?></td>
            <td><?=$busqueda['dni']?></td>
            <td><?=$busqueda['sexo']?></td>
            <td><?=$busqueda['edad']?></td>
            <td><?=$busqueda['descuento']?></td>
            <td><?=$busqueda['sueldo']?></td>
            <td><?=$busqueda['descuento']?></td>
            <td><?=intval($busqueda['sueldo']) - intval($busqueda['descuento'])?></td>
        </tr>
    </table>
    <label><?=$msg?></label>
</body>
</html>