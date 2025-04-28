# Maintainer: AlphaJack <alphajack at tuta dot io>

pkgname="teams-for-linux-bin"
pkgver=2.0.11
pkgrel=1
pkgdesc="Unofficial Microsoft Teams for Linux client (binary version)"
url="https://github.com/IsmaelMartinez/teams-for-linux"
license=("GPL3")
arch=("x86_64" "aarch64" "armv7h")
provides=("teams-for-linux")
conflicts=("teams-for-linux"
           "teams-for-linux-appimage"
           "teams-for-linux-git"
           "teams-for-linux-wbundled-electron"
          )
depends=("gtk3" "libxss" "nss")
source_x86_64=("$url/releases/download/v$pkgver/teams-for-linux_${pkgver}_amd64.deb")
source_aarch64=("$url/releases/download/v$pkgver/teams-for-linux_${pkgver}_arm64.deb")
source_armv7h=("$url/releases/download/v$pkgver/teams-for-linux_${pkgver}_armv7l.deb")
b2sums_x86_64=('42d815d0fbabb71eb301b665e7ede725d07b6b637846b1a7758e54a2731ce7472598f65aae0a25fb90709225c399c4c5710a1fe795b12e8cf786933d5ba7fa34')
b2sums_aarch64=('771ed3c37ca9a5632bbcc6c0ed5f009f52a4b941e20840eb233c6430826cdf7bd5af2401721300604c2f01d35331c432a54ea5e6809fb8ad782dce72c1a25dfd')
b2sums_armv7h=('1b85573a74b0874ba99b313aa6702631c5b94471907651a3f2bf7535a4f2c070727ba296a7932db1e663614c31abbff0e5ec35b6f1daea9290ea5fb20c391af1')
options=("!strip")

prepare(){
 tar -xf "data.tar.xz"
}

package(){
 cp -r "opt" "$pkgdir"
 cp -r "usr" "$pkgdir"
}
