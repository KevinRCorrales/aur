# Maintainer: AlphaJack <alphajack at tuta dot io>

pkgname="teams-for-linux-bin"
pkgver=2.0.13
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
b2sums_x86_64=('262b1d9fd37dfbe80cb8f7e79bf62ae12965452ae9286cb041bcf8a00b4b27bcf0009d16db39740b3bbde9bff5034502fd8430872bfd9c6df65bf648adbc9fc0')
b2sums_aarch64=('e8845e146f6705975d03137d2109d6f11cf4de3e1aebbc631a32a1114ac91ef3a669378ca247226f71259b7f200a0621c30b4883db0eb52e973af4da6c35818c')
b2sums_armv7h=('b987ceff648c0743f6868a9daa0ef35f7aa7226d5dce04675339f31484398f5adef3e2a6a9fa45b8f51fc3059dfb4ceb3fa43211603ae24e148e96ca833a2f54')
options=("!strip")

prepare(){
 tar -xf "data.tar.xz"
}

package(){
 cp -r "opt" "$pkgdir"
 cp -r "usr" "$pkgdir"
}
