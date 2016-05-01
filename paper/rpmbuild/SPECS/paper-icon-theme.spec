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
%global commit0 60293772a8688d12c8f530725f6009136510bc13

name:       paper-icon-theme
version:    1.2.0
release:    0.323.20160501git6029377%{?dist}

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
* Sun May 01 2016 Ashesh Kumar Singh <user501254@gmail.com> 1.2.0-0.323
- 6029377: completed science icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 6b8ae76: completed games icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- ae775f3: added a few preferences icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 0af8b91: preferences symlinks	(Sam Hewitt <hewittsamuel@gmail.com>)
- cc64e46: haskell mime; links	(Sam Hewitt <hewittsamuel@gmail.com>)
- fe89098: dark video mime; audio symlinks	(Sam Hewitt <hewittsamuel@gmail.com>)
- dca4300: added video mime symlinks	(Sam Hewitt <hewittsamuel@gmail.com>)
- 1b04388: added some mime links	(Sam Hewitt <hewittsamuel@gmail.com>)
- 5b37801: added coloured KDE folders	(Sam Hewitt <hewittsamuel@gmail.com>)
- 989c0e1: added pycharm and meld icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 2a667a3: added mixxx icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 96a530e: added birdie icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- bf4afbc: added vector status icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- f31589b: added doublecmd icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 8c713ce: added old firefox icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 05c6ddc: completed nylas icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 7aa70f6: added quassel icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- d539a54: added some mimetypes	(Sam Hewitt <hewittsamuel@gmail.com>)
- 2141e2b: added qt app icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- ca131bd: added skype icon	(Sam Hewitt <hewittsamuel@gmail.com>)