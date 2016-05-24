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
%global commit0 6831599d358f4556bd2d3aeab3183a8f9152cf9d

name:       paper-gtk-theme
version:    2.0.0
release:    0.242.20160501git6831599%{?dist}

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
* Tue May 24 2016 Ashesh Kumar Singh <user501254@gmail.com> 2.0.0-0.242
- 6831599: tweaked budgie header switch styles	(Sam Hewitt <hewittsamuel@gmail.com>)
- 2069957: smaller budgie header switches	(Sam Hewitt <hewittsamuel@gmail.com>)
- 0e8585f: tweaked budgie header switch styles	(Sam Hewitt <hewittsamuel@gmail.com>)
- e2cdacb: added budgie header switch styles	(Sam Hewitt <hewittsamuel@gmail.com>)
- 5aa983e: v2.0.2	(Sam Hewitt <hewittsamuel@gmail.com>)
- 87369ba: more budgie refinements	(Sam Hewitt <hewittsamuel@gmail.com>)
- 3c0ec75: switch style improvements	(Sam Hewitt <hewittsamuel@gmail.com>)
- 3b3c58f: budgie refinements	(Sam Hewitt <hewittsamuel@gmail.com>)
- 44e0b3f: budgie fixes	(Sam Hewitt <hewittsamuel@gmail.com>)