pkgname=kpa-bin
pkgver=1.4.0
pkgrel=1
pkgdesc="KevinCrrl Python AUR helper"
arch=('x86_64' 'aarch64')
url="https://github.com/KevinCrrl/kpa"
license=('GPL-3')
depends=('pacman' 'git' 'base-devel' 'zlib' 'glibc')
optdepends=('torsocks' 'tor' 'sudo' 'doas')
source_x86_64=("https://github.com/KevinCrrl/kpa/releases/download/${pkgver}/kpa-x86_64-${pkgver}")
sha256sums_x86_64=('9544f85a4bde3ec51da2a40442dcfb7c4562b6927d68b594d68c42ce0010f291')

source_aarch64=("https://github.com/KevinCrrl/kpa/releases/download/${pkgver}/kpa-aarch64-${pkgver}")
sha256sums_aarch64=('3dbb23484bff66efb7f8c45d3e5a59370ea06cba714f3ad46d6c8b7398360e7b')

package() {
    local binaryname="kpa-${CARCH}-${pkgver}"
    install -Dm755 "$srcdir/$binaryname" "$pkgdir/usr/bin/kpa"
}
