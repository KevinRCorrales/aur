pkgname=kpa-bin
pkgver=1.3.0
pkgrel=1
pkgdesc="KevinCrrl Python AUR helper"
arch=('x86_64' 'aarch64')
url="https://github.com/KevinCrrl/kpa"
license=('GPL-3')
depends=('pacman' 'git' 'base-devel')
optdepends=('torsocks' 'tor' 'sudo' 'doas')
source_x86_64=("https://github.com/KevinCrrl/kpa/releases/download/${pkgver}/kpa-x86_64-${pkgver}")
sha256sums_x86_64=('39a9d8c732a71e0cec4afad9aa9ad608c01668621b23988fcf8339fd65a2d791')

source_aarch64=("https://github.com/KevinCrrl/kpa/releases/download/${pkgver}/kpa-aarch64-${pkgver}")
sha256sums_aarch64=('d5cee07c40f9bc3617e39b10fa940ecbac36215f9a92b1e973997f465f34f3b4')

package() {
    local binaryname="kpa-${CARCH}-${pkgver}"
    install -Dm755 "$srcdir/$binaryname" "$pkgdir/usr/bin/kpa"
}
