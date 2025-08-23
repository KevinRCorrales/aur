# aur

Este es un pequeño mirror donde guardo en distintas ramas copias de los repositorios AUR de los paquetes que uso en mi Arch Linux.

## ADVERTENCIA

EL [AUR](https://aur.archlinux.org) ES UN REPOSITORIO COMUNITARIO DONDE CUALQUIERA PUEDE SUBIR UN PKGBUILD, MÁS INFO [AQUÍ](https://wiki.archlinux.org/title/Arch_User_Repository).

Las ramas de los paquetes que subo son copias exactas de las que hay en el AUR, sin modificaciones ni adaptaciones mías, algunos paquetes pueden ser de software que no es de código abierto y en ciertos casos hay paquetes del AUR que pueden ser malware, sin embargo, este repositorio, ni ninguno en el AUR, distribuye binarios ya compilados o código fuente, los PKGBUILD son solo scripts con instrucciones para crear un paquete para instalar con el gestor PacMan, en cuanto a malware, intento hacer la mejor selección de los paquetes que subo aquí y uso, a pesar de esto, es el usuario final quien debe verificar la integridad del PKGBUILD, esto esta claro en la wiki de Arch Linux:

Warning
AUR packages are user-produced content. These PKGBUILDs are completely unofficial and have not been thoroughly vetted. Any use of the provided files is at your own risk.

Más información sobre PacMan y los PKGBUILD aquí: [PacMan](https://wiki.archlinux.org/title/Pacman) y [PKGBUILD](https://wiki.archlinux.org/title/PKGBUILD).

## Objetivo de este repositorio

El objetivo de esto es aprender sobre control de versiones con Git, manejo de paquetes en distribuciones de Linux (en este caso Arch), gestión de mirrors y copias de archivos importantes (en este caso los PKGBUILD que uso del AUR) en caso de problemas con el servidor principal.

## Scripts en la rama main

A diferencia de los PKGBUILD de las múltiples ramas en este repositorio, los programas en la rama main sí son de mi creación y los uso para automatizar trabajos en este repositorio como añadir nuevas ramas o actualizar todas las ramas.

## PKGBUILDs de mi autoría

LAS ÚNICAS RAMAS QUE MANTENGO EN EL AUR REAL Y QUE ESTÁN AQUÍ CLONADOS SON:

### rama uaspl-bin

[repositorio en AUR](https://aur.archlinux.org/packages/uaspl-bin) y [repositorio en GitHub](https://github.com/KevinCrrl/UASPL)

### rama kpa-bin

[repositorio en AUR](https://aur.archlinux.org/packages/kpa-bin) y [repositorio en GitHub](https://github.com/KevinCrrl/kpa)

Aún así se recomienda revisar los PKGBUILD sean o no creador por mí en caso de querer usar alguno, el uso de estos archivos no es mi responsabilidad, es del usuario.

---
**Nota:** Este proyecto es de carácter personal/educativo,  
no está afiliado oficialmente ni con Arch Linux ni con mi Universidad.