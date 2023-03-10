Queremos un playbook, con tags

Y llevarlo a TOWER en una orquestación:
- Proyecto - Reutilziar
- Inventario
- Playbook
    - Survey <- Formulario (pediremos la variable VUESTRO NOMBRE)
- Orquestación

Playbook
variable:
    VUESTRO NOMBRE
3 tareas:
    1- Crear la carpeta /datos/VUESTRO NOMBRE
        TAG: GENERARFICHERO
    2- Generar un archivo desde una plantilla JINJA, que contenga:
        Este archivo ha sido creador por: VUESTRO NOMBRE
        TAG: GENERARFICHERO
        
        
    3- Comprobar que el archivo existe y contiene vuestro nombre
        TAG: PRUEBA
        