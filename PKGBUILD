# Maintainer: Cristophero <cristophero.alvarado@gmail.com>
pkgname=pseint-bin
pkgver=20200501
pkgrel=1
pkgdesc="Una herramienta para aprender las bases de la programación en Español-23-03-2021"
arch=('x86_64')
url="http://pseint.sourceforge.net"
license=('GPL')
conflicts=('pseint')
groups=()
depends=('libpng12' 'glu')
makedepends=()
optdepends=()
source=(https://razaoinfo.dl.sourceforge.net/project/pseint/${pkgver}/pseint-l64-${pkgver}.tgz)
noextract=()
sha256sums=()

package() {
    mkdir -p "${pkgdir}/opt/pseint"
    cp -rv "${srcdir}/pseint/"* "${pkgdir}/opt/pseint"
    mkdir -p "${pkgdir}/usr/share/applications/"
    desktopfile="${pkgdir}/opt/pseint/pseint.desktop"
    touch $desktopfile
    echo "[Desktop Entry]" >> $desktopfile
    echo "Type=Application" >> $desktopfile
    echo "Name=PSeInt" >> $desktopfile
    echo "Comment=${pkgdesc}" >> $desktopfile
    echo "Comment[es]=Una herramienta para aprender las bases de la programación mediante pseudocodigo en español" >> $desktopfile
    echo "Exec=pseint" >> $desktopfile
    echo "Icon=/opt/pseint/imgs/icon.svg" >> $desktopfile
    echo "Terminal=false" >> $desktopfile
    echo "Categories=Development;IDE;" >> $desktopfile
    mkdir -p "${pkgdir}/usr/share/applications/"
    cp $desktopfile "${pkgdir}/usr/share/applications/"
    mkdir -p "${pkgdir}/usr/bin/"
    touch "${pkgdir}/usr/bin/pseint"
    echo "#!/usr/bin/env sh" >> "${pkgdir}/usr/bin/pseint"
    echo "/opt/pseint/wxPSeInt" >> "${pkgdir}/usr/bin/pseint"
    chmod +x "${pkgdir}/usr/bin/pseint"
}
