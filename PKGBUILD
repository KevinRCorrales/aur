# Maintainer: AlphaJack <alphajack at tuta dot io>

pkgname="teams-for-linux-bin"
pkgver=2.0.8
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
b2sums_x86_64=('1b3a1bdd1bf430c3d9d34859c29956d9b697d9d85fa380fdfc22395ae93f5d682ee8bce71872fdaa5aefce8fe76820302bafb3c1e240e8514eea412712fde880')
b2sums_aarch64=('857c1ee3ee5b35e2b564b4492c9067c94473e5794f9fc80e73604d83b9d67744bb8cc956ff72a8871a9cdbede05dc982003eb32cfe7740517c59600874edbbee')
b2sums_armv7h=('6a6120f20d6348a089deffb37b29b2b294d530d3ea52857bbb1ea3c841cc26999e507a365470027377f087274e131a73c7e9a316f649c2825719a6b39e31db6e')
options=("!strip")

prepare(){
 tar -xf "data.tar.xz"
}

package(){
 cp -r "opt" "$pkgdir"
 cp -r "usr" "$pkgdir"
}
