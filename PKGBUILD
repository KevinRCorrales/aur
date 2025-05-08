# Maintainer: AlphaJack <alphajack at tuta dot io>

pkgname="teams-for-linux-bin"
pkgver=2.0.12
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
b2sums_x86_64=('6afe5c92a32183a085376b37192e29e0ef42620258e0f96a7395c4e711d284cf57e427115a4db9ba6b7100e98444eddf377cc63b6fc7c82e7e1bc79e57f9e944')
b2sums_aarch64=('3fa2d33f3636df181419ac550089b286aaa3122696314fffbb1902b9df43f19aafb00edbdebba195fca406a3c005a8e3dc4ccb7c302c11f9fb6784243241699b')
b2sums_armv7h=('b2b4f5cbbf0eda3cf53552a4cd8eea392aa2751bf492524c908e23b347830cda507618e0706cad504baebf71ce807c78777b6e147663b9c40c6030e8ef58ac6d')
options=("!strip")

prepare(){
 tar -xf "data.tar.xz"
}

package(){
 cp -r "opt" "$pkgdir"
 cp -r "usr" "$pkgdir"
}
