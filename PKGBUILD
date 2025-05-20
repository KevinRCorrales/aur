# Maintainer: AlphaJack <alphajack at tuta dot io>

pkgname="teams-for-linux-bin"
pkgver=2.0.14
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
b2sums_x86_64=('76496ad2239f54889d61b0afab1ece1b7fd4efa4fc72101d50f86b309baf586f97e377c622275f14d85dfc47cd3b22dbbb0e9e098bde3d89bb2a0224c5e16d09')
b2sums_aarch64=('1ed2b260026b67cd3cb48ee682b16ac45f79cd5d457b1a896e57dce685937892e37fbb59af0d3a11128919bfceb87bae2dab18e7760233030fd185353ba029af')
b2sums_armv7h=('b5d878618d6dfd5a37c0de0db5976a516fff6d1e0a05b885e5c019e872faa7469920c71c8c996e71afbf881613f1724f04d7c2501cf95ecc2a0274fb87ca92dd')
options=("!strip")

prepare(){
 tar -xf "data.tar.xz"
}

package(){
 cp -r "opt" "$pkgdir"
 cp -r "usr" "$pkgdir"
}
