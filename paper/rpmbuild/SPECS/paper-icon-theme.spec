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
%global commit0 3f01b6bcce57a4f7e92e4a5b411621af28bde95e

name:       paper-icon-theme
version:    1.3.0
release:    0.347.20160501git3f01b6b%{?dist}

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
* Wed May 11 2016 Ashesh Kumar Singh <user501254@gmail.com> 1.3.0-0.347
- 3f01b6b: version 1.3	(Sam Hewitt <hewittsamuel@gmail.com>)
- 326dcc0: more icon colour updates	(Sam Hewitt <hewittsamuel@gmail.com>)
- 178a539: reorganized colour palette	(Sam Hewitt <hewittsamuel@gmail.com>)
- 9c05185: more colour updates	(Sam Hewitt <hewittsamuel@gmail.com>)
- 0b35ee5: updating more colours	(Sam Hewitt <hewittsamuel@gmail.com>)
- c640f57: update readme	(Sam Hewitt <hewittsamuel@gmail.com>)
- ee908c4: colour palette update	(Sam Hewitt <hewittsamuel@gmail.com>)