# Maintainer: Nemo <archlinux at captnemo dot in>
pkgname=signal-desktop-beta-bin
pkgrel=1
pkgdesc="Private messaging from your desktop"
arch=('x86_64')
url="https://github.com/WhisperSystems/Signal-Desktop#readme"
license=('GPL3')
depends=('gconf' 'gtk2' 'libnotify' 'libxtst' 'nss' 'xdg-utils' 'libxss')
options=('!strip' '!emptydirs')
install=${pkgname}.install
provides=('signal-desktop-beta')

pkgver=1.34.0beta.3
source=("https://updates.signal.org/desktop/apt/pool/main/s/signal-desktop-beta/signal-desktop-beta_1.34.0-beta.3_amd64.deb")
sha256sums=('70675854ddfebc6e5a834c3857146b7976f91964b3773c83db34c4b0aa1645be')

package(){
	# Extract package data
	tar xf data.tar.xz -C "${pkgdir}"
}
