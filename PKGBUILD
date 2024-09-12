# Maintainer: Nemo <archlinux at captnemo dot in>
# Co-maintainer: Eduard T <edu4rdshl>
pkgname=signal-desktop-beta-bin
pkgrel=1
pkgdesc="Private messaging from your desktop"
arch=('x86_64')
url='https://signal.org'
license=('GPL3')
depends=('libnotify' 'libxtst' 'nss' 'xdg-utils' 'libxss')
options=('!strip' '!emptydirs')
install=${pkgname}.install
provides=('signal-desktop-beta')
_pkgver=7.25.0-beta.1
pkgver=${_pkgver/-/}
source=("https://updates.signal.org/desktop/apt/pool/s/signal-desktop-beta/signal-desktop-beta_${_pkgver}_amd64.deb")
sha256sums=('f4f5abb0615ac00da427b71021ff65df439dbaa502e4373138db2e38fed2d010')

package(){
  # Extract package data
  tar xf data.tar.xz -C "${pkgdir}"
}
