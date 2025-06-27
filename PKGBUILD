pkgname=kpa-bin
pkgver=1.2.0
pkgrel=1
pkgdesc="KevinCrrl Python AUR helper"
arch=('x86_64' 'aarch64')
url="https://github.com/KevinCrrl/kpa"
license=('GPL-3')
depends=('pacman' 'coreutils' 'git' 'base-devel')
optdepends=('torsocks' 'tor')
source_x86_64=("https://github.com/KevinCrrl/kpa/releases/download/${pkgver}/kpa-x86_64-${pkgver}")
sha256sums_x86_64=('d8e5fe326270e6ded54b07836664c7d19097c70a37650b8aedfddd3924beec14')

source_aarch64=("https://github.com/KevinCrrl/kpa/releases/download/${pkgver}/kpa-aarch64-${pkgver}")
sha256sums_aarch64=('8565af104b870771c78b067df2f05992114979b089a90d1eaa397890714b618f')

package() {
    local binaryname="kpa-${CARCH}-${pkgver}"
    install -Dm755 "$srcdir/$binaryname" "$pkgdir/usr/bin/kpa"
}
