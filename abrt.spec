#
# TODO:
# - SysV init scripts for -addon-ccpp, -addon-kerneloops, -addon-pstoreoops, -addon-upload-watch, -addon-vmcore, -addon-xorg
#
# Conditional build:
%bcond_without	tests	# disable pythontests
%bcond_with	rpm5	# build with rpm5

%define		libreport_ver	2.17.0
Summary:	Automatic bug detection and reporting tool
Summary(pl.UTF-8):	Narzędzie do automatycznego wykrywania i zgłaszania błędów
Name:		abrt
Version:	2.17.5
Release:	2
License:	GPL v2+
Group:		Applications/System
#Source0Download: https://github.com/abrt/abrt/releases
Source0:	https://github.com/abrt/abrt/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	3844c4c81019f573fe1e7db9cbe05b52
Source1:	%{name}.init
Patch0:		%{name}-rpm5.patch
Patch1:		%{name}-rpm.patch
Patch2:		%{name}-link.patch
Patch3:		%{name}-split-usr.patch
URL:		https://abrt.readthedocs.org/
BuildRequires:	asciidoc
%{?with_tests:BuildRequires:	augeas}
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.11
BuildRequires:	dbus-devel
BuildRequires:	docbook-dtd45-xml
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	glib2-devel >= 1:2.55.1
BuildRequires:	gsettings-desktop-schemas-devel >= 3.15.1
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	json-c-devel
BuildRequires:	libgomp-devel
BuildRequires:	libnotify-devel >= 0.7.0
BuildRequires:	libreport-devel >= %{libreport_ver}
BuildRequires:	libreport-gtk-devel >= %{libreport_ver}
BuildRequires:	libreport-web-devel >= %{libreport_ver}
BuildRequires:	libselinux-devel
BuildRequires:	libsoup3-devel >= 3.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel
BuildRequires:	python3-devel >= 1:3.6
BuildRequires:	python3-modules >= 1:3.6
%{?with_tests:BuildRequires:	python3-pytest}
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-devel >= 4.5-28
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.752
BuildRequires:	satyr-devel >= 0.21
BuildRequires:	sphinx-pdg-3
BuildRequires:	systemd-devel >= 1:209
BuildRequires:	xmlto
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires:	%{name}-libs = %{version}-%{release}
Provides:	group(abrt)
Provides:	user(abrt)
Obsoletes:	abrt-addon-coredump-helper < 2.13.0
Obsoletes:	abrt-addon-python < 2.13.0
Obsoletes:	abrt-atomic < 2.13.0
Obsoletes:	abrt-cli < 2.13.0
Obsoletes:	abrt-plugin-catcut < 2.1
Obsoletes:	abrt-plugin-filetransfer < 2.1
Obsoletes:	abrt-plugin-rhfastcheck < 2.1
Obsoletes:	abrt-plugin-rhticket < 2.1
Obsoletes:	abrt-plugin-runapp < 2.1
Obsoletes:	abrt-plugin-sosreport < 2.1
Obsoletes:	abrt-plugin-sqlite3 < 1.0.7
Obsoletes:	abrt-plugin-ticketuploader < 2.1
Obsoletes:	abrt-retrace-client < 2.16
Obsoletes:	bash-completion-abrt < 2.17
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ABRT is a tool to help users to detect defects in applications and to
create a bug report with all informations needed by maintainer to fix
it. It uses plugin system to extend its functionality.

%description -l pl.UTF-8
ABRT to narzędzie pomagające użytkownikom w wykrywaniu defektów w
aplikacjach oraz tworzeniu raportów błędów ze wszystkimi informacjami
potrzebnymi utrzymującemu pakiet do poprawienia go. Wykorzystuje
system wtyczek do rozszerzania funkcjonalności.

%package libs
Summary:	ABRT shared library
Summary(pl.UTF-8):	Biblioteka współdzielona ABRT
Group:		Libraries
Requires:	glib2 >= 1:2.55.1
Requires:	libreport >= %{libreport_ver}

%description libs
ABRT shared library.

%description libs -l pl.UTF-8
Biblioteka współdzielona ABRT.

%package devel
Summary:	Header files for ABRT livrary
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotekia ABRT
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.55.1
Requires:	libreport-devel >= %{libreport_ver}

%description devel
Header files for ABRT livrary.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki ABRT.

%package addon-ccpp
Summary:	ABRT's C/C++ addon
Summary(pl.UTF-8):	Dodatek C/C++ do ABRT
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cpio
Requires:	elfutils
Requires:	gdb >= 7.0-3
Requires:	satyr >= 0.21
Obsoletes:	abrt-atomic < 2.13

%description addon-ccpp
This package contains hook for C/C++ crashed programs and abrt's C/C++
analyzer plugin.

%description addon-ccpp -l pl.UTF-8
Ten pakiet zawiera punkt zaczepienia dla programów w C/C++, które
uległy awarii oraz wtyczkę analizatora C/C++ ABRT.

%package addon-kerneloops
Summary:	ABRT's kerneloops addon
Summary(pl.UTF-8):	Dodatek kerneloops do ABRT
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	curl
Requires:	libreport-plugin-kerneloops >= %{libreport_ver}
Obsoletes:	abrt-plugin-kerneloops < 0.0.7.2
Obsoletes:	abrt-plugin-kerneloopsreporter < 1.0.7
Obsoletes:	kerneloops < 0.0.7.2

%description addon-kerneloops
This package contains plugin for collecting kernel crash information
from system log.

%description addon-kerneloops -l pl.UTF-8
Ten pakiet zawiera wtyczkę do zbierania informacji o awarii jądra z
logu systemowego.

%package addon-pstoreoops
Summary:	ABRT's pstoreoops addon
Summary(pl.UTF-8):	Dodatek pstoreoops do ABRT
Group:		Libraries
Requires:	%{name}-addon-kerneloops = %{version}-%{release}
Obsoletes:	abrt-addon-uefioops < 2.1.7

%description addon-pstoreoops
This package contains plugin for collecting kernel oopses from pstore
storage.

%description addon-pstoreoops -l pl.UTF-8
Ten pakiet zawiera wtyczkę do zbierania oopsów jądra z danych pstore.

%package addon-python3
Summary:	ABRT's addon for catching and analyzing Python 3 exceptions
Summary(pl.UTF-8):	Dodatek ABRT do przechwytywania i analizy wyjątków Pythona 3
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-python3 = %{version}-%{release}
# for detecting package name containing offending file
%{!?with_rpm5:Suggests:	python3-rpm}
# for logging to journal
Suggests:	python3-systemd

%description addon-python3
This package contains Python hook and Python analyzer plugin for
handling uncaught exception in Python 3 programs.

%description addon-python3 -l pl.UTF-8
Ten pakiet zawiera pythonowy punkt zaczepienia oraz wtyczkę
analizatora Pythona do obsługi nie obsłużonych wyjątków w programach w
Pythonie 3.

%package addon-upload-watch
Summary:	ABRT's upload addon
Summary(pl.UTF-8):	Dodatek upload do ABRT
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description addon-upload-watch
This package contains hook for uploaded problems.

%description addon-upload-watch -l pl.UTF-8
Ten pakiet zawiera uchwyt dla problemów przysłanych.

%package addon-vmcore
Summary:	ABRT's vmcore addon
Summary(pl.UTF-8):	Dodatek vmcore do ABRT
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-addon-kerneloops = %{version}-%{release}
Requires:	crash

%description addon-vmcore
This package contains plugin for collecting kernel crash information
from vmcore files.

%description addon-vmcore -l pl.UTF-8
Ten pakiet zawiera wtyczkę do zbierania informacji o awarii jądra z
plików vmcore.

%package addon-xorg
Summary:	ABRT's Xorg addon
Summary(pl.UTF-8):	Dodatek Xorg do ABRT
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	curl

%description addon-xorg
This package contains plugin for collecting Xorg crash information
from Xorg log.

%description addon-xorg -l pl.UTF-8
Ten pakiet zawiera wtyczkę do zbierania informacji o awarii jądra z
logu Xorg.

%package plugin-bodhi
Summary:	ABRT's bodhi plugin
Summary(pl.UTF-8):	Wtyczka bodhi do ABRT
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libreport-web >= %{libreport_ver}
Obsoletes:	libreport-plugin-bodhi < 2.0.16

%description plugin-bodhi
Plugin to search for a new updates in bodhi server.

%description plugin-bodhi -l pl.UTF-8
Wtyczka do wyszukiwania nowych uaktualnień na serwerze bodhi.

%package dbus
Summary:	ABRT DBus service
Summary(pl.UTF-8):	Usługa DBus ABRT
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	libreport >= %{libreport_ver}

%description dbus
ABRT DBus service which provides org.freedesktop.problems API on DBus
and uses PolicyKit to authorize to access the problem data.

%description dbus -l pl.UTF-8
Usługa DBus ABRT, udostępniająca poprzez DBus API
org.freedesktop.problems, używająca PolicyKit do autoryzacji dostępu
do danych o problemach.

%package python3
Summary:	ABRT Python 3 API
Summary(pl.UTF-8):	API Pythona 3 do ABRT
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python3-libreport >= %{libreport_ver}
Obsoletes:	abrt-python < 2.13.0

%description python3
High-level API for querying, creating and manipulating problems
handled by ABRT in Python.

%description python3 -l pl.UTF-8
Wysokopoziomowe API do odpytywania, tworzenia i obróbki z poziomu
Pythona 3 problemów obsługiwanych przez ABRT.

%package gui
Summary:	ABRT's GUI
Summary(pl.UTF-8):	Graficzny interfejs użytkownika do ABRT
Group:		X11/Applications
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-dbus = %{version}-%{release}
Requires:	%{name}-gui-libs = %{version}-%{release}
Suggests:	gnome-abrt
Provides:	abrt-applet = %{version}-%{release}
Obsoletes:	abrt-applet < 0.0.5
Conflicts:	abrt-applet < 0.0.5

%description gui
GTK+ wizard for convenient bug reporting.

%description gui -l pl.UTF-8
Oparty na GTK+ kreator do wygodnego zgłaszania błędów.

%package gui-libs
Summary:	ABRT's GUI library
Summary(pl.UTF-8):	Biblioteka graficznego interfejsu użytkownika ABRT
Group:		X11/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gtk+3 >= 3.0

%description gui-libs
ABRT's GUI library.

%description gui-libs -l pl.UTF-8
Biblioteka graficznego interfejsu użytkownika ABRT.

%package gui-devel
Summary:	Header files for ABRT GUI library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki graficznego interfejsu użytkownika ABRT
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gui-libs = %{version}-%{release}
Requires:	gtk+3-devel >= 3.0

%description gui-devel
Header files for ABRT GUI library.

%description gui-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki graficznego interfejsu użytkownika ABRT.

%package desktop
Summary:	Virtual package to install all necessary packages for usage from desktop environment
Summary(pl.UTF-8):	Writualny pakiet do instalacji pakietów potrzebnych do użycia w środowisku graficznym
Group:		X11/Applications
# This package should be installed when anything requests bug-buddy;
# installing abrt-desktop should result in the abrt which works without
# any tweaking in abrt.conf (IOW: all plugins mentioned there must be installed)
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-addon-ccpp = %{version}-%{release}
Requires:	%{name}-addon-kerneloops = %{version}-%{release}
Requires:	%{name}-addon-pstoreoops = %{version}-%{release}
Requires:	%{name}-addon-python3 = %{version}-%{release}
Requires:	%{name}-addon-vmcore = %{version}-%{release}
Requires:	%{name}-addon-xorg = %{version}-%{release}
Requires:	%{name}-gui = %{version}-%{release}
Requires:	%{name}-plugin-bodhi = %{version}-%{release}
Requires:	libreport-plugin-bugzilla >= %{libreport_ver}
Requires:	libreport-plugin-logger >= %{libreport_ver}
Requires:	libreport-plugin-ureport >= %{libreport_ver}
Provides:	bug-buddy
Obsoletes:	bug-buddy < 2.33

%description desktop
Virtual package to make easy default installation on desktop
environments.

%description desktop -l pl.UTF-8
Wirtualny pakiet ułatwiający domyślną instalację w środowiskach
graficznych.

%package console-notification
Summary:	ABRT console notification script
Summary(pl.UTF-8):	Skrypt ABRT do powiadomień na konsoli
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description console-notification
A small script which prints a count of detected problems when someone
logs in to the shell.

%description console-notification -l pl.UTF-8
Mały skrypt wypisujący liczbę wykrytych problemów, kiedy ktoś loguje
się do powłoki.

%prep
%setup -q
%{?with_rpm5:%patch0 -p1}
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1

%{__sed} -n -e '/^%%changelog/,$p' abrt.spec.in | tail -n +2 > changelog

echo -n %{version} > abrt-version

%build
%{__libtoolize}
%{__gettextize}
%{__intltoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	AUGPARSE=/usr/bin/augparse \
	FINDMNT=/bin/findmnt \
	--enable-dump-time-unwind \
	--enable-native-unwinder \
	--disable-silent-rules \
	%{!?with_tests:--without-pythontests} \
	--with-systemdsystemunitdir=%{systemdunitdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	systemdsystemunitdir=%{systemdunitdir} \
	python3dir=%{py3_sitescriptdir}

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la

install -D %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/abrtd
install -d $RPM_BUILD_ROOT/var/cache/%{name}
install -d $RPM_BUILD_ROOT/var/cache/%{name}-di
install -d $RPM_BUILD_ROOT/var/run/%{name}

install -d $RPM_BUILD_ROOT%{systemdtmpfilesdir}
cat > $RPM_BUILD_ROOT%{systemdtmpfilesdir}/abrt.conf <<EOF
d /var/run/%{name} 0755 root root -
EOF

%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/problem/*.la
# examples
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/problem_examples
# packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_docdir}/abrt/README.md

# fool man verification - report_event.conf.5 belongs to libreport (NOTE: don't package it here)
touch $RPM_BUILD_ROOT%{_mandir}/man5/report_event.conf.5

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 248 abrt
%useradd -u 248 -g abrt -d /etc/abrt -s /sbin/nologin abrt

%post
/sbin/chkconfig --add abrtd
%service abrtd restart
%systemd_post abrtd.service

%preun
if [ "$1" = "0" ]; then
	%service abrtd stop
	/sbin/chkconfig --del abrtd
fi
%systemd_preun abrtd.service

%postun
if [ "$1" = "0" ]; then
	%userremove abrt
	%groupremove abrt
fi

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post addon-ccpp
%systemd_post abrt-ccpp.service
%systemd_post abrt-journal-core.service
%journal_catalog_update

%preun addon-ccpp
%systemd_preun abrt-ccpp.service
%systemd_preun abrt-journal-core.service

%post addon-kerneloops
%systemd_post abrt-oops.service
%journal_catalog_update

%preun addon-kerneloops
%systemd_preun abrt-oops.service

%post addon-pstoreoops
%systemd_post abrt-pstoreoops.service

%preun addon-pstoreoops
%systemd_preun abrt-pstoreoops.service

%post addon-python3
%journal_catalog_update

%post addon-upload-watch
%systemd_post abrt-upload-watch.service

%preun addon-upload-watch
%systemd_preun abrt-upload-watch.service

%post addon-vmcore
%systemd_post abrt-vmcore.service
%journal_catalog_update

%preun addon-vmcore
%systemd_preun abrt-vmcore.service

%post addon-xorg
%systemd_post abrt-xorg.service
%journal_catalog_update

%preun addon-xorg
%systemd_preun abrt-xorg.service

%post gui
%update_icon_cache hicolor

%postun gui
%update_icon_cache hicolor

%post	gui-libs -p /sbin/ldconfig
%postun	gui-libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGELOG.md README.md changelog
%attr(755,root,root) %{_bindir}/abrt
%attr(755,root,root) %{_bindir}/abrt-action-analyze-python
%attr(755,root,root) %{_bindir}/abrt-action-notify
%attr(755,root,root) %{_bindir}/abrt-action-save-package-data
%attr(755,root,root) %{_bindir}/abrt-handle-upload
%attr(755,root,root) %{_bindir}/abrt-watch-log
%attr(755,root,root) %{_sbindir}/abrt-auto-reporting
%attr(755,root,root) %{_sbindir}/abrt-server
%attr(755,root,root) %{_sbindir}/abrtd
%attr(755,root,root) %{_libexecdir}/abrt-action-coredump
%attr(755,root,root) %{_libexecdir}/abrt-action-generate-machine-id
%attr(755,root,root) %{_libexecdir}/abrt-action-save-container-data
%attr(755,root,root) %{_libexecdir}/abrt-action-ureport
%attr(755,root,root) %{_libexecdir}/abrt-handle-event
%{py3_sitescriptdir}/abrtcli
%dir %{_datadir}/%{name}
%{_datadir}/augeas/lenses/abrt.aug
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/abrt.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/abrt-action-save-package-data.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/gpg_keys.conf
%dir %{_sysconfdir}/%{name}/plugins
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libreport/events.d/abrt_event.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libreport/events.d/machine-id_event.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libreport/events.d/smart_event.conf
%attr(754,root,root) /etc/rc.d/init.d/abrtd
%{systemdunitdir}/abrtd.service
%attr(775,root,abrt) %dir /var/cache/%{name}
%dir /var/run/%{name}
%{systemdtmpfilesdir}/abrt.conf
%{_mandir}/man1/abrt.1*
%{_mandir}/man1/abrt-action-analyze-python.1*
%{_mandir}/man1/abrt-action-notify.1*
%{_mandir}/man1/abrt-action-save-package-data.1*
%{_mandir}/man1/abrt-auto-reporting.1*
%{_mandir}/man1/abrt-handle-upload.1*
%{_mandir}/man1/abrt-server.1*
%{_mandir}/man1/abrt-watch-log.1*
%{_mandir}/man5/abrt.conf.5*
%{_mandir}/man5/abrt-action-save-package-data.conf.5*
%{_mandir}/man5/abrt_event.conf.5*
%{_mandir}/man5/report_event.conf.5
%{_mandir}/man5/gpg_keys.conf.5*
%{_mandir}/man5/smart_event.conf.5*
%{_mandir}/man8/abrtd.8*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libabrt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libabrt.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libabrt.so
%dir %{_includedir}/abrt
%{_includedir}/abrt/abrt-dbus.h
%{_includedir}/abrt/hooklib.h
%{_includedir}/abrt/libabrt.h
%{_includedir}/abrt/problem_api.h
%{_pkgconfigdir}/abrt.pc

%files addon-ccpp
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/abrt-action-analyze-backtrace
%attr(755,root,root) %{_bindir}/abrt-action-analyze-c
%attr(755,root,root) %{_bindir}/abrt-action-analyze-ccpp-local
%attr(755,root,root) %{_bindir}/abrt-action-analyze-vulnerability
%attr(755,root,root) %{_bindir}/abrt-action-generate-backtrace
%attr(755,root,root) %{_bindir}/abrt-action-generate-core-backtrace
%attr(755,root,root) %{_bindir}/abrt-action-list-dsos
%attr(755,root,root) %{_bindir}/abrt-action-trim-files
%attr(755,root,root) %{_bindir}/abrt-dump-journal-core
%attr(755,root,root) %{_libexecdir}/abrt-gdb-exploitable
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/plugins/CCpp.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libreport/events.d/ccpp_event.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libreport/events.d/gconf_event.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libreport/events.d/vimrc_event.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libreport/plugins/catalog_journal_ccpp_format.conf
%attr(775,abrt,abrt) %dir %{_localstatedir}/cache/abrt-di
#%attr(754,root,root) /etc/rc.d/init.d/abrt-ccpp
%{_datadir}/libreport/events/analyze_CCpp.xml
%{_datadir}/libreport/events/analyze_LocalGDB.xml
%{_datadir}/libreport/events/collect_GConf.xml
%{_datadir}/libreport/events/collect_vimrc_system.xml
%{_datadir}/libreport/events/collect_vimrc_user.xml
%{_datadir}/libreport/events/collect_xsession_errors.xml
%{_datadir}/libreport/events/post_report.xml
%{systemdunitdir}/abrt-journal-core.service
%{_prefix}/lib/systemd/catalog/abrt_ccpp.catalog
%{_mandir}/man1/abrt-action-analyze-backtrace.1*
%{_mandir}/man1/abrt-action-analyze-c.1*
%{_mandir}/man1/abrt-action-analyze-ccpp-local.1*
%{_mandir}/man1/abrt-action-analyze-vulnerability.1*
%{_mandir}/man1/abrt-action-generate-backtrace.1*
%{_mandir}/man1/abrt-action-generate-core-backtrace.1*
%{_mandir}/man1/abrt-action-list-dsos.1*
%{_mandir}/man1/abrt-action-trim-files.1*
%{_mandir}/man1/abrt-dump-journal-core.1*
%{_mandir}/man5/abrt-CCpp.conf.5*
%{_mandir}/man5/ccpp_event.conf.5*
%{_mandir}/man5/gconf_event.conf.5*
%{_mandir}/man5/vimrc_event.conf.5*

%files addon-kerneloops
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/abrt-action-analyze-oops
%attr(755,root,root) %{_bindir}/abrt-action-check-oops-for-alt-component
%attr(755,root,root) %{_bindir}/abrt-action-check-oops-for-hw-error
%attr(755,root,root) %{_bindir}/abrt-dump-journal-oops
%attr(755,root,root) %{_bindir}/abrt-dump-oops
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libreport/events.d/koops_event.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libreport/plugins/catalog_koops_format.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/plugins/oops.conf
#%attr(754,root,root) /etc/rc.d/init.d/abrt-oops
%{systemdunitdir}/abrt-oops.service
%{_prefix}/lib/systemd/catalog/abrt_koops.catalog
%{_mandir}/man1/abrt-action-analyze-oops.1*
%{_mandir}/man1/abrt-action-check-oops-for-hw-error.1*
%{_mandir}/man1/abrt-dump-journal-oops.1*
%{_mandir}/man1/abrt-dump-oops.1*
%{_mandir}/man5/abrt-oops.conf.5*
%{_mandir}/man5/koops_event.conf.5*

%files addon-pstoreoops
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/abrt-merge-pstoreoops
%attr(755,root,root) %{_sbindir}/abrt-harvest-pstoreoops
%{systemdunitdir}/abrt-pstoreoops.service
#%attr(754,root,root) /etc/rc.d/init.d/abrt-pstoreoops
%{_mandir}/man1/abrt-harvest-pstoreoops.1*
%{_mandir}/man1/abrt-merge-pstoreoops.1*

%files addon-python3
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/plugins/python3.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libreport/events.d/python3_event.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libreport/plugins/catalog_python3_format.conf
%{py3_sitescriptdir}/abrt_exception_handler3.py*
%{py3_sitescriptdir}/abrt_exception_handler3_container.py*
%{py3_sitescriptdir}/abrt3.pth
%{py3_sitescriptdir}/abrt3_container.pth
%{py3_sitescriptdir}/__pycache__/abrt_exception_handler3*.cpython-*.py[co]
%{_prefix}/lib/systemd/catalog/python3_abrt.catalog
%{_mandir}/man5/python3_event.conf.5*
%{_mandir}/man5/python3-abrt.conf.5*

%files addon-upload-watch
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/abrt-upload-watch
%{systemdunitdir}/abrt-upload-watch.service
%{_mandir}/man1/abrt-upload-watch.1*

%files addon-vmcore
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/abrt-action-analyze-vmcore
%attr(755,root,root) %{_sbindir}/abrt-harvest-vmcore
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/plugins/vmcore.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libreport/events.d/vmcore_event.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libreport/plugins/catalog_vmcore_format.conf
#%attr(754,root,root) /etc/rc.d/init.d/abrt-vmcore
%{_datadir}/libreport/events/analyze_VMcore.xml
%{systemdunitdir}/abrt-vmcore.service
%{_prefix}/lib/systemd/catalog/abrt_vmcore.catalog
%{_mandir}/man1/abrt-action-analyze-vmcore.1*
%{_mandir}/man1/abrt-harvest-vmcore.1*
%{_mandir}/man5/abrt-vmcore.conf.5*
%{_mandir}/man5/vmcore_event.conf.5*

%files addon-xorg
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/abrt-action-analyze-xorg
%attr(755,root,root) %{_bindir}/abrt-dump-journal-xorg
%attr(755,root,root) %{_bindir}/abrt-dump-xorg
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/plugins/xorg.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libreport/events.d/xorg_event.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libreport/plugins/catalog_xorg_format.conf
#%attr(754,root,root) /etc/rc.d/init.d/abrt-xorg
%{systemdunitdir}/abrt-xorg.service
%{_prefix}/lib/systemd/catalog/abrt_xorg.catalog
%{_mandir}/man1/abrt-action-analyze-xorg.1*
%{_mandir}/man1/abrt-dump-journal-xorg.1*
%{_mandir}/man1/abrt-dump-xorg.1*
%{_mandir}/man5/abrt-xorg.conf.5*
%{_mandir}/man5/xorg_event.conf.5*

%files plugin-bodhi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/abrt-action-find-bodhi-update
%attr(755,root,root) %{_bindir}/abrt-bodhi
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libreport/events.d/bodhi_event.conf
%{_datadir}/libreport/events/analyze_BodhiUpdates.xml
%{_mandir}/man1/abrt-action-find-bodhi-update.1*
%{_mandir}/man1/abrt-bodhi.1*

%files dbus
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/abrt-dbus
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libreport/events.d/abrt_dbus_event.conf
/etc/dbus-1/system.d/dbus-abrt.conf
/etc/dbus-1/system.d/org.freedesktop.problems.daemon.conf
%{_datadir}/dbus-1/interfaces/org.freedesktop.Problems2.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Problems2.Entry.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Problems2.Session.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Problems2.Task.xml
%{_datadir}/dbus-1/system-services/org.freedesktop.problems.service
%{_datadir}/polkit-1/actions/abrt_polkit.policy
%{_mandir}/man8/abrt-dbus.8*
%{_docdir}/abrt-dbus-%{version}

%files python3
%defattr(644,root,root,755)
%dir %{py3_sitedir}/problem
%attr(755,root,root) %{py3_sitedir}/problem/_py3abrt.so
%{py3_sitedir}/problem/*.py*
%{py3_sitedir}/problem/__pycache__
%{_mandir}/man5/python3-abrt.5*

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/abrt-applet
%attr(755,root,root) %{_bindir}/system-config-abrt
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/ui
%{_iconsdir}/hicolor/scalable/apps/abrt.svg
%{_iconsdir}/hicolor/symbolic/apps/abrt-symbolic.svg
%{_sysconfdir}/xdg/autostart/org.freedesktop.problems.applet.desktop
%{_datadir}/dbus-1/services/org.freedesktop.problems.applet.service
%{_mandir}/man1/abrt-applet.1*
%{_mandir}/man1/system-config-abrt.1*

%files gui-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libabrt_gui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libabrt_gui.so.0

%files gui-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libabrt_gui.so
%{_includedir}/abrt/abrt-config-widget.h
%{_includedir}/abrt/system-config-abrt.h
%{_pkgconfigdir}/abrt_gui.pc

%files desktop
%defattr(644,root,root,755)

%files console-notification
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) /etc/profile.d/abrt-console-notification.sh
