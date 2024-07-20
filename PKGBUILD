# Maintainer: AlphaJack <alphajack at tuta dot io>

pkgname="teams-for-linux-bin"
pkgver=1.8.1
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
b2sums_x86_64=('f7ba2e68d124e3ef9d86c81c0028e2aa54d3c8d683f55190069733009b28dd651ec9d3c3968baab9feb34b979b51d3f61ba371444646d10e1448bc8a34e0cc22')
b2sums_aarch64=('6a563e632124ba0442387c8bfa904a2f535c2e365926e54235736658a090cf12c92cc14634ad0605c9c051f3a9c984ab81242a989da8060a71e7b74f3c87d8f4')
b2sums_armv7h=('425bca2772a65e262b588d87d3f54324a47b1ab06513f486961c767692e087118f29c6dc076b8211b5ed0ad62b958c16f3c6fbcb7625207399ebb0b6313484b3')
options=("!strip")

prepare(){
 tar -xf "data.tar.xz"
}

package(){
 cp -r "opt" "$pkgdir"
 cp -r "usr" "$pkgdir"
}
