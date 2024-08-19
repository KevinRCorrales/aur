# Maintainer: AlphaJack <alphajack at tuta dot io>

pkgname="teams-for-linux-bin"
pkgver=1.9.0
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
b2sums_x86_64=('d6be9c6283b4be01c735d694ceca6749fbf63539710f2cc852e1306261f89d2c88a7241e8b64dedfc5145a46471a5ccca25317d5004424877525393d7b405f34')
b2sums_aarch64=('e7f1870bf469bbc92c706589ff631f90b316bb86bc9b66f71b346ca65edb3646e7beda112bfc8efbc23c7e44410d2f4d58f02aae13487b37ec1eb9cbff595070')
b2sums_armv7h=('6721cf61a5d72f5cb75ad595a01dab291c0513a1b54b127d7f46b831da0961dd28b7944f8e4e34e71a0d527ee4a9dd5686825e529ec3550d7b6ccbbfbab3398a')
options=("!strip")

prepare(){
 tar -xf "data.tar.xz"
}

package(){
 cp -r "opt" "$pkgdir"
 cp -r "usr" "$pkgdir"
}
