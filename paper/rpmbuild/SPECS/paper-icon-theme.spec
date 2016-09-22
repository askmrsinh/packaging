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
%global commit0 95a53798385fa344238c27f7f4e504609501b607

name:       paper-icon-theme
version:    1.3.0
release:    0.580.20160501git95a5379%{?dist}

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
* Fri Sep 23 2016 Ashesh Kumar Singh <user501254@gmail.com> 1.3.0-0.580
- 95a5379: added lockscreen icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 32fedb4: updated docs	(Sam Hewitt <hewittsamuel@gmail.com>)
- bbb30a7: update readme	(Sam Hewitt <hewittsamuel@gmail.com>)
- df0c0fe: added gitter to readme	(Sam Hewitt <hewittsamuel@gmail.com>)
- 74a6a50: added links	(Sam Hewitt <hewittsamuel@gmail.com>)
- 28d2401: added some missing panel icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- ae811ce: added a bunch of symlinks	(Sam Hewitt <hewittsamuel@gmail.com>)
- cf1eb04: added totem symlink	(Sam Hewitt <hewittsamuel@gmail.com>)
- ea71366: added bitcoin icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 97f8e8f: added anki icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 3dfc927: added symlinks	(Sam Hewitt <hewittsamuel@gmail.com>)