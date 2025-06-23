pkgname=uaspl-bin
pkgver=1.2.1
pkgrel=1
pkgdesc="UASPL Automatizado para la Seguridad y Protección de Linux"
arch=('x86_64')
url="https://github.com/KevinCrrl/UASPL"
license=('GPL3')
# No es necesario poner dependencias como Python, python-colorama, etc ya que el paquete está compilado por ende es independiente.
# Y solo necesita de estas 5 mostradas abajo que se ejecutan en comandos dentro del programa, es decir no están integradas, solo se llaman para ser ejecutadas.
depends=('clamav' 'ufw' 'rkhunter' 'systemd' 'sudo')
source=("https://github.com/KevinCrrl/UASPL/releases/download/${pkgver}/uaspl-${pkgver}" "LICENSE")
sha256sums=('eccc4277e16fa1b28346bf8c60585877531433f8f80c98fc82d78c9a90f3278b' 'SKIP')

package() {
    install -Dm755 "uaspl-${pkgver}" "$pkgdir/usr/bin/uaspl"
    install -Dm644 "LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -Dm644 "README.md" "$pkgdir/usr/share/doc/$pkgname/README.md"
}
