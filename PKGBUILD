# Maintainer: AlphaJack <alphajack at tuta dot io>

pkgname="teams-for-linux-bin"
pkgver=2.1.3
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
b2sums_x86_64=('4d3982485939d49bcb4738f2a8b434013018b167c356308b2029a059223e98c23926eb45ce8e5336e08069672dfa06002723ef5c7d816721b95d52f747634089')
b2sums_aarch64=('cfc4a388f720a90977365f1e318c97ea7747511a4418ce3a74c46c4c4aade97a904845787172d1a0c27b06c2ca4f77193eea1d0acf2b0a2fe08677a1166fd13d')
b2sums_armv7h=('abbb85f20e74b7bb909fd7cda8b5e7833ad3f760186e44ab03e004581e75544b709e62e5206421ea7469c337b069ca58675a9d9e54fe4dd7515f325c05613235')
options=("!strip")

prepare(){
 tar -xf "data.tar.xz"
}

package(){
 cp -r "opt" "$pkgdir"
 cp -r "usr" "$pkgdir"
}
