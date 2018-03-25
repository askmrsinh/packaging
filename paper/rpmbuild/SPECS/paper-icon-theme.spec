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
%global commit0 84c87025ab8ae102139e5a55317ae8717892cf04

name:       paper-icon-theme
version:    1.4.0
release:    0.696.20160501git84c8702%{?dist}

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
* Sun Mar 25 2018 Ashesh Kumar Singh <user501254@gmail.com> 1.4.0-0.696
- 84c87025: Merge pull request #638 from besser82/enhancement/dnfdragora	(Sam Hewitt <hewittsamuel@gmail.com>)
- d6e70724: Merge pull request #634 from krouma/master	(Sam Hewitt <hewittsamuel@gmail.com>)
- 049658cd: Merge pull request #641 from tista500/master	(Sam Hewitt <hewittsamuel@gmail.com>)
- 6c4749e5: Added symlinks for Gnome-tweaks 3.27.x	(tista500 <tista.gma500@gmail.com>)
- 2eb3df9b: Add symlink for dnfdragora (Fixes #637)	(Björn Esser <besser82@fedoraproject.org>)
- 4f4cae22: Add Firefox Nightly and Firefox Developer Edition flatpak icon symlinks	(Matyáš Kroupa <kroupa.matyas@gmail.com>)
- af0296ec: Merge pull request #629 from krouma/master	(Sam Hewitt <hewittsamuel@gmail.com>)
- a133412e: Fix LibreOffice Math flatpak icon	(krouma <kroupa.matyas@gmail.com>)
- 4113e5c8: Add LibreOffice flatpak symlinks	(krouma <kroupa.matyas@gmail.com>)
- fe138eb7: Add VLC flatpak symlinks	(krouma <kroupa.matyas@gmail.com>)