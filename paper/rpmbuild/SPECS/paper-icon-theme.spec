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
%global commit0 5cee4108f0cfd5209438a299723bb8e6e231f2c9

name:       paper-icon-theme
version:    1.3.0
release:    0.371.20160501git5cee410%{?dist}

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
* Sat May 14 2016 Ashesh Kumar Singh <user501254@gmail.com> 1.3.0-0.371
- 5cee410: added some distro logos	(Sam Hewitt <hewittsamuel@gmail.com>)
- 05612f0: refined icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 594bf30: updated deja dup icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- b2ae24f: added exaile icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 5e1cd79: added codeblocks icons; links to others	(Sam Hewitt <hewittsamuel@gmail.com>)
- b92dfe9: added netbeans icon & linked others	(Sam Hewitt <hewittsamuel@gmail.com>)
- 928585c: added qtox icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- e350da5: added fluxgui-panel	(Sam Hewitt <hewittsamuel@gmail.com>)
- 94dfeaf: added gnome-nettool icon	(Sam Hewitt <hewittsamuel@gmail.com>)