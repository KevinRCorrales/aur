# Maintainer: AlphaJack <alphajack at tuta dot io>

pkgname="teams-for-linux-bin"
pkgver=1.4.31
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
b2sums_x86_64=('5fd9fbdfc15f0dd5fcd09cc04d09ceebff7bf244b4515b8416d016d47f6967e1aeb1b8b44aa03b00398f7fa2927c9220081a934a72f1bb411175119381107fb8')
b2sums_aarch64=('df84c7367b587130b89a0812dbeaae9316075d0d5ef6e147a7cdba9db016a3c449bd10fd1407f17eb877e921d50ad124724702241c0966770607c63b01fe30a0')
b2sums_armv7h=('61bc90d73d0eddd1e3a8a1dc0351ae89d1cb04b844ea491b1c8ed996c0cfd7ab74bd62a7ce538c40ce8dfcc61b6268234f5a0e01b4882eca80f444ba8218681d')
options=("!strip")

prepare(){
 tar -xf "data.tar.xz"
}

package(){
 cp -r "opt" "$pkgdir"
 cp -r "usr" "$pkgdir"
}
