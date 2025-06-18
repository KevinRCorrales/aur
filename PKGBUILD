# Maintainer: AlphaJack <alphajack at tuta dot io>

pkgname="teams-for-linux-bin"
pkgver=2.0.17
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
b2sums_x86_64=('1e8711191034ece5c8224573a6460ed63cbf0ba4a555161a69792113df8aae20f6624384d9301de67b40cf9323be345d4bd37a6fdd5eb1963a8d019faf7a7ffc')
b2sums_aarch64=('6f33c05832a7a3c673a3db81aaded5ced482aba6843ae61d882c1395a23970a37b5a40d62011622b62fa2fe41aa2bae89137c84f5422147a8ee06efd50d16987')
b2sums_armv7h=('7170409f9ab37f69c008ce925042b3e252b2bf78b6c590ee90a4bccda884ef96df7edebfde0024b47e97a4ce338c49352c20e7b7227e24b92a010d9e549001b9')
options=("!strip")

prepare(){
 tar -xf "data.tar.xz"
}

package(){
 cp -r "opt" "$pkgdir"
 cp -r "usr" "$pkgdir"
}
