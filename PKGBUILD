# Maintainer: AlphaJack <alphajack at tuta dot io>

pkgname="teams-for-linux-bin"
pkgver=1.13.1
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
b2sums_x86_64=('a9eff9cd27ef007e74843030a8deb6bb5b97d092fd37b0266964d704d8b22463b56b075b15937d5e3596c5a13172eab1752b3253e013e91078c5021f65e7689f')
b2sums_aarch64=('71468e3722e1c0469a9cebe989199dc63c05491f5ff6a93c4ae677439c7e570c41f2062266b70d0470605fef7a1611f08b559c447c06d55083f09ed4ebb9f8f7')
b2sums_armv7h=('e49ac582902687f23c8ac89d29d4c31bf9e96b70733b767d843b1dff4fa66d76c3f57c6cb0261c5febcb1b45044b27444682e9f9a0964b8ac58bc8f9da56ee1b')
options=("!strip")

prepare(){
 tar -xf "data.tar.xz"
}

package(){
 cp -r "opt" "$pkgdir"
 cp -r "usr" "$pkgdir"
}
