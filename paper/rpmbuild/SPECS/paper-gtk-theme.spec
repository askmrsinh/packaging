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
%global commit0 dea5f97b12e4f41dddbd01a1529760761aa3784e

name:       paper-gtk-theme
version:    2.1.0
release:    0.261.20160501gitdea5f97%{?dist}

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
* Thu May 26 2016 Ashesh Kumar Singh <user501254@gmail.com> 2.1.0-0.261
- dea5f97: added a dark portion to the gtk2 theme	(Sam Hewitt <hewittsamuel@gmail.com>)
- c35c9c8: toned down text colour in gtk2	(Sam Hewitt <hewittsamuel@gmail.com>)
- c02e6b2: fixed missing asset	(Sam Hewitt <hewittsamuel@gmail.com>)
- 8a06ac9: redid the GTK2 theme	(Sam Hewitt <hewittsamuel@gmail.com>)