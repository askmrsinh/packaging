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
%global commit0 3060559509ce7fb7be4a18e3253e355da2b7ca8d

name:       paper-icon-theme
version:    1.3.0
release:    0.393.20160501git3060559%{?dist}

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
* Tue May 17 2016 Ashesh Kumar Singh <user501254@gmail.com> 1.3.0-0.393
- 3060559: added visual code studio icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- ebb26df: adjusted vector icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 2a913e4: added alternate terminal icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 76d015b: added 2048 icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- c46bb54: updated src readme	(Sam Hewitt <hewittsamuel@gmail.com>)
- 567a46c: added uget tray icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 9a879a9: added geany icon	(Sam Hewitt <hewittsamuel@gmail.com>)