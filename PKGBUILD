pkgname=kpa-bin
pkgver=1.0.1
pkgrel=1
pkgdesc="KevinCrrl Python AUR helper"
arch=('x86_64')
url="https://github.com/KevinCrrl/kpa"
license=('GPL3')
depends=('pacman' 'coreutils' 'git' 'base-devel')
source=("https://github.com/KevinCrrl/kpa/releases/download/${pkgver}/kpa-${pkgver}")
sha256sums=('65c7bbac8d1f77d60bd037ebe6cd81509b9a78991ab55e5d1900049b72e95131')

package() {
    install -Dm755 "kpa-${pkgver}" "$pkgdir/usr/bin/kpa"
}
