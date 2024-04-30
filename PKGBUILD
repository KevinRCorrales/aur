# Maintainer: AlphaJack <alphajack at tuta dot io>

pkgname="teams-for-linux-bin"
pkgver=1.4.19
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
b2sums_x86_64=('aa367107df82078f4e7bcfc54b4324529869a89334f70d4c058bf53d6472457b574595bcfcf94ffe039e52eeb69ecbfac3825e4711038eed5d868c7c648e4bcf')
b2sums_aarch64=('13022edb9acdb189583bf1ef61e1a2442034c8f833c727c5e8378fb0bed33ccfda3d338b06693602909c472b28eee526279b0ac0bd1252573f9e5e902194d6b7')
b2sums_armv7h=('46ea644749f177df404cba8f02b75cdd9c2f79c6ef44ccc7345af527963068ca42f278b7702ba7c0a39804f3e00862f6389c879ae7d5ef09c3f29609c403033f')
options=("!strip")

prepare(){
 tar -xf "data.tar.xz"
}

package(){
 cp -r "opt" "$pkgdir"
 cp -r "usr" "$pkgdir"
}
