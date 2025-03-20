# Maintainer: AlphaJack <alphajack at tuta dot io>

pkgname="teams-for-linux-bin"
pkgver=1.12.7
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
b2sums_x86_64=('338cfa470d2f0ae91748c38e20c1b72d0b1ac8a3b8b98c11e42c8209675d8952f6a848cafe3457ee8cbd2c9473239722d114a7a13b184141d3047e01aaab12d7')
b2sums_aarch64=('883b6790b0807998ee46e3fb7a951f517ce539bc356ff606f0bffa11f632e6ddce5fbb73eba1dbf0bfc3c017bc87c8ce4a9e0216a5d9753b359670693f5a5e3c')
b2sums_armv7h=('6bcd7991fd5de4c021bbabfc08ead706d7ba9d5bb03a92b3c4a59088662148b7ac8ecda718e47094bb1bf0db0c7d2e8c6fd34efd2df3d62c6b1c5c90f38cb1c8')
options=("!strip")

prepare(){
 tar -xf "data.tar.xz"
}

package(){
 cp -r "opt" "$pkgdir"
 cp -r "usr" "$pkgdir"
}
