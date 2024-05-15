# Maintainer: dakataca <🐬danieldakataca@gmail.com>
# Contributor: Cristophero <cristophero.alvarado@gmail.com>

pkgname=pseint-bin
_pkgname=${pkgname%-*}
pkgver=20240122
pkgrel=1
pkgdesc='A tool for learning programming basis with a simple spanish pseudocode'
arch=('x86_64')
url='http://pseint.sourceforge.net'
license=('GPL2')
conflicts=("$_pkgname")
makedepends=('gendesk')
depends=('wxwidgets-gtk3' 'rsync')
noextract=(creator.psz)
source=("$_pkgname-$pkgver.tgz::https://cfhcable.dl.sourceforge.net/project/$_pkgname/$pkgver/$_pkgname-l64-$pkgver.tgz")
sha256sums=('4ed1945df7a2935ea8da2809ded71f737ddabcbeeaa4976d9b75f7567054b1c5')

# Función 'prepare': Prepara el entorno antes de compilar el paquete.
prepare(){
    cd $_pkgname

    # Utilidad 'gendesk' para generar el archivo .desktop.
    gendesk -f -n \
        --pkgname="$_pkgname" \
        --pkgdesc="$pkgdesc" \
        --name="$_pkgname" \
        --genericname="$_pkgname" \
        --comment="$pkgdesc" \
        --exec="$_pkgname" \
        --path="/opt/$_pkgname" \
        --icon="$_pkgname" \
        --categories='Development,Education'
}

# Función 'pkgver': Devuelve la versión del paquete.
pkgver(){
    cd $_pkgname
    cat version
}

# Función 'package': Empaqueta los archivos compilados en el paquete final.
package(){
    cd $_pkgname

    # Crear el directorio de destino y copiar en él, el contenido de pseint-bin.
    rsync -a . --mkpath "$pkgdir/opt/$_pkgname/"

    # Instala el archivo .desktop en la ubicación (-t) adecuada.
    install -Dvm644 "$_pkgname.desktop" -t "$pkgdir/usr/share/applications"

    # Instalar icono de pseint-bin.
    install -Dvm644 "imgs/icon.icns" "$pkgdir/usr/share/pixmaps/$_pkgname.icns"

    # Crea un archivo ejecutable en la ubicación /usr/bin/$_pkgname que ejecuta el programa wxPSeInt(pseint).
    install -Dvm755 <(echo -e '#!/usr/bin/env bash\n/opt/pseint/wxPSeInt') $pkgdir/usr/bin/$_pkgname
}

## Update:
# updpkgsums
# makepkg -si
# makepkg --printsrcinfo > .SRCINFO
# git clean -dfx

## References
# Example: https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=densify
# Site:    https://sourceforge.net/projects/pseint/files/
# Tarball: https://sourceforge.net/projects/pseint/files/20210609/pseint-l64-20210609.tgz/download
# WebHelp: https://wiki.archlinux.org/title/Desktop_entries#How_to_use
# WebHelp: https://www.gnu.org/software/bash/manual/html_node/Process-Substitution.html

## Clean:
# rm -rf pseint-* src/ pkg/

# 👤 Autor: https://t.me/dakataca 💻 🐬 #
