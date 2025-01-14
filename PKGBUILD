# Maintainer: AlphaJack <alphajack at tuta dot io>

pkgname="teams-for-linux-bin"
pkgver=1.12.5
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
b2sums_x86_64=('de071d2db8a3fa02b90028998ef6bd11e2ea5568722bb61a06105300403cffcd645892644af106f0dd5ecb07751cfa2b746dbaf923009efca4c5bcfa51c2a8e3')
b2sums_aarch64=('2873576e32a10e18ef03e3dfc120db7716b77dc3d60e67c708526116d560bd7255af5f5fe261b8adcb1eab2803990b761700a4773ddd1ba435075f574222647e')
b2sums_armv7h=('21f569f260a66d9f8b58c29c90ec68e2d984f3e283e7155aef480c5a2ad2da284c6af47128765e0853523f614ad9d80dd1e4d8c87cf0c1c7224878a3b057eb37')
options=("!strip")

prepare(){
 tar -xf "data.tar.xz"
}

package(){
 cp -r "opt" "$pkgdir"
 cp -r "usr" "$pkgdir"
}
