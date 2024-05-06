# Maintainer: AlphaJack <alphajack at tuta dot io>

pkgname="teams-for-linux-bin"
pkgver=1.4.37
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
b2sums_x86_64=('299f98ef11e4951300e152fa3d559a331eb5936cfedf0c8552dd4b69aede1161e244b26496355928fbdd806c2c6e564068bcda1e409abb1e6f41b40604a8b37f')
b2sums_aarch64=('c4e0ad8290973fb5c15a087538645171f081fdf4eeb7f2bef7a17e3008e5a5900ef2d360ad93278a8b6d5266cecd9fbf26ca043c8cce4a7466b36ddc4a4ced23')
b2sums_armv7h=('db1ef1425f4d3c0db04abec780e33b580ab0bbfaa752924b9483332ff8e8ed92d3dff0a4fecec2b1e487df707e52f6f462b11e7753dda664cb1136d20480d69a')
options=("!strip")

prepare(){
 tar -xf "data.tar.xz"
}

package(){
 cp -r "opt" "$pkgdir"
 cp -r "usr" "$pkgdir"
}
