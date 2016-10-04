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
%global commit0 54fa6058d7f6ec964a88a6558cb99fec15df2389

name:       paper-icon-theme
version:    1.3.0
release:    0.619.20160501git54fa605%{?dist}

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
* Wed Oct 05 2016 Ashesh Kumar Singh <user501254@gmail.com> 1.3.0-0.619
- 54fa605: updated index	(Sam Hewitt <hewittsamuel@gmail.com>)
- 6811d60: removed non-existent 22px references in index	(Sam Hewitt <hewittsamuel@gmail.com>)
- 36a8d65: unified render script	(Sam Hewitt <hewittsamuel@gmail.com>)
- b5068ce: update readme	(Sam Hewitt <hewittsamuel@gmail.com>)
- a5f15a9: update readme	(Sam Hewitt <hewittsamuel@gmail.com>)
- 72b45f8: update docs	(Sam Hewitt <hewittsamuel@gmail.com>)
- 5603ca3: added some symlinks	(Sam Hewitt <hewittsamuel@gmail.com>)
- 593ddcf: added some symlinks	(Sam Hewitt <hewittsamuel@gmail.com>)
- f77cd67: added some mint symlinks	(Sam Hewitt <hewittsamuel@gmail.com>)
- d1f1abf: added some mint symlinks	(Sam Hewitt <hewittsamuel@gmail.com>)
- e5070ba: added folder recent	(Sam Hewitt <hewittsamuel@gmail.com>)
- f0aa38d: added preferences effects icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- c348d77: added some mint symlinks	(Sam Hewitt <hewittsamuel@gmail.com>)
- e34f353: added some more Mint-specific icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- d92a7e8: added some Mint-specific icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- ac4f9a1: added mgba icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- eb10ef8: added shutter icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- aa63086: added five-or-more icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- b2f513a: added scribus icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- c3e131e: added recent icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 609a7b3: added dota 2 icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 911b729: added linssid icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 9006e5a: added facebook messenger icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 0fa7de1: updated folder icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 59dac5a: fixed 16px place icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 3fe8b85: added variety icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 37e9a3e: added symlinks	(Sam Hewitt <hewittsamuel@gmail.com>)
- 46ae233: updated 16px place icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 6922144: added lastfm icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- c361230: added stellarium icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 842811d: added celestia icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 4a5c1dc: added cantata icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 8521b27: added mendeleydesktop icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- c92cfec: added devede symlink	(Sam Hewitt <hewittsamuel@gmail.com>)
- 63c1d0f: fixed panel icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- b0fe58b: fixed battery icon mistake	(Sam Hewitt <hewittsamuel@gmail.com>)
- 9335117: fixed misnamed icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 856612c: fixed 48px muted icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 35fc1a0: added symlinks	(Sam Hewitt <hewittsamuel@gmail.com>)