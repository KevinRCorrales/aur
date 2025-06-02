pkgname=kpa-bin
pkgver=1.0.0
pkgrel=1
pkgdesc="KevinCrrl Python AUR helper"
arch=('x86_64')
url="https://github.com/KevinCrrl/kpa"
license=('GPL3')
depends=('pacman' 'coreutils' 'git' 'base-devel')
source=("https://github.com/KevinCrrl/kpa/releases/download/${pkgver}/kpa-${pkgver}")
sha256sums=('baf50f17a6e5fef3ede56113bac838a636cc11b124ad131da6833f4b2b1fcb43')

package() {
    install -Dm755 "kpa-${pkgver}" "$pkgdir/usr/bin/kpa"
}
