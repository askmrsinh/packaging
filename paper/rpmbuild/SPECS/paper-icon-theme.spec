# Spec file for package paper-icon-theme
#
# Copyright (c) 2015 Sam Hewitt <sam@snwh.org>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#


# GitHub Stuff
%global commit0 6aa0a2c8d802199d0a9f71579f136bd6476d5d8e

name:       paper-icon-theme
version:    1.3.0
release:    0.560.20160501git6aa0a2c%{?dist}

Summary:    Paper Icon theme
Group:      System/GUI/Other
License:    CC-BY-SA-4.0
Url:        http://snwh.org/paper/icons
Source0:    https://github.com/snwh/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{commit0}.tar.gz
Requires:   hicolor-icon-theme, gnome-icon-theme
BuildArch:  noarch


%description
Paper Icon Theme

%prep
%setup -qn %{name}-%{commit0}

# Delete dead icon symlinks
find -L . -type l -delete

%build

%install
install -dpm 0755 $RPM_BUILD_ROOT%{_datadir}/icons/
cp -a Paper/ $RPM_BUILD_ROOT%{_datadir}/icons/

%files
%doc AUTHORS COPYING
%{_datadir}/icons/Paper/

%changelog
* Fri Jun 10 2016 Ashesh Kumar Singh <user501254@gmail.com> 1.3.0-0.560
- 6aa0a2c: added R mimetypes	(Sam Hewitt <hewittsamuel@gmail.com>)
- 0c3f5ae: added a few icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 9eb1ecc: tweaked send-recieve icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- b4f4c10: mail icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- b9af83c: added zoom icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- f1676b4: repeat song icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 554b6d2: added repeat icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- f2f4335: severe weather and mute icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- ab7aadc: weather few clouds	(Sam Hewitt <hewittsamuel@gmail.com>)
- 73d64a1: updated gnome-weather icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- a3301ac: refined a few icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 5da942f: added help-contents	(Sam Hewitt <hewittsamuel@gmail.com>)
- ec146b0: added go arrows	(Sam Hewitt <hewittsamuel@gmail.com>)
- 73f2b01: updated mail-signed icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- e246ecc: added signed mail icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 04a289f: added mail icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 6611f55: added appointment icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- d5bfe0e: updated weather icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 0e9c561: added network status icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 9a4a0c2: updated some icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 1ecc653: added print and help icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 1316bad: added media-tape icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 3e70f43: added sync icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- daa8cc6: added emblem-favorite	(Sam Hewitt <hewittsamuel@gmail.com>)
- 5c52cf0: update icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 34ab313: added more emblems	(Sam Hewitt <hewittsamuel@gmail.com>)
- 345282f: added emblem-synchronizing	(Sam Hewitt <hewittsamuel@gmail.com>)
- 7e80424: tweaked emblem icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 6a13c73: added audio-card icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- d987240: added some emblem icons and symlinks	(Sam Hewitt <hewittsamuel@gmail.com>)
- df04f8f: Merge pull request #252 from bil-elmoussaoui/master	(Sam Hewitt <hewittsamuel@gmail.com>)
- 0897d70: added font-x-generic; tweaked document mimes	(Sam Hewitt <hewittsamuel@gmail.com>)
- 81b2517: added screensaver icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- e7b0583: added preferences-desktop-multimedia	(Sam Hewitt <hewittsamuel@gmail.com>)
- d85429a: something-for-reddit symlink	(Bilal Elmoussaoui <bil.elmoussaoui@gmail.com>)
- ca1e213: Update README.md	(Sam Hewitt <hewittsamuel@gmail.com>)
- d3f2ca4: added smile emotes	(Sam Hewitt <hewittsamuel@gmail.com>)
- 2356ceb: added template mime	(Sam Hewitt <hewittsamuel@gmail.com>)
- dbb1be8: added addressbook mime	(Sam Hewitt <hewittsamuel@gmail.com>)
- 84a28e0: added symlinks	(Sam Hewitt <hewittsamuel@gmail.com>)
- 131b47a: added battery symlinks	(Sam Hewitt <hewittsamuel@gmail.com>)
- f10e1b1: added battery and volume icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 49375fb: changed the context of some icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 40cac90: updated a few cions	(Sam Hewitt <hewittsamuel@gmail.com>)
- 95c3a79: added icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 71e9a23: blam symlink	(Sam Hewitt <hewittsamuel@gmail.com>)
- 9663587: added r icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- f804caf: added dbeaver icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- cb262c0: added seafile icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- df09c4a: fixed name error	(Sam Hewitt <hewittsamuel@gmail.com>)
- 8bd62f0: added icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- f8668d5: added homebank icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- e456a0d: added authy icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 35d7152: tweaked office icon again	(Sam Hewitt <hewittsamuel@gmail.com>)
- 57a2e12: tweaked office icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 20f4030: added office and accessories icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 47110d6: adjusted plex icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- e8187bd: adjusted plex icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- faaed76: Merge pull request #215 from poltertec/master	(Sam Hewitt <hewittsamuel@gmail.com>)
- 0634652: Added plex png icons	(Peter Cornelis <poltertec@gmail.com>)
- ddb8806: added source for Plex chrome app	(Peter Cornelis <poltertec@gmail.com>)
- 4e7a3b9: added some links for Solus Software Center	(Peter Cornelis <poltertec@gmail.com>)
- f221537: added system lock screen	(Sam Hewitt <hewittsamuel@gmail.com>)
- 9dd75d8: updated session control icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- f594725: updated session control icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 8e06c2f: added web-gitter	(Sam Hewitt <hewittsamuel@gmail.com>)
- 98bf758: added soundconverter icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 289c12d: added transmageddon icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 8e08688: refined a few icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- a636abb: adjusted audio mime	(Sam Hewitt <hewittsamuel@gmail.com>)
- c817e93: updated slack icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- d4918f7: adjusted folder icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 7cf7ec5: v1.3.2	(Sam Hewitt <hewittsamuel@gmail.com>)
- 7bf5a5f: updated a few symbolic icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- c32a1c8: updated a few symbolic icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- f2a34ca: updated calendar icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 954e3c1: updated video player icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 08fd14a: updated mimetypes	(Sam Hewitt <hewittsamuel@gmail.com>)
- e6bff73: added synergy and cmake icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 4ce07fa: Update README.md	(Sam Hewitt <hewittsamuel@gmail.com>)
- 45bf780: added steam icon links	(Sam Hewitt <hewittsamuel@gmail.com>)
- a99d4ab: extended a few icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 04b91fc: adjusted list icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- d7ba304: propegated list icon changes	(Sam Hewitt <hewittsamuel@gmail.com>)
- 025e8bf: Merge pull request #191 from ArtyomZorin/master	(Sam Hewitt <hewittsamuel@gmail.com>)
- 32d6c63: Changed the list compact icon	(Artyom Zorin <azorin@zoringroup.com>)
- 4e5c838: Changed the list icon	(Artyom Zorin <azorin@zoringroup.com>)
- a0e1e78: Changed the list icons	(Artyom Zorin <azorin@zoringroup.com>)
- 44fd940: reorg symbolic plate	(Sam Hewitt <hewittsamuel@gmail.com>)
- b863670: refined symbolic icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- f6609dc: refined symbolic icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- a35642f: refined a few more symbolic icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 50b1abf: updated symbolic icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- bb5c76c: added firmware icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- c939dbc: updated exe icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 94fae9c: updated a few icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 6f5fd88: added symlinks	(Sam Hewitt <hewittsamuel@gmail.com>)
- d399565: updated some icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- dfa7862: added status icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 7289c69: added server links	(Sam Hewitt <hewittsamuel@gmail.com>)
- a09abee: better network server icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 69b340d: added notification icons; fixed broken symlinks	(Sam Hewitt <hewittsamuel@gmail.com>)
- d388bdf: reverted battery icon style	(Sam Hewitt <hewittsamuel@gmail.com>)
- 5cab14d: added icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- a12f7ec: added some linked icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- c462865: renamed symbolic to scalabel	(Sam Hewitt <hewittsamuel@gmail.com>)
- 9c8253c: added a bunch of symlinks	(Sam Hewitt <hewittsamuel@gmail.com>)
- 7024bd9: added a few icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 41bb33d: added dosbox icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- bcefb9c: added image adjust icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 88f76af: added flash icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- f16233c: added symlinks	(Sam Hewitt <hewittsamuel@gmail.com>)
- 78a139a: added vmware player icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 58bc060: added more panel icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- a2e376c: added skype icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- e5314af: added typecatcher icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 0f2c2d7: added symlinks	(Sam Hewitt <hewittsamuel@gmail.com>)
- 2dfb653: added uget icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 78e8896: added discord icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 8951342: added folder-dropbox	(Sam Hewitt <hewittsamuel@gmail.com>)
- d2c76f8: updated some icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 113988c: added korora icon	(Sam Hewitt <hewittsamuel@gmail.com>)