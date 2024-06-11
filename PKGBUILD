# Maintainer:
# Contributor: Figue <ffigue at gmail dot com>

## useful links
# https://icecatbrowser.org/
# https://www.gnu.org/software/gnuzilla/
# https://git.savannah.gnu.org/cgit/gnuzilla.git
# https://software.classictetris.net/icecat/

## options
: ${_install_path:=opt}

## basic info
_pkgname="icecat"
pkgname="$_pkgname-bin"
pkgver=115.12.0
pkgrel=1
pkgdesc="GNU version of the Firefox ESR browser"
url="https://icecatbrowser.org"
license=('MPL-2.0')
arch=('x86_64')

provides=("icecat=$pkgver")
conflicts=('icecat')

options=('!strip' '!debug')

_dl_url="https://icecatbrowser.org/assets/icecat/$pkgver"
_dl_file="icecat-$pkgver.en-US.linux-$CARCH.tar.bz2"

noextract=("$_dl_file")

source=("$_dl_url/$_dl_file")
sha256sums=('a32808694358ec2bf52ecabb3dc867f4e22d1dfe924c55d5049c9dfa4b030c89')

package() {
  depends=(
    'dbus-glib'
    'alsa-lib'
    'gtk3'

    ## implicit
    #at-spi2-core
    #cairo
    #dbus
    #fontconfig
    #freetype2
    #gdk-pixbuf2
    #glib2
    #harfbuzz
    #libx11
    #libxcb
    #libxcomposite
    #libxcursor
    #libxdamage
    #libxext
    #libxfixes
    #libxi
    #libxrandr
    #libxrender
    #libxtst
    #pango
    #zlib
  )

  # app
  install -dm755 "$pkgdir/$_install_path"
  bsdtar -C "$pkgdir/$_install_path" -xf "$srcdir/$_dl_file"

  # duplicate binary
  ln -sf "$_pkgname" "$pkgdir/$_install_path/$_pkgname/$_pkgname-bin"

  # symlink
  install -dm755 "$pkgdir/usr/bin"
  ln -sf "/$_install_path/$_pkgname/$_pkgname" "$pkgdir/usr/bin/$_pkgname"

  # icon
  install -Dm644 "$pkgdir/$_install_path/$_pkgname/browser/chrome/icons/default/default128.png" "$pkgdir/usr/share/pixmaps/$_pkgname.png"

  # desktop file
  install -Dm644 /dev/stdin "$pkgdir/usr/share/applications/$_pkgname.desktop" << END
[Desktop Entry]
Version=1.0
Name=IceCat
GenericName=Web Browser
Comment=Browse the World Wide Web
Keywords=Internet;WWW;Browser;Web;Explorer
Exec=icecat %u
Icon=icecat
Terminal=false
X-MultipleArgs=false
Type=Application
MimeType=text/html;text/xml;application/xhtml+xml;x-scheme-handler/http;x-scheme-handler/https;application/x-xpinstall;
StartupNotify=true
StartupWMClass=icecat
Categories=Network;WebBrowser;
Actions=new-window;new-private-window;safe-mode;

[Desktop Action new-window]
Name=New Window
Exec=icecat --new-window %u

[Desktop Action new-private-window]
Name=New Private Window
Exec=icecat --private-window %u

[Desktop Action safe-mode]
Name=Safe Mode
Exec=icecat -safe-mode %u
END

  # disable auto-updates
  local _policies_json="$pkgdir/$_install_path/$_pkgname/distribution/policies.json"
  install -Dm644 /dev/stdin "$_policies_json" << END
{
  "policies": {
    "DisableAppUpdate": true
  }
}
END

  # custom defaults
  local vendorjs="$pkgdir/$_install_path/$_pkgname/browser/defaults/preferences/vendor.js"
  install -Dm644 /dev/stdin "$vendorjs" << END
// Use LANG environment variable to choose locale
pref("intl.locale.requested", "");

// Use system-provided dictionaries
pref("spellchecker.dictionary_path", "/usr/share/hunspell");

// Disable default browser checking.
pref("browser.shell.checkDefaultBrowser", false);

// Don't disable extensions in the application directory
pref("extensions.autoDisableScopes", 11);

// Enable JPEG XL images
pref("image.jxl.enabled", true);

// Prevent about:config warning
pref("browser.aboutConfig.showWarning", false);

// Prevent telemetry notification
pref("services.settings.main.search-telemetry-v2.last_check", $(date +%s));
END

  # fix permissions
  chmod -R u+rwX,go+rX,go-w "$pkgdir/"
}
