# GitHub Stuff
%global commit0 c561afa73c345022dc23bbbb2b8707d705043fa2


Name:		arc-theme
Version:  1459454111.c561afa
Release:  65.1%{?dist}
Summary:	Arc is a theme for GTK 3, GTK 2 and Gnome-Shell.
Group:		User Interface/Desktops

License:	GPL-3
URL:		https://github.com/horst3180/Arc-theme

Source0:	https://github.com/horst3180/arc-theme/archive/%{commit0}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: autoconf automake gtk3-devel

%if 0%{?suse_version}
Requires:	gtk2-engine-murrine
Requires:	gtk2-theming-engine-adwaita
%else
Requires:	gtk-murrine-engine
Requires:	gnome-themes-standard
%endif

BuildArch:	noarch

%description
Arc is a flat theme with transparent elements for GTK 3, GTK 2 and Gnome-Shell. It supports GTK 3 and GTK 2 based desktop environments like Gnome, Unity, Budgie, Pantheon, etc.


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
%{_datadir}/themes/Arc
%{_datadir}/themes/Arc-Darker
%{_datadir}/themes/Arc-Dark

%changelog

