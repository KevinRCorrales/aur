# Maintainer: AlphaJack <alphajack at tuta dot io>

pkgname="teams-for-linux-bin"
pkgver=1.12.3
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
b2sums_x86_64=('1e983724c671ea8f2ce584888ab7145a981be2fde87a18ed15d8879f7843c842381dd71915652354b86e7c826cf272fd7de883dc643d028c876939255b7b98b2')
b2sums_aarch64=('4cc659c9981cb769d1ab47eb1e0b762780e10b809d144657a965ad1a7cbd429a81c281500994d90ba6d44d72ce46d39f23609a003e2d83ccad38f39b98d3abe6')
b2sums_armv7h=('064c7154504be980d151acf10bdd65e68492c7eeb14c510842e8dc48aff7a3597905451177deb34d4db342bf3db0dc5cac93d95ddd69abf7ae976acd5e7e31bd')
options=("!strip")

prepare(){
 tar -xf "data.tar.xz"
}

package(){
 cp -r "opt" "$pkgdir"
 cp -r "usr" "$pkgdir"
}
