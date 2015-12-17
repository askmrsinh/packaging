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
%global commit0 617a6b1549d9512da2a01585e18f2ac09a4c530a

name:       paper-gtk-theme
version:    1.0.0
release:    0.168.20151213git617a6b1%{?dist}

Summary:    Paper GTK Theme
Group:      System/GUI/Other
License:    GPL-3.0+
Url:        http://samuelhewitt.com/paper/theme
Source0:    %{name}-%{commit0}.tar.gz
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
