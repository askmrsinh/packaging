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
%global commit0 a7d5d4f04a118d44336e1386267f2a48f29e1fa7

name:       paper-icon-theme
version:    1.3.0
release:    0.662.20160501gita7d5d4f%{?dist}

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
* Sat Oct 08 2016 Ashesh Kumar Singh <user501254@gmail.com> 1.3.0-0.662
- a7d5d4f: added some package icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- f287885: added symlinks	(Sam Hewitt <hewittsamuel@gmail.com>)
- 27fc5ed: added symlinks	(Sam Hewitt <hewittsamuel@gmail.com>)
- d6cbac5: added deb icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 38572e1: adjusted archive filenames and links	(Sam Hewitt <hewittsamuel@gmail.com>)
- 89353a0: adjusted document mime icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- ebaae7c: adjusted zip icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- d0c17aa: refined zip icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 09bc577: added bzip icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 8d9aea8: refined targz icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 4b0c9e8: added symlinks	(Sam Hewitt <hewittsamuel@gmail.com>)
- 4dccd52: added gz symlinks	(Sam Hewitt <hewittsamuel@gmail.com>)
- 52c4826: added gz icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 84a3bfa: added tar symlinks	(Sam Hewitt <hewittsamuel@gmail.com>)
- 976f699: added tar icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 40a6d28: refined package mimes	(Sam Hewitt <hewittsamuel@gmail.com>)
- bdddd54: extended package mimes	(Sam Hewitt <hewittsamuel@gmail.com>)
- c6cd607: updated pdf icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 18de367: added freecad icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- e437de3: added hex icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 47b672a: added retext icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- c9c6e51: added typora icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- b2c4985: added museeq icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- bbbf37b: added google hangouts icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 9b23012: added symlink	(Sam Hewitt <hewittsamuel@gmail.com>)
- fb9fb8b: added sparkleshare panel icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- e638b90: added missing panel icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 00b1750: oops v1.3.4	(Sam Hewitt <hewittsamuel@gmail.com>)
- 14fe393: v1.3.3	(Sam Hewitt <hewittsamuel@gmail.com>)
- b1c99b9: updated battery icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- a0de0b9: added a couple icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 2ad06a4: fixed calendar icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- e376372: fixed calendar icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 6ae2b43: added play music icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 4434a03: added xmind icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- cdec7a9: added icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 389d0f2: added smartgit icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 4e8aaa9: added mono icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- d9bf170: added xnoise icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 78e3f4a: added a tonne of calendar icons	(Sam Hewitt <hewittsamuel@gmail.com>)
- 675561e: added antimicro icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- 82e13d3: added ghex icon	(Sam Hewitt <hewittsamuel@gmail.com>)
- e16f79a: added discord-canary icon	(Sam Hewitt <hewittsamuel@gmail.com>)