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
provides=('signal-desktop')

pkgver=1.28.0beta.4
source=("https://updates.signal.org/desktop/apt/pool/main/s/signal-desktop-beta/signal-desktop-beta_1.28.0-beta.4_amd64.deb")
sha256sums=('fcf3d6f056a470358fde21cb5d695e20736d6a425a6a73a5946e8a5056f2ead2')

package(){
	# Extract package data
	tar xf data.tar.xz -C "${pkgdir}"
}
