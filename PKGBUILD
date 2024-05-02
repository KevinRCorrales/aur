# Maintainer: AlphaJack <alphajack at tuta dot io>

pkgname="teams-for-linux-bin"
pkgver=1.4.34
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
b2sums_x86_64=('4772c30527bf7bdb535db098caecfbdbdce04dadd707c7b805331b6ebf48ad00ef34871283d8cb55925e3eb1c419e7db795ddb6f5334c3c20ff9f97b4d171b9a')
b2sums_aarch64=('a64f1a268c24c163906f293772ace3df4ac21865c2b1003b0f0a8c3075e84f98face0ad2e3aa4f13ccf32bd6cf9d6a8458c42d2db06ba6ad536329e8bf877dd7')
b2sums_armv7h=('72f348992fef30bbb652058308016524879347ab310224823434de2671bcc3261057c1e8b8cecd470652685ca17053ee6e3a770ed599bbfaea06ea449a964b81')
options=("!strip")

prepare(){
 tar -xf "data.tar.xz"
}

package(){
 cp -r "opt" "$pkgdir"
 cp -r "usr" "$pkgdir"
}
