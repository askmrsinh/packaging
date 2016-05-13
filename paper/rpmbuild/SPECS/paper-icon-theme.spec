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
%global commit0 0f7ed07701455c018e1e1991d93e0a26d05f0ecf

name:       paper-icon-theme
version:    1.3.0
release:    0.362.20160501git0f7ed07%{?dist}

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
* Fri May 13 2016 Ashesh Kumar Singh <user501254@gmail.com> 1.3.0-0.362
- 0f7ed07: added rstudio icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- aba460f: added flux, folder-dropbox	(Sam Hewitt <hewittsamuel@gmail.com>)
- 6428e60: added status icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 93fa26d: added zsnes icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 9340d5e: added telegram icon & symlinks	(Sam Hewitt <hewittsamuel@gmail.com>)
- 82dc274: added symlinks	(Sam Hewitt <hewittsamuel@gmail.com>)
- b8020fb: added session/login icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 0093dfb: desktop icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- fb0492f: updated firefox icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- fe93958: added link	(Sam Hewitt <hewittsamuel@gmail.com>)
- 37ec975: added a few icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- f1bbeae: added a few web icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 4ea4bc6: updated blue folders	(Sam Hewitt <hewittsamuel@gmail.com>)
- 3443154: updated coloured folders	(Sam Hewitt <hewittsamuel@gmail.com>)
- 413de02: adding icons	(Sam Hewitt <hewittsamuel@gmail.com>)