# Maintainer: AlphaJack <alphajack at tuta dot io>

pkgname="teams-for-linux-bin"
pkgver=1.4.18
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
b2sums_x86_64=('b45afd5cc6173e960c78a48ba4d1d056c305941f610990a3fceb1582fd63c621a86d293a8aee78808cdbc75d368af8be3995466c2308dc0f77bd2ae11579dfda')
b2sums_aarch64=('1a60b0fefe44061362a11c6476af0de2aa92b8a75be622a4d1e9b49a745bce2e5e4ec41957f614c06f4a7b91248447e96f4cb2a18a4cbcdc3ec9e522e8612cf2')
b2sums_armv7h=('ac60d966817075a82031176049affd493c17c5a1e7cb4f7ea446c98d3c951e13267e02edbf99be43b427dce2a1345877c959f04ae699c74b5c031a0e3879ff83')
options=("!strip")

prepare(){
 tar -xf "data.tar.xz"
}

package(){
 cp -r "opt" "$pkgdir"
 cp -r "usr" "$pkgdir"
}
