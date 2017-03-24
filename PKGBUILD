# Maintainer: XavierCLL <xavier.corredor.llano (a) gmail.com>

pkgname=pycharm-professional
pkgver=2017.1.0
_pkgver=2017.1
pkgrel=1
pkgdesc="Powerful Python and Django IDE. Professional edition."
arch=('any')
options=('!strip')
url="http://www.jetbrains.com/pycharm/"
conflicts=('pycharm' 'pycharm-community')
provides=('pycharm')
license=('custom')
install=${pkgname}.install
# for no-jdk:
# depends=('java-runtime-common' 'java-runtime>=8' 'ttf-font' 'libxtst' 'libxslt')
depends=('giflib' 'ttf-font' 'libxtst' 'libxslt')
makedepends=('python2-setuptools' 'python-setuptools')
# for no-jdk:
# source=(https://download.jetbrains.com/python/$pkgname-$_pkgver-no-jdk.tar.gz
source=(https://download.jetbrains.com/python/$pkgname-$_pkgver.tar.gz
        'pycharm-professional.desktop'
        'pycharm-professional.install'
        'pycharm'
        'charm.desktop'
        'charm')
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
            'vagrant: For support virtualized development environments'
            'python2-pytest: For support testing inside Pycharm with Python 2'
            'python-pytest: For support testing inside Pycharm with Python 3'
            'python2-tox: Python environments for testing tool with Python 2'
            'python-tox: Python environments for testing tool with Python 3', 
            'jupyter: For support Jupyter Notebook')
# for no-jdk:
# sha256sums=('42be162851c00869f2d920d7d4b759664614ad475f500d158fcc252a595544d2'
sha256sums=('6e5223fa4b50e459ad6b03d33b6184ec59791aedd97048f50588602ded6071e7'
            '016db1860a8b36d408c827f90aeb04b9d55cf21ea36788a9d8510cc54fae1c49'
            'c1a74303d9e870918bd8068f761c8251b996694b1b96b3537fbca317679c4958'
            '43e79e5a786fc76385634dc0a9f1c3489b25031745b840b0822b059fc91d1060'
            'e1cf2a280d90a55710131bdf33f4026a427d10131ddd5c776a936ee1ecf5a6fb'
            '0a753ef612fa689465aceb2e8279591bca9b8ffd02ee16da0b69d32388d81303')

package() {
  # compile PyDev debugger used by PyCharm to speedup debugging
  python2 $srcdir/pycharm-$_pkgver/helpers/pydev/setup_cython.py build_ext --inplace
  python3 $srcdir/pycharm-$_pkgver/helpers/pydev/setup_cython.py build_ext --inplace
  
  # base
  cd $srcdir
  install -dm 755 $pkgdir/opt/$pkgname
  cp -dr --no-preserve=ownership $srcdir/pycharm-$_pkgver/* $pkgdir/opt/$pkgname
  install -dm 755 $pkgdir/usr/share/{applications,pixmaps}
  install -dm 755 $pkgdir/usr/bin/
  install -Dm 644 $pkgdir/opt/$pkgname/bin/pycharm.png $pkgdir/usr/share/pixmaps/pycharm.png
  
  # licenses
  install -dm 755 $pkgdir/usr/share/licenses/$pkgname/
  cp -dr --no-preserve=ownership $srcdir/pycharm-$_pkgver/license/* $pkgdir/usr/share/licenses/$pkgname
  
  # exec
  install -Dm 755 pycharm $pkgdir/usr/bin/
  
  # app file desktop
  install -Dm 644 pycharm-professional.desktop $pkgdir/usr/share/applications/
  
  # install charm application - for edit a single file in Pycharm
  install -Dm 755 charm $pkgdir/opt/pycharm-professional/bin/
  install -Dm 644 charm.desktop $pkgdir/usr/share/applications/
  
  # delete some conflicts files for i686 
  if [[ $CARCH = 'i686' ]]; then
    rm -f $pkgdir/opt/$pkgname/bin/libyjpagent-linux64.so
    rm -f $pkgdir/opt/$pkgname/bin/fsnotifier64
  fi
  
}
