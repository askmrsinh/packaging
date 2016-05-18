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
%global commit0 ba6b0df08b857125047f484977c22ae0b5e4a112

name:       paper-icon-theme
version:    1.3.0
release:    0.413.20160501gitba6b0df%{?dist}

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
* Wed May 18 2016 Ashesh Kumar Singh <user501254@gmail.com> 1.3.0-0.413
- ba6b0df: added antergos icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 25f351c: renamed install script	(Sam Hewitt <hewittsamuel@gmail.com>)
- 3e059eb: updated spec	(Sam Hewitt <hewittsamuel@gmail.com>)
- e29754f: updated spec	(Sam Hewitt <hewittsamuel@gmail.com>)
- 172ac38: updated spec	(Sam Hewitt <hewittsamuel@gmail.com>)
- e28e027: updated spec	(Sam Hewitt <hewittsamuel@gmail.com>)
- e04011b: updated spec	(Sam Hewitt <hewittsamuel@gmail.com>)
- c5a6979: updated spec	(Sam Hewitt <hewittsamuel@gmail.com>)
- cd048f7: updated spec	(Sam Hewitt <hewittsamuel@gmail.com>)
- 05635bc: updated spec	(Sam Hewitt <hewittsamuel@gmail.com>)
- 514e57e: updated spec	(Sam Hewitt <hewittsamuel@gmail.com>)
- 550061a: completed libreoffice icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 4254695: adjusted libreoffice icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 123cbee: fixed typo in icon name	(Sam Hewitt <hewittsamuel@gmail.com>)
- 54a3896: refined some icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 619db69: added popcorn time iocn	(Sam Hewitt <hewittsamuel@gmail.com>)
- df03ab8: added pgadmin icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 7a039a0: added mumble icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 53afa5f: updated key icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- cdc6d69: added bleachbit icon	(Sam Hewitt <hewittsamuel@gmail.com>)