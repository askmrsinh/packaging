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
%global commit0 4497b8605dde6ce45f678fe3d8bf88d7c06870b1

name:       paper-icon-theme
version:    1.3.0
release:    0.386.20160501git4497b86%{?dist}

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
* Mon May 16 2016 Ashesh Kumar Singh <user501254@gmail.com> 1.3.0-0.386
- 4497b86: Merge pull request #160 from bil-elmoussaoui/master	(Sam Hewitt <hewittsamuel@gmail.com>)
- 102ef84: add symlinks for Chrome tray	(Bilal Elmoussaoui <bil.elmoussaoui@gmail.com>)
- 4d6b163: added link	(Sam Hewitt <hewittsamuel@gmail.com>)
- 5b7db4a: added caffeine icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 94acba6: added computer-fail	(Sam Hewitt <hewittsamuel@gmail.com>)
- 4bad23a: remove broken links	(Sam Hewitt <hewittsamuel@gmail.com>)
- d370d0a: added a tonne of symbolic links	(Sam Hewitt <hewittsamuel@gmail.com>)
- e904cc9: refined desktops	(Sam Hewitt <hewittsamuel@gmail.com>)
- 6e53166: refined terminal icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 5d338f4: refined terminal icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 163d61b: added youtube icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 1e6b4e0: added wireshark, qbittorrent icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- ed6165a: added applications-multimedia; fixed misnamed icon	(Sam Hewitt <hewittsamuel@gmail.com>)