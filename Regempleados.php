<?php 

    session_start();

    // Inicializa $_SESSION['empleados'] si no está definido
if (!isset($_SESSION['empleados'])) {
    $_SESSION['empleados'] = array();
}

    $msg = "";

    if(isset($_POST['nombre']) && isset($_POST['dni']) && isset($_POST['sueldo'])){
        
        array_push($_SESSION['empleados'], $_POST);
        $msg = "Empleado guardado correctamente";
    
    }

?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registrar Empleados</title>
</head>
<body>
    <h1>Registrar Empleados</h1>
    <form action="" method="POST">

        <label for="nombre">Nombres:</label>
        <input type="text" id="nombre" name="nombre" required><br>

        <label for="dni">DNI:</label>
        <input type="text" id="dni" name="dni" required><br>

        <label for="sueldo">Sueldo:</label>
        <input type="namber" id="sueldo" name="sueldo" required><br>

        <label for="descuento">Descuento:</label>
        <input type="namber" id="descuento" name="descuento" required><br>

        <label for="sexo">Sexo:</label>
        <select name="sexo" id="sexo">
            <option value="">Seleccionar</option>
            <option value="M">Masculino</option>
            <option value="F">Femenino</option>
        </select><br>

        <label for="edad">Edad:</label>
        <input type="namber" id="edad" name="edad" required><br>

        <label for="estado_civil">Estado Civil:</label>
        <select name="estado_civil" id="estado_civil">
            <option value="">Seleccionar</option>
            <option value="S">Soltero</option>
            <option value="C">Casado</option>
        </select><br>

        <input type="checkbox" name="seguro_social" id="seguro_social" value="S">Seguro Social<br>

        <input type="checkbox" name="seguro_social" id="seguro_social" value="S">AFP<br>

        <button type="submit">Guardar Empleado</button>

        <a href="index.php">Regresar al menú</a>
        <label><?=$msg?></label>
    </form>
</body>
</html>