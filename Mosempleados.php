<?php
    session_start();
    $empleados = $_SESSION['empleados'];
    // var_dump($empleados);
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aplicación web de empleados</title>
</head>
<body>
    <h4>Lista de Empleados</h4>
    <a href="index.php">Regresar al menú</a>
    <table border="1">
        <tr>
            <th>Nombres</th>
            <th>DNIFEFWEFWE</th>
            <th>Sexo</th>
            <th>Edad</th>
            <th>Estado Civil</th>
        </tr>
        <?php foreach($empleados AS $empleado) { ?>
        <tr>
            <td><?=$empleado['nombre']?></td>
            <td><?=$empleado['dni']?></td>
            <td><?=$empleado['sexo']?></td>
            <td><?=$empleado['edad']?></td>
            <td><?=$empleado['estado_civil']?></td>
        </tr>
        <?php  } ?>
    </table>
</body>
</html>