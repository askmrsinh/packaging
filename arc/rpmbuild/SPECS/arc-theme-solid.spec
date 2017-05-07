# GitHub Stuff
%global commit0 766ae1a386134f122bab4a0456af802e7a5b66bd


Name:       arc-theme-solid
Version:    1488477732.766ae1a
Release:    32.2%{?dist}
Summary:    Arc is a theme for GTK 3, GTK 2 and Gnome-Shell.
Group:      User Interface/Desktops

License:    GPL-3
URL:        https://github.com/horst3180/Arc-theme

Source0:    https://github.com/horst3180/arc-theme/archive/%{commit0}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: autoconf automake gtk3-devel

%if 0%{?suse_version}
Requires:   gtk2-engine-murrine
Requires:   gtk2-theming-engine-adwaita
%else
Requires:   gtk-murrine-engine
Requires:   gnome-themes-standard
%endif

Conflicts:  arc-theme

BuildArch:  noarch

%description
Arc is a flat theme with transparent elements for GTK 3, GTK 2 and Gnome-Shell. It supports GTK 3 and GTK 2 based desktop environments like Gnome, Unity, Budgie, Pantheon, etc.


%prep
%setup -q


%build
./autogen.sh --prefix=/usr --disable-transparency


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
* Mon May 08 2017 Ashesh Kumar Singh <user501254@gmail.com> 1488477732.766ae1a-32.2
- 766ae1a: fix atril toolbar background (fix #741)	(Horst3180 <horst3180@gmx.net>)
- 947a0ad: fix asymmetric circular buttons (fix #728)	(Horst3180 <horst3180@gmx.net>)
- 81c4f01: Merge pull request #734 from leigh123linux/fix_gradient_warning	(horst3180 <horst3180@users.noreply.github.com>)
- e411c4b: gtk 3.22: fix frame borders (#742)	(Horst3180 <horst3180@gmx.net>)
- 0df7eae: fix missing gradient warning	(leigh123linux <leigh123linux@googlemail.com>)
- 0af4e07: add link to Arc KDE to README.md	(Horst3180 <horst3180@gmx.net>)
- 78dd4dd: update readme	(Horst3180 <horst3180@gmx.net>)
- 7e3043f: add official fedora package name to readme (fix #726)	(Horst3180 <horst3180@gmx.net>)
- acbf49d: Merge pull request #723 from GeneralFailer/master	(horst3180 <horst3180@users.noreply.github.com>)
- ef20dcd: Correct capitalization	(Daniil Zhilin <just4steam778@gmail.com>)
- 530569a: Correct capitalization	(Daniil Zhilin <just4steam778@gmail.com>)
- b8640ca: Merge pull request #718 from unixfox/patch-1	(horst3180 <horst3180@users.noreply.github.com>)
- d2305d7: Correction of the package name of AUR	(Emilien Devos <unixfox@users.noreply.github.com>)
- 7da711e: gtk2: fix thunar bulk rename entry (fix #707)	(Horst3180 <horst3180@gmx.net>)
- d641d3d: add lightdm panel padding (fix #678)	(Horst3180 <horst3180@gmx.net>)
- ef96c20: be more careful with libreoffice toolbar workaround (#670)	(Horst3180 <horst3180@gmx.net>)
- 9047b20: cinnamon 3.2: fix panel launcher styling (#695)	(Horst3180 <horst3180@gmx.net>)
- 8d26ecd: cinnamon 3.2: remove menu min-width (#695)	(Horst3180 <horst3180@gmx.net>)
- 57ad591: cinnamon 3.2: fix notifications inside menus (#695)	(Horst3180 <horst3180@gmx.net>)
- e4b0e99: bump version	(Horst3180 <horst3180@gmx.net>)
- a6ad262: GTK 3.20, 3.22: add some gnome-tweak-tool styling	(Horst3180 <horst3180@users.noreply.github.com>)
- 1569933: add Cinnamon 3.2 support (#695)	(Horst3180 <horst3180@users.noreply.github.com>)
- 2df5d9d: Update README.md	(horst3180 <horst3180@users.noreply.github.com>)
- 0012981: Update README.md	(horst3180 <horst3180@users.noreply.github.com>)
- 59ee31e: Update README.md	(horst3180 <horst3180@users.noreply.github.com>)
- a4936b7: Merge pull request #690 from zach-adams/patch-4	(horst3180 <horst3180@users.noreply.github.com>)
- d65e1a6: Update Arch Linux package links	(Zach Adams <zach@zach-adams.com>)
- 419ebbb: gtk 3.18: fix gnome-flashback panel background (#688)	(Horst3180 <horst3180@users.noreply.github.com>)
- 152a427: cinnamon: use correct path for menu-separator.svg (fix #689)	(Horst3180 <horst3180@users.noreply.github.com>)
- 2ca1989: gtk2: fix geany search combobox border (#674)	(Horst3180 <horst3180@users.noreply.github.com>)
- 20edae5: gnome-shell: reduce dash padding (fix #561)	(Horst3180 <horst3180@users.noreply.github.com>)
- a9ce9d5: gtk2: fix geany search entries (#674)	(Horst3180 <horst3180@users.noreply.github.com>)
- cbc5050: add thumbnails for cinnamon theme chooser (#592)	(Horst3180 <horst3180@users.noreply.github.com>)
- 5acba94: fix disabled entry border-color in header bars (#668)	(Horst3180 <horst3180@users.noreply.github.com>)
- d3d70b4: bump version	(Horst3180 <horst3180@users.noreply.github.com>)
- 5b15bdc: gtk3: add a workaround for broken Libreoffice toolbar styling	(Horst3180 <horst3180@users.noreply.github.com>)
- efdd708: gtk2: fix mousepad find and replace textbox (fix #664)	(Horst3180 <horst3180@users.noreply.github.com>)
- b8a8461: revert recent pathbar changes	(Horst3180 <horst3180@users.noreply.github.com>)
- bd67b39: more builder tweaks	(Horst3180 <horst3180@users.noreply.github.com>)
- 89ee981: gnome-builder 3.22 fixes	(Horst3180 <horst3180@users.noreply.github.com>)
- 1e317d2: gtk 3.20: try to fix unity decorations (#660)	(Horst3180 <horst3180@users.noreply.github.com>)
- e2fde83: add Mate OSD window styling	(Horst3180 <horst3180@users.noreply.github.com>)
- 1959509: bump version	(Horst3180 <horst3180@users.noreply.github.com>)
- 9616edd: gnome-shell: updates for 3.22	(Horst3180 <horst3180@users.noreply.github.com>)
- 39f00f0: Merge pull request #654 from chewi/master	(horst3180 <horst3180@users.noreply.github.com>)
- 2fd0b4d: add borders to metacity-1 and metacity-2 themes	(Horst3180 <horst3180@users.noreply.github.com>)
- fb1a401: add more Gnome Flashback styling	(Horst3180 <horst3180@users.noreply.github.com>)
- a7e9f80: spinbutton tweaks	(Horst3180 <horst3180@users.noreply.github.com>)
- 97d9627: fix color of disabled labels in checked buttons	(Horst3180 <horst3180@users.noreply.github.com>)
- f416c04: Don't require GTK+3 at configure time when it's not needed	(James Le Cuirot <chewi@gentoo.org>)
- bd6e288: update Readme	(Horst3180 <horst3180@users.noreply.github.com>)
- 6e3491f: tweak treeview progressbars	(Horst3180 <horst3180@users.noreply.github.com>)
- b7bebc5: remove sidebar background in wingpanel popovers	(Horst3180 <horst3180@users.noreply.github.com>)
- ad31038: fix jumping granite tabs	(Horst3180 <horst3180@users.noreply.github.com>)
- 2d2a3ba: update wingpanel styling	(Horst3180 <horst3180@users.noreply.github.com>)
- 045273f: remove unneeded pantheon terminal styling	(Horst3180 <horst3180@users.noreply.github.com>)
- bee90f0: use blue highlight in wingpanel popovers	(Horst3180 <horst3180@users.noreply.github.com>)
- 3e6c57d: fix bold font in wingpanel popovers	(Horst3180 <horst3180@users.noreply.github.com>)
- 8266ad0: add some mate application styling	(Horst3180 <horst3180@users.noreply.github.com>)
- 64382c9: mate-panel, gnome-panel: remove transparency	(Horst3180 <horst3180@users.noreply.github.com>)
- 32a5aa9: gnome-panel: remove double background from menubar	(Horst3180 <horst3180@users.noreply.github.com>)
- c58544c: gtk2: improve combobox styling	(Horst3180 <horst3180@users.noreply.github.com>)
- 871f775: gtk2: fix unreadable text in VMware horizon client (#628)	(Horst3180 <horst3180@users.noreply.github.com>)
- 3fd402c: gnome-shell: fix jumping switcher list subitems (#636)	(Horst3180 <horst3180@users.noreply.github.com>)
- ea8aa16: Merge pull request #630 from w1res/patch-1	(horst3180 <horst3180@users.noreply.github.com>)
- 28dfc77: cinnamon: add proper popup-combo-menu styling (#634)	(Horst3180 <horst3180@users.noreply.github.com>)
- e250405: fix gnome-flashback panel background	(Horst3180 <horst3180@users.noreply.github.com>)
- 6f76588: fix bogus box-shadows in stack-switchers	(Horst3180 <horst3180@users.noreply.github.com>)
- ed153bb: separate disabled linked buttons more clearly	(Horst3180 <horst3180@users.noreply.github.com>)
- b0181fb: Merge pull request #645 from scriptkitties/master	(horst3180 <horst3180@users.noreply.github.com>)
- f1490cd: Merge pull request #639 from feskyde/patch-1	(horst3180 <horst3180@users.noreply.github.com>)
- 050bd83: Add Gentoo overlay to README	(Patrick Spek <p.spek@tyil.nl>)
- 16aad05: Removing unnecessary repeat of "list" word	(Federico Damián Schonborn <federico.d.schonborn@gmail.com>)
- 12179bf: Remove checks and make this more readable	(Federico Damián Schonborn <federico.d.schonborn@gmail.com>)
- c374cba: clean up treeview style properties	(Horst3180 <horst3180@users.noreply.github.com>)
- 32017a2: fix infobar styling	(Horst3180 <horst3180@users.noreply.github.com>)
- 57248f7: clean up calendar styling	(Horst3180 <horst3180@users.noreply.github.com>)
- 99d645f: simpler outline-color styling	(Horst3180 <horst3180@users.noreply.github.com>)
- 3f11de0: hide separator in font and filechooser buttons	(Horst3180 <horst3180@users.noreply.github.com>)
- 1c70646: nautilus: add conflict-row styling	(Horst3180 <horst3180@users.noreply.github.com>)
- 0cfa794: GTK 3.22: fix parsing errors	(Horst3180 <horst3180@users.noreply.github.com>)
- 5bd92f1: don't use background images for entries	(Horst3180 <horst3180@users.noreply.github.com>)
- 780bd46: add build support for Gnome 3.22	(Horst3180 <horst3180@users.noreply.github.com>)
- e6ec849: refactor xfwm theme	(Horst3180 <horst3180@users.noreply.github.com>)
- 06b0911: don't use selected_fg_color in weird places	(Horst3180 <horst3180@users.noreply.github.com>)
- 9c4b802: underp gtk2 render-assets script	(Horst3180 <horst3180@users.noreply.github.com>)
- 3932218: use color swatches for selected bg and fg in svg assets	(Horst3180 <horst3180@users.noreply.github.com>)
- 211dd7a: Merge pull request #622 from Beta1440/gnome-shell-slider-patch	(horst3180 <horst3180@users.noreply.github.com>)
- 9433174: Fix typo in README.md	(Adam Siembida <w1res@users.noreply.github.com>)
- 2668df1: Fix slider for gnome-shell	(Dela Anthonio <dell.anthonio@gmail.com>)
- e10fefb: Merge pull request #624 from feskyde/patch-1	(horst3180 <horst3180@users.noreply.github.com>)
- 85b5541: Put instructions at the top of sections	(feskyde <federico.d.schonborn@gmail.com>)
- 9439f10: Add base distribution to details	(feskyde <federico.d.schonborn@gmail.com>)
- d6155b4: Add the version of desktop environment, Murrine, "gts" and distribution in details	(feskyde <federico.d.schonborn@gmail.com>)
- 40b7bd1: Avoid people from ignoring the template and add details	(feskyde <federico.d.schonborn@gmail.com>)
- 9478b8d: Update README.md	(Horst3180 <horst3180@users.noreply.github.com>)
- ee44856: xfce: fix desktop icon shadows (#607)	(Horst3180 <horst3180@users.noreply.github.com>)
- 894573e: gedit 3.20: make sidebar separator dark (fix #591)	(Horst3180 <horst3180@users.noreply.github.com>)
- 4d58f02: tweak gedit-map-frame styling (fix #584)	(Horst3180 <horst3180@users.noreply.github.com>)
- f328026: Ignore project files of IntellijIDEA (#562)	(Pavel Zlámal <zlamal@cesnet.cz>)
- 89728b5: 3.18: fix sidebar-button	(Horst3180 <horst3180@users.noreply.github.com>)
- d24a7b5: Update README.md	(horst3180 <horst3180@users.noreply.github.com>)
- e0cbe3f: Update README.md	(horst3180 <horst3180@users.noreply.github.com>)
- 3095952: bump version	(Horst3180 <horst3180@users.noreply.github.com>)
- 1de4ef7: gnome-shell: remove menu separator margins	(Horst3180 <horst3180@users.noreply.github.com>)
- 76d343f: fix unity window decorations (#566)	(Horst3180 <horst3180@users.noreply.github.com>)
- 226098a: gtk2: more entry fixes	(Horst3180 <horst3180@users.noreply.github.com>)
- 519718b: use more specific selectors	(Horst3180 <horst3180@users.noreply.github.com>)
- 2f80d3c: fix switches in selected menuitems (fix #556)	(Horst3180 <horst3180@users.noreply.github.com>)
- 2b1a290: fix hexchat input box (#558)	(Horst3180 <horst3180@users.noreply.github.com>)
- d9d1772: bump version	(Horst3180 <horst3180@users.noreply.github.com>)
- 543d5a9: gtk2: fix entry styling (fix #547)	(Horst3180 <horst3180@users.noreply.github.com>)
- e4f382c: gtk2: make panel buttons consistent	(Horst3180 <horst3180@users.noreply.github.com>)
- 789d509: merge xfce-notify theme into the gtk2 theme	(Horst3180 <horst3180@users.noreply.github.com>)
- 9ac60f1: panel.rc: clean up	(Horst3180 <horst3180@users.noreply.github.com>)
- 324722a: fix xfce-panel progressbar background	(Horst3180 <horst3180@users.noreply.github.com>)
- ca76d0e: use accent color for menu highlight (fix #135)	(Horst3180 <horst3180@users.noreply.github.com>)
- 753130a: tweak unity panel background color	(Horst3180 <horst3180@users.noreply.github.com>)
- 5fd6b58: remove textview border	(Horst3180 <horst3180@users.noreply.github.com>)
- da9ce16: gedit: fix subpixel-rendering in open-document-selector-treeview (fix #549)	(Horst3180 <horst3180@users.noreply.github.com>)
- d02ab7a: xfwm theme refinements	(Horst3180 <horst3180@users.noreply.github.com>)
- d32e573: Update README.md	(horst3180 <horst3180@users.noreply.github.com>)
- 662fbcd: gtk3: export link_color variable (fix #536)	(Horst3180 <horst3180@users.noreply.github.com>)
- c5ed48f: fix a firefox workaround	(Horst3180 <horst3180@users.noreply.github.com>)
- d62246c: gnome-shell: fix volume mixer extension width (fix #486)	(Horst3180 <horst3180@users.noreply.github.com>)
- a27b333: gnome-shell: add support for the multi-monitors-add-on extension (fix #464)	(Horst3180 <horst3180@users.noreply.github.com>)
- 6539bc9: gtk3: remove borders from nautilus-list-view (fix #533)	(Horst3180 <horst3180@users.noreply.github.com>)
- 28cdb3e: gtk3: reduce menubar height to match gtk2 theme (fix #535)	(Horst3180 <horst3180@users.noreply.github.com>)
- cc20a2e: 3.20: dark sidebars style for caja	(Horst3180 <horst3180@users.noreply.github.com>)
- 98360ab: fix the last commit	(Horst3180 <horst3180@users.noreply.github.com>)
- 0a34ab5: 3.20: caja fixes	(Horst3180 <horst3180@users.noreply.github.com>)
- c6262bb: 3.20: add mate-panel support (#524)	(Horst3180 <horst3180@users.noreply.github.com>)