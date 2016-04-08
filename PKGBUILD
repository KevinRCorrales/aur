# Maintainer: XavierCLL <xavier.corredor.llano (a) gmail.com>

pkgname=pycharm-professional
pkgver=2016.1.2
pkgrel=1
pkgdesc="Powerful Python and Django IDE. Professional version."
arch=('any')
options=('!strip')
url="http://www.jetbrains.com/pycharm/"
conflicts=('pycharm' 'pycharm-community')
provides=('pycharm')
license=('custom')
install=${pkgname}.install
depends=('java-runtime-common' 'java-runtime>=8' 'ttf-font' 'libxtst' 'libxslt')
source=(https://download.jetbrains.com/python/$pkgname-$pkgver.tar.gz
        'pycharm-professional.desktop'
        'pycharm-professional.install'
        'pycharm')
optdepends=('ipython2: For enhanced interactive Python shell v2 inside Pycharm'
            'ipython: For enhanced interactive Python shell v3 inside Pycharm'
            'openssh: For deployment and remote connections'
            'python2-setuptools: Packages manager for Python 2, for project interpreter'
            'python-setuptools: Packages manager for Python 3, for project interpreter'
            'python2-coverage: For support code coverage measurement for Python 2'
            'python-coverage: For support code coverage measurement for Python 3'
            'cython2: For performance debugger in Python 2'
            'cython: For performance debugger in Python 3'
            'docker-machine: For support docker inside Pycharm'
            'docker-compose: For support docker inside Pycharm'
            'vagrant: For support virtualized development environments')
sha256sums=('730e994f3582b1cb9754b121457636265515c19199eabd762cd78b0c504b91cf'
            '016db1860a8b36d408c827f90aeb04b9d55cf21ea36788a9d8510cc54fae1c49'
            '6442ec9f0690f743da697a2a65b0784017de501e7f39d5de0879153fbf85dc7a'
            'ad59415f8ac2c623f9c61453caf70bf75b6b14db2f09807e4ea339a2dc740be9')

package() {
  # base
  cd $srcdir
  install -dm 755 $pkgdir/opt/$pkgname
  cp -dr --no-preserve=ownership $srcdir/pycharm-$pkgver/* $pkgdir/opt/$pkgname
  install -dm 755 $pkgdir/usr/share/{applications,pixmaps}
  install -dm 755 $pkgdir/usr/bin/
  install -Dm 644 $pkgdir/opt/$pkgname/bin/pycharm.png $pkgdir/usr/share/pixmaps/pycharm.png
  
  # licenses
  install -dm 755 $pkgdir/usr/share/licenses/$pkgname/
  cp -dr --no-preserve=ownership $srcdir/pycharm-$pkgver/license/* $pkgdir/usr/share/licenses/$pkgname
  
  # exec
  install -Dm 755 pycharm $pkgdir/usr/bin/
  
  # app file desktop
  install -Dm 644 pycharm-professional.desktop $pkgdir/usr/share/applications/
  
  # delete some conflicts files for i686 
  if [[ $CARCH = 'i686' ]]; then
    rm -f $pkgdir/opt/$pkgname/bin/libyjpagent-linux64.so
    rm -f $pkgdir/opt/$pkgname/bin/fsnotifier64
  fi
  
  # delete bundled JRE inside Pycharm installation
  rm -rf $pkgdir/opt/$pkgname/jre/

  # enable anti-aliasing text in pycharm options
  if [[ $CARCH = 'i686' ]]; then
    #echo '-Dawt.useSystemAAFontSettings=on' >> $pkgdir/opt/$pkgname/bin/pycharm.vmoptions
    echo '-Dswing.aatext=true' >> $pkgdir/opt/$pkgname/bin/pycharm.vmoptions
  else
    #echo '-Dawt.useSystemAAFontSettings=on' >> $pkgdir/opt/$pkgname/bin/pycharm64.vmoptions
    echo '-Dswing.aatext=true' >> $pkgdir/opt/$pkgname/bin/pycharm64.vmoptions
  fi
  
}
