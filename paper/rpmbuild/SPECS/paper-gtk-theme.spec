# Spec file for package paper-gtk-theme
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
%global commit0 f3a5096b5bc41105e17b3228146a3be8aff850c7

name:       paper-gtk-theme
version:    2.0.0
release:    0.257.20160501gitf3a5096%{?dist}

Summary:    Paper GTK Theme
Group:      System/GUI/Other
License:    GPL-3.0+
Url:        http://snwh.org/paper/theme
Source0:    https://github.com/snwh/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{commit0}.tar.gz
Requires:   gtk2-engines
BuildArch:  noarch


%description
Paper GTK Theme

%prep
%setup -qn %{name}-%{commit0}

%build

%install
install -dpm 0755 $RPM_BUILD_ROOT%{_datadir}/themes/
cp -a Paper/ $RPM_BUILD_ROOT%{_datadir}/themes/

%files
%doc AUTHORS LICENSE
%{_datadir}/themes/Paper/

%changelog
* Wed May 25 2016 Ashesh Kumar Singh <user501254@gmail.com> 2.0.0-0.257
- f3a5096: fixed some menu bugs	(Sam Hewitt <hewittsamuel@gmail.com>)
- f3066b2: updated colors	(Sam Hewitt <hewittsamuel@gmail.com>)
- e906a43: updated colors	(Sam Hewitt <hewittsamuel@gmail.com>)
- cb3ff1e: updated selection colour	(Sam Hewitt <hewittsamuel@gmail.com>)
- 12ec99b: updated selection colour	(Sam Hewitt <hewittsamuel@gmail.com>)
- bbbf050: updated colours	(Sam Hewitt <hewittsamuel@gmail.com>)
- 3c65feb: updated plank theme	(Sam Hewitt <hewittsamuel@gmail.com>)
- 3394d11: updated plank theme	(Sam Hewitt <hewittsamuel@gmail.com>)
- 80f65e2: a few refinements	(Sam Hewitt <hewittsamuel@gmail.com>)
- d3d282d: a few bugfixes	(Sam Hewitt <hewittsamuel@gmail.com>)
- 9dbe261: a few bug fixes	(Sam Hewitt <hewittsamuel@gmail.com>)
- 86fd8b8: improved level bars	(Sam Hewitt <hewittsamuel@gmail.com>)
- e23bbd2: updated colours	(Sam Hewitt <hewittsamuel@gmail.com>)
- 443526f: levelbar improvements	(Sam Hewitt <hewittsamuel@gmail.com>)
- 04b94a1: refinements	(Sam Hewitt <hewittsamuel@gmail.com>)