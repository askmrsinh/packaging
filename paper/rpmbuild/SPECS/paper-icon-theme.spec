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
%global commit0 5c3c4ca45d904cd83e377d216612d1d7d993a565

name:       paper-icon-theme
version:    1.3.0
release:    0.445.20160501git5c3c4ca%{?dist}

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
* Fri May 20 2016 Ashesh Kumar Singh <user501254@gmail.com> 1.3.0-0.445
- 5c3c4ca: added extra folders	(Sam Hewitt <hewittsamuel@gmail.com>)
- 8e65404: added clipboard icons;updated battery symbolics	(Sam Hewitt <hewittsamuel@gmail.com>)
- 8ebea8f: added solus icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 57be322: updated a few icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- f5a1be9: added media-flash	(Sam Hewitt <hewittsamuel@gmail.com>)
- d0481d4: updated whatsapp icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- cc00af2: added whatsapp icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 1693a2d: added cairo-dock	(Sam Hewitt <hewittsamuel@gmail.com>)
- 172b108: added extra opera icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 6ef6047: added more distro logos	(Sam Hewitt <hewittsamuel@gmail.com>)
- 1693f86: stylized emacs icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- b3f0f66: updated vlc and vim icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- eec7a83: added intellij idea icon	(Sam Hewitt <hewittsamuel@gmail.com>)