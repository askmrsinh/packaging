# GitHub Stuff
%global commit0 55a575386a412544c3ed2b5617a61f842ee4ec15


Name:       arc-icon-theme
Version:    1479849758.55a5753
Release:    0.20161122%{?dist}
Summary:    A flat icon theme to accompany the Arc GTK theme.
Group:      User Interface/Desktops

License:    GPL-3
URL:        https://github.com/horst3180/Arc-icon-theme

Source0:    https://github.com/horst3180/arc-icon-theme/archive/%{commit0}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: autoconf automake

Requires:   moka-icon-theme, faba-icon-theme, gnome-icon-theme, hicolor-icon-theme 

BuildArch:  noarch

%description
The Arc icon pack makes use of simple, clean colours, thin crisp lines and follows the trend for ‘flat’ design. The use of obvious and straight-forward glyphs, symbols and metaphors lends the theme a clear, modern aesthetic. 


%prep
%setup -q


%build
./autogen.sh --prefix=/usr


%install
make install DESTDIR=$RPM_BUILD_ROOT

find ${RPM_BUILD_ROOT} -name "*.sh" -exec chmod -x {} \;


%files
%defattr(-,root,root)
%doc
%{_datadir}/icons/Arc/

%changelog
* Sun May 14 2017 Ashesh Kumar Singh <user501254@gmail.com> 1479849758.55a5753-0.20161122
- 55a5753: bump version	(Horst3180 <horst3180@gmx.net>)
- f26262e: tweak pane-hide,show-symobic	(Horst3180 <horst3180@gmx.net>)
- 664c05e: add input-gaming icon	(Horst3180 <horst3180@users.noreply.github.com>)
- ba985aa: fix rendering script	(Horst3180 <horst3180@users.noreply.github.com>)
- 4c07a04: fix icon alignment	(Horst3180 <horst3180@users.noreply.github.com>)
- 69da5ee: Add preview	(horst3180 <horst3180@users.noreply.github.com>)
- a69db04: fix moka url (#2)	(Jakob Gillich <jakob@gillich.me>)
- 6471480: initial commit	(Horst3180 <horst3180@users.noreply.github.com>)
