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
%global commit0 ade160ee64639c27fb5d0bf9620539c18ce77f00

name:       paper-icon-theme
version:    1.3.0
release:    0.432.20160501gitade160e%{?dist}

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
* Thu May 19 2016 Ashesh Kumar Singh <user501254@gmail.com> 1.3.0-0.432
- ade160e: updated text-x-go colours	(Sam Hewitt <hewittsamuel@gmail.com>)
- 604d76f: added text-x-go	(Sam Hewitt <hewittsamuel@gmail.com>)
- 69b4646: added focuswriter icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 46d3ab6: added amarok symlink	(Sam Hewitt <hewittsamuel@gmail.com>)
- 3a4d920: added amarok icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 6dd085f: added rust mimetype	(Sam Hewitt <hewittsamuel@gmail.com>)
- e5285d9: minor spec fixed	(Sam Hewitt <hewittsamuel@gmail.com>)
- a78cd9c: tweaked spec for OBS	(Sam Hewitt <hewittsamuel@gmail.com>)
- b01b1e6: Merge pull request #177 from user501254/patch-1	(Sam Hewitt <hewittsamuel@gmail.com>)
- af069ae: Update spec file	(Ashesh <user501254@gmail.com>)
- ec755b8: finished folders	(Sam Hewitt <hewittsamuel@gmail.com>)
- ad78795: updated colours in a couple icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 76c7624: added insync icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 88c988a: added network wired disconnected icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- eb6ff0e: added wps office icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 5ce12b1: moved misplaced svg	(Sam Hewitt <hewittsamuel@gmail.com>)
- 1b0dacb: update readme	(Sam Hewitt <hewittsamuel@gmail.com>)
- 202575a: undo install rename	(Sam Hewitt <hewittsamuel@gmail.com>)
- 6b0525d: new firefox icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- a46b4ee: added zotero icon	(Sam Hewitt <hewittsamuel@gmail.com>)