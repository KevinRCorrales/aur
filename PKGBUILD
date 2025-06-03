pkgname=kpa-bin
pkgver=1.0.1
pkgrel=1
pkgdesc="KevinCrrl Python AUR helper"
arch=('x86_64')
url="https://github.com/KevinCrrl/kpa"
license=('GPL3')
depends=('pacman' 'coreutils' 'git' 'base-devel')
source=("https://github.com/KevinCrrl/kpa/releases/download/${pkgver}/kpa-${pkgver}")
sha256sums=('b437ed6fabaeca171f8f8b67baa2b649b63b83b5391fcfa042d74979eb7c55fa')

package() {
    install -Dm755 "kpa-${pkgver}" "$pkgdir/usr/bin/kpa"
}
