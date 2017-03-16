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
%global commit0 19bf8d6b029b83e6fd451a6d76639d7d917545b9

name:       paper-icon-theme
version:    1.4.0
release:    0.678.20160501git19bf8d6%{?dist}

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
* Thu Mar 16 2017 Ashesh Kumar Singh <user501254@gmail.com> 1.4.0-0.678
- 19bf8d6: Merge pull request #517 from LaurentTreguier/master	(Sam Hewitt <hewittsamuel@gmail.com>)
- 408f627: Merge pull request #526 from gabrielelucci/master	(Sam Hewitt <hewittsamuel@gmail.com>)
- 4631856: fix README.md	(Gabriele Lucci <gabrielelucci.0@gmail.com>)
- bcb6949: add symbolic links for Tilix (f.k.a. Terminix)	(Gabriele Lucci <gabrielelucci.0@gmail.com>)
- cb8a2e3: Remove useless Ghetto Skype symlink	(LaurentTreguier <laurent@treguier.org>)