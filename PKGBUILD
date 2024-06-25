# Maintainer: AlphaJack <alphajack at tuta dot io>

pkgname="teams-for-linux-bin"
pkgver=1.7.4
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
b2sums_x86_64=('68f39e4fea122c1bc1c1ee0b94062a8c49b6d80b0732c2b0011019908af0c909325ca663ef8bd39c2c41c03c8e956bc8d54a518f194fb28a2bcfc92f66fbc154')
b2sums_aarch64=('44eb1d821d50f3f56631e9b45811c9101d1b90226539364cc3fd79f6707461af68ba79277968e0f5a19de4d644c2f23942265272c315a0b11c5d8999816303e7')
b2sums_armv7h=('429da130ea71c2785e8b737428f51374ea1dc8305dcb8acc4bef77e11a4fda8388ba5924307b2e670fd274804f4f6ef0ddda21ce923bcad8f34387d270e6574e')
options=("!strip")

prepare(){
 tar -xf "data.tar.xz"
}

package(){
 cp -r "opt" "$pkgdir"
 cp -r "usr" "$pkgdir"
}
