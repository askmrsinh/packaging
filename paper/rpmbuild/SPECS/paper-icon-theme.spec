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
%global commit0 45207e8406cf4a702cf74c81b33bb4f170f7aeef

name:       paper-icon-theme
version:    1.2.0
release:    0.340.20160501git45207e8%{?dist}

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
* Sun May 08 2016 Ashesh Kumar Singh <user501254@gmail.com> 1.2.0-0.340
- 45207e8: added less-than-satisfactory gimp icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 35ab919: refined display icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- f1b9a3d: refined symbolic icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- f8f793f: refined utilities icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- f57723e: added utilities icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 95e2220: added computer icon	(Sam Hewitt <hewittsamuel@gmail.com>)