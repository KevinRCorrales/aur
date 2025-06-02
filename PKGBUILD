pkgname=kpa-bin
pkgver=1.0.0
pkgrel=1
pkgdesc="KevinCrrl Python AUR helper"
arch=('x86_64')
url="https://github.com/KevinCrrl/kpa"
license=('GPL3')
depends=('pacman' 'coreutils' 'git' 'base-devel')
source=("https://github.com/KevinCrrl/kpa/releases/download/${pkgver}/kpa-${pkgver}")
sha256sums=('baa4f7895efc076678748566e074db5fee5ec32f09da8ea4e5dd441ab9e2cec8')

package() {
    install -Dm755 "kpa-${pkgver}" "$pkgdir/usr/bin/kpa"
}
