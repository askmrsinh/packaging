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
%global commit0 ca720c6627eced390c04a86a64b69d3d1f57ff8b

name:       paper-icon-theme
version:    1.1.0
release:    0.238.20151212gitca720c6%{?dist}

Summary:    Paper Icon theme
Group:      System/GUI/Other
License:    CC-BY-SA-4.0
Url:        http://samuelhewitt.com/paper/icons
Source0:    %{name}-%{commit0}.tar.gz
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
