# Maintainer: Plague-doctor <plague <at>> privacyrequired <<dot>> com >
# Contributor: me at oguzkaganeren dot com dot tr
# Contributor: Rowisi < nomail <at> private <dot> com >

pkgname=vscodium-bin
pkgver=1.44.0
pkgrel=1
pkgdesc="Binary releases of VS Code without MS branding/telemetry/licensing."
arch=('x86_64' 'aarch64' 'armv7h')
url="https://github.com/VSCodium/vscodium"
license=('MIT')
depends=(
        fontconfig libxtst gtk3 python cairo alsa-lib nss gcc-libs libnotify libxss
        'glibc>=2.28-4'
        )
optdepends=(
        'gvfs: For move to trash functionality'
        'libdbusmenu-glib: For KDE global menu'
)
provides=('code')
conflicts=('code')
source=(vscodium-bin.desktop)
sha256sums=('5504e93bd55f2bc068c29e4fa962c1eddc6e08edb39c3255319dd5ad998a1b86')

source_x86_64=("${pkgname}-${pkgver}-${pkgrel}-x86_64.tar.gz::${url}/releases/download/${pkgver}/VSCodium-linux-x64-${pkgver}.tar.gz")
source_aarch64=("${pkgname}-${pkgver}-${pkgrel}-aarch64.tar.gz::${url}/releases/download/${pkgver}/VSCodium-linux-arm64-${pkgver}.tar.gz")
source_armv7h=("${pkgname}-${pkgver}-${pkgrel}-armv7h.tar.gz::${url}/releases/download/${pkgver}/VSCodium-linux-arm-${pkgver}.tar.gz")

sha256sums_x86_64=('0f842932e6a4db3510a171a54aac457f96fc4f6a75562b8d2e20fd927f263bdf')
sha256sums_aarch64=('abf4f9aa0a2c2c6927a4a2d52463366b325a3ac738cfedeed827cf0b36b35315')
sha256sums_armv7h=('314ee25c1c8f86eb1d144b36b9f251de875fe2807c86bf5564a452662c3deac2')

noextract=("${pkgname}-${pkgver}-${pkgrel}-${CARCH}.tar.gz")

prepare() {
    mkdir -p ${srcdir}/${pkgname}
    tar -xf ${srcdir}/${pkgname}-${pkgver}-${pkgrel}-${CARCH}.tar.gz -C ${srcdir}/${pkgname}
}

package() {
    install -d -m755 ${pkgdir}/usr/bin
    install -d -m755 ${pkgdir}/usr/share/{${pkgname},applications,pixmaps}
    cp -r ${srcdir}/${pkgname} ${pkgdir}/usr/share
    ln -s /usr/share/${pkgname}/bin/codium ${pkgdir}/usr/bin/code
    ln -s /usr/share/${pkgname}/bin/codium ${pkgdir}/usr/bin/codium
    ln -s /usr/share/${pkgname}/bin/codium ${pkgdir}/usr/bin/vscodium
    install -D -m644 vscodium-bin.desktop ${pkgdir}/usr/share/applications/${pkgname}.desktop
    install -D -m644 ${srcdir}/${pkgname}/resources/app/resources/linux/code.png \
            ${pkgdir}/usr/share/pixmaps/vscodium.png
}
