# Role

$ ansible-galaxy init ROLENAME
    
    .
    └── knownhosts
        ├── README.md
        ├── defaults                Meteremos las variables del role que la gente vaya a modificar
        │   └── main.yml
        ├── files                   Ficheros que nuestro role (tareas) puedan usar
        ├── handlers                Handlers que puedan ser lanzados desde esas tareas
        │   └── main.yml
        ├── meta                    Donde hay metadatos (nombre del rol, licencia, sitio web) que se compartirán si publicamos el role
        │   └── main.yml
        ├── tasks
        │   └── main.yml            Tareas reutilizables
        ├── templates               Plantillas que usen nuestras taras
        ├── tests                   Pruebas del rol, para ver si funciona
        │   ├── inventory               Inventario de prueba
        │   └── test.yml                Playbook de prueba
        └── vars                    Meteremos nuestras propias variables que no quiero que me toquen
            └── main.yml