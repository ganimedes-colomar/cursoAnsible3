# Inventarios

Catalogo de entornos sobre los que vamos a ejecutar nuestros playbooks

Ansible NOS OFRECE 3 sintaxis para crear inventarios:
- Ficheros .ini
- Ficheros .yaml
- Carpeta


# Contenedor

Es un entorno aislado dentro de un SO Linux donde ejecutar procesos.
Entorno aislado:
- Tiene su propia configuración de red -> su propia IP.. en una red virtual que genera el gestor de contenedores: DOCKER
- Tiene su propio sistema de archivos
- Tiene sus propias variables de entorno
- Puede tener limitaciones de acceso al Hardware

Hoy en día es la forma estandar de distirbuir, desplegar y ejecutar apliaciones.
Los contenedores los creamos de imagenes de contenedor.

# Imagen del contenedor

Fichero comprimido (.tar) que dentro tiene una estructura de carpetas compatible con POSIX (boot, root, home, var, bin, lib, etc)
Y además, en esas carpetas instalado y configurado una serie de programas.

Las encontramos en registries de repos de imagenes de contenedor: 
- Docker hub


rastasheep