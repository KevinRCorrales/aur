pkgname=uaspl-bin
pkgver=1.0.0
pkgrel=1
pkgdesc="UASPL Automatizado para la Seguridad y Protección de Linux"
arch=('x86_64')
url="https://github.com/KevinCrrl/UASPL"
license=('GPL3')
depends=('clamav' 'ufw' 'rkhunter')
source=("https://github.com/KevinCrrl/UASPL/releases/download/${pkgver}/uaspl" "LICENSE" "README.md")
sha256sums=('SKIP' 'SKIP' 'SKIP')

package() {
    install -Dm755 "uaspl" "$pkgdir/usr/bin/uaspl"
    install -Dm644 "LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -Dm644 "README.md" "$pkgdir/usr/share/doc/$pkgname/README.md"
}
