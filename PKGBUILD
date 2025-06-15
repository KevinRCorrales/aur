pkgname=uaspl-bin
pkgver=1.2.0
pkgrel=1
pkgdesc="UASPL Automatizado para la Seguridad y Protección de Linux"
arch=('x86_64')
url="https://github.com/KevinCrrl/UASPL"
license=('GPL3')
# No es necesario poner dependencias como Python, python-colorama, etc ya que el paquete está compilado por ende es independiente.
# Y solo necesita de estas 5 mostradas abajo que se ejecutan en comandos dentro del programa, es decir no están integradas, solo se llaman para ser ejecutadas.
depends=('clamav' 'ufw' 'rkhunter' 'systemd' 'sudo')
source=("https://github.com/KevinCrrl/UASPL/releases/download/${pkgver}/uaspl-${pkgver}" "LICENSE" "README.md")
sha256sums=('1ff9f8fe24c99137b29e14c2c54fd30ca2cdf49f6c68b10c70d7a30ee305cf09'
     'SKIP' 'SKIP')

package() {
    install -Dm755 "uaspl-${pkgver}" "$pkgdir/usr/bin/uaspl"
    install -Dm644 "LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -Dm644 "README.md" "$pkgdir/usr/share/doc/$pkgname/README.md"
}
