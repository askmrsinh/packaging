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
%global commit0 70f1c0453521a17d80db2d2d473cc7b3e6e7b913

name:       paper-icon-theme
version:    1.3.0
release:    0.564.20160501git70f1c04%{?dist}

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
* Sun Jul 03 2016 Ashesh Kumar Singh <user501254@gmail.com> 1.3.0-0.564
- 70f1c04: Merge pull request #288 from Findus23/icedove	(Sam Hewitt <hewittsamuel@gmail.com>)
- 0000257: add symlink for icedove	(Lukas Winkler <l.winkler23@mailbox.org>)
- 5944e66: Merge pull request #276 from sappo/master	(Sam Hewitt <hewittsamuel@gmail.com>)
- a8514ce: Merge pull request #285 from Findus23/master	(Sam Hewitt <hewittsamuel@gmail.com>)
- 78ac875: add symlink for firefox-esr	(Lukas Winkler <l.winkler23@mailbox.org>)
- 0ed0925: Problem: seafile client references icon by seafile instead of seafile-client	(Kevin Sapper <mail@kevinsapper.de>)