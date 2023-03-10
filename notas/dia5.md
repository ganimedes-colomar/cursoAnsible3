# Custom facts

Son archivos que creamos en la carpeta /etc/ansible/facts.d del remoto.

El nombre del archivo será el nombre del fact(variable) que vamos a usar posteriormente en ansible.
De hecho, para usar ese dato, tendremos que escribir: -
- `ansible_local.NOMBRE_FACT`
- `ansible_facts.ansible_local.NOMBRE_FACT`

# CUSTOM FACT ESTÁTICO

El fichero que vamos a crear para un fact debe ser un json... y le ponemos extensión ".json"
La extensión no se tiene en cuenta en el nombre del fact:
`monitorizada.json` -> { "deployed": true, ... }
Para recuperar el dato: `ansible_local.monitorizada.deployed`

# CUSTOM FACT DINAMICO

Puedo crear un fichero ahí dentro de esa carpeta con mi lenguaje de programación de scripting favorito:
- bash
- ps1
- py
- perl

Que hace Ansible, ejecuta ese fichero 
(motivo por el cuál, el fichero necesita permisos de ejecución... eso es lo que mira Ansible)
De hecho Ansible no sabe en que lenguaje está escrito aquello... Para eso esta el SHEBANG !

Pasa igual que con los estáticos. El resultado del programa (stdout) se toma como valor del fact. Y al fact accedo
a través del nombre del archivo... sin extensión.