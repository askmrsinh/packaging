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
%global commit0 2a8317e357b781b84a4bf04ea7c6356fbf4b8afc

name:       paper-icon-theme
version:    1.4.0
release:    0.689.20160501git2a8317e%{?dist}

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
* Tue Jun 13 2017 Ashesh Kumar Singh <user501254@gmail.com> 1.4.0-0.689
- 2a8317e: symlink	(Sam Hewitt <sam@snwh.org>)
- 9212d94: Merge pull request #582 from bil-elmoussaoui/xmind	(Sam Hewitt <hewittsamuel@gmail.com>)
- 6ca2b9e: add XMind symlink #519	(Bilal Elmoussaoui <bil.elmoussaoui@gmail.com>)
- 223da6b: Merge pull request #581 from bil-elmoussaoui/symlinks	(Sam Hewitt <hewittsamuel@gmail.com>)
- 2063d91: Create README.md	(Sam Hewitt <hewittsamuel@gmail.com>)
- 38ee903: add Tilix & FeedReader symlinks	(Bilal Elmoussaoui <bil.elmoussaoui@gmail.com>)
- 6dd2d67: update readme	(Sam Hewitt <sam@snwh.org>)
- 1b27257: minor fix	(Sam Hewitt <sam@snwh.org>)
- e34d2c3: Merge pull request #554 from schrieveslaach/master	(Sam Hewitt <hewittsamuel@gmail.com>)
- 2c3e3fc: Merge pull request #564 from ArtyomZorin/master	(Sam Hewitt <hewittsamuel@gmail.com>)
- 377305a: Merge pull request #578 from wincinderith/emacs25-fix	(Sam Hewitt <hewittsamuel@gmail.com>)
- 98bcece: Merge pull request #553 from alexlarsson/master	(Sam Hewitt <hewittsamuel@gmail.com>)
- 547d630: Create Emacs 25 symlinks	(Kevin Boxhoorn <kevinboxhoorn@yahoo.com>)
- c13a9e2: Added symlinks for XFCE apps and the Removable Drives and Media settings panel	(Artyom Zorin <azorin@zoringroup.com>)
- 085fd99: Fixes #486	(Marc Schreiber <marc.schreiber@fh-aachen.de>)
- 5952aaa: Use $(datadir) instead of hardcoding /usr	(Alexander Larsson <alexl@redhat.com>)