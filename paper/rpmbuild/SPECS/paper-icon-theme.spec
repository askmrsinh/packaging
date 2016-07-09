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
%global commit0 dca2ec16130aa39ef23c40e2e775e7b5ee691883

name:       paper-icon-theme
version:    1.3.0
release:    0.565.20160501gitdca2ec1%{?dist}

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
* Sun Jul 10 2016 Ashesh Kumar Singh <user501254@gmail.com> 1.3.0-0.565
- dca2ec1: new desktop file for installing updating	(Sam Hewitt <hewittsamuel@gmail.com>)
- ebc3ff2: added visual studio symlink	(Sam Hewitt <hewittsamuel@gmail.com>)
- f947c66: Merge branch 'master' of github.com:snwh/paper-icon-theme	(Sam Hewitt <hewittsamuel@gmail.com>)
- 6f23124: fixed text-rust	(Sam Hewitt <hewittsamuel@gmail.com>)