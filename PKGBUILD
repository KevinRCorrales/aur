pkgname=kpa-bin
pkgver=1.1.0
pkgrel=1
pkgdesc="KevinCrrl Python AUR helper"
arch=('x86_64' 'aarch64')
url="https://github.com/KevinCrrl/kpa"
license=('GPL3')
depends=('pacman' 'coreutils' 'git' 'base-devel')

source_x86_64=("https://github.com/KevinCrrl/kpa/releases/download/${pkgver}/kpa-x86_64-${pkgver}")
sha256sums_x86_64=('66990c1b411f00a786af3631fdfe267a8c1509197d52c162b93283e1dc9e1443')

source_aarch64=("https://github.com/KevinCrrl/kpa/releases/download/${pkgver}/kpa-aarch64-${pkgver}")
sha256sums_aarch64=('afbfc4247a224c47ee6aba74eba6ba01b0c360d024b84aac1a3db1c205dfa466')

package() {
    local binaryname="kpa-${CARCH}-${pkgver}"
    install -Dm755 "$srcdir/$binaryname" "$pkgdir/usr/bin/kpa"
}
