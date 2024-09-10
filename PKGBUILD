# Maintainer: AlphaJack <alphajack at tuta dot io>

pkgname="teams-for-linux-bin"
pkgver=1.10.1
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
b2sums_x86_64=('e3816a293b1d38750e980e5d34b557c54c55ec80eb519590ceb41ef775bf16f2a11791089cc57f3f624b6a615dcd0db9be7ad799eb4a9c528fe7c0d3bbf27cb5')
b2sums_aarch64=('4be1331df8acab5e0fbd406ec8914905a77dde496cb2a0ddb1871acde1dec9f576688c4e0f34384a8139a04818ae2a199fd616803867b810b07c50945ff7b098')
b2sums_armv7h=('d636e2e3688710e8b70a8bb3e3304328f50e75ed149a1334b3b27db2eef1444d6ac918087601e776813d13a3c5d28eeafaad2773cc2be15445b480b5e8407ad2')
options=("!strip")

prepare(){
 tar -xf "data.tar.xz"
}

package(){
 cp -r "opt" "$pkgdir"
 cp -r "usr" "$pkgdir"
}
