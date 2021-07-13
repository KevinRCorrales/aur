# Maintainer: Mark Wagie <mark dot wagie at tutanota dot com>
# Contributor: Mehmet Ozgur Bayhan <mozgurbayhan at gmail.com>
# Contributor: Thomas Quillan <tjquillan at gmail.com>
# Contributor: iboyperson <tjquillan at gmail dot com>
# Contributor: Alessandro Pazzaglia <jackdroido at gmail dot com>
pkgname=pyinstaller
pkgver=4.4
pkgrel=1
pkgdesc="Bundles a Python application and all its dependencies into a single package"
arch=('x86_64')
url="http://www.pyinstaller.org"
license=('GPL2')
depends=('python-altgraph' 'pyinstaller-hooks-contrib')
makedepends=('cmocka' 'python-setuptools')
#checkdepends=('flake8' 'python-execnet' 'python-flaky' 'python-lxml' 'python-psutil'
#              'python-pytest-rerunfailures' 'python-pytest-xdist')
#              'python-pytest-drop-dup-tests' 'python-tinyaes'
optdepends=('python-pycrypto: bytecode encryption support'
            'upx: executable compression support')
source=("https://pypi.org/packages/source/${pkgname:0:1}/$pkgname/$pkgname-$pkgver.tar.gz")
sha256sums=('af3ef0b9f265a2d3859357a25ab16743fbb6143c89fd7c3570cb84b8d24db0ba')

build() {
  cd "$pkgname-$pkgver"
  python setup.py build
}

#check() {
#  cd "$pkgname-$pkgver"
#  local python_version=$(python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')

#  # Run only the unit and functional tests, but not the huge library test-suite
#  PYTHONPATH="$PWD/build/lib.linux-$CARCH-${python_version}" \
#    pytest -k "unit and functional and not test_libraries"
#}

package() {
  cd "$pkgname-$pkgver"
  export PYTHONHASHSEED=0
  python setup.py install --root="$pkgdir/" --optimize=1 --skip-build
}
