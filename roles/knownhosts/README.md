# Knownhosts

Deja preparado el entorno local para poder contectarse con un remoto por ssh, **añadiendo los fingerprints** al archivo `knownhosts`.

Estos evita al ejecutar playbooks de ansible, problemas como:
![Tooltip](https://linuxhandbook.com/content/images/2022/09/ssh-known-hosts.png)

Internamente usa los comandos:
- `ssh-keygen -F <IP>`.  Ver si tengo un host (IP) dado de alta entre los reconocidos
- `ssh-keyscan -H <IP>`. Ese me da las huellas del entorno usando distintos algoritmos de generación de huella:
- `ssh-keygen -R <IP>`. Borra las entradas del host (IP) en el known_hosts

Admite los siguientes algoritmos de fingerprint:
- rsa
- ecdsa
- ed25519


## Variables

| Variable                             | Valor por defecto | Uso                                                                      |
| ------------------------------------ | ----------------- | ------------------------------------------------------------------------ |
| `generate_finger_print_on_unknown`   | `False`           | Generar entradas en `knownhosts`para hosts desconocidos                  |
| `regenerate_finger_print_on_changed` | `False`           | Regenerar entradas en `knownhosts`para hosts que hayan cambiado          |
| `log_file`                           | `"./log.txt"`     | Archivo donde generar logs de los eventos                                |
| `default_fingerprint_algorythm`      | `ssh-rsa`         | Algoritmo para generar los fingerprints, a elegir entre: `ssh-rsa`, `ecdsa-sha2-nistp256` o `ssh-ed25519`|

## Ejemplo de uso:

```yaml
  tasks:
      -   name: Ejecutar el role
          include_role: 
              name: knownhosts
          vars:
            generate_finger_print_on_unknown:   True
            regenerate_finger_print_on_changed: True
            log_file:                           "./milog.txt"
            default_fingerprint_algorythm:      ssh-ed25519
```

Si quisiera poner un enlace: [Ir a google](https://www.google.es)

