#
# TODO:
# - handle obsolete packages: abrt-plugin-{catcut,rhfastcheck,rhticket,ticketuploader}
# - SysV init scripts for -addon-ccpp, -addon-kerneloops, -addon-uefioops, -addon-vmcore, -addon-xorg
Summary:	Automatic bug detection and reporting tool
Summary(pl.UTF-8):	Narzędzie do automatycznego wykrywania i zgłaszania błędów
Name:		abrt
Version:	2.1.6
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	https://fedorahosted.org/released/abrt/%{name}-%{version}.tar.gz
# Source0-md5:	7a8d16a6f316528a767e6be93164e688
Source1:	%{name}.init
Patch0:		%{name}-rpm5.patch
Patch1:		%{name}-rpm45.patch
Patch2:		rpmkey-pld.patch
Patch3:		format_security.patch
Patch4:		%{name}-link.patch
URL:		https://fedorahosted.org/abrt/
BuildRequires:	asciidoc
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dbus-devel
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	glib2-devel >= 1:2.21
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	json-c-devel
BuildRequires:	libmagic-devel
BuildRequires:	libnotify-devel
BuildRequires:	libreport-devel >= 2.1.6
BuildRequires:	libreport-gtk-devel >= 2.1.6
BuildRequires:	libreport-web-devel >= 2.1.6
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2
BuildRequires:	rpm-devel >= 4.5
BuildRequires:	nss-devel
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	rpm-devel >= 4.5-28
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	satyr-devel
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
Obsoletes:	abrt-plugin-filetransfer
Obsoletes:	abrt-plugin-runapp
Obsoletes:	abrt-plugin-sosreport
Obsoletes:	abrt-plugin-sqlite3
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

%description libs
ABRT shared library.

%description libs -l pl.UTF-8
Biblioteka współdzielona ABRT.

%package devel
Summary:	Header files for ABRT livrary
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotekia ABRT
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for ABRT livrary.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotekia ABRT.

%package addon-ccpp
Summary:	ABRT's C/C++ addon
Summary(pl.UTF-8):	Dodatek C/C++ do ABRT
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-retrace-client = %{version}-%{release}
Requires:	cpio
Requires:	elfutils
Requires:	gdb >= 7.0-3
Requires:	satyr
Requires:	yum-utils

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
Requires:	libreport-plugin-kerneloops >= 2.1.6
Obsoletes:	abrt-plugin-kerneloops
Obsoletes:	abrt-plugin-kerneloopsreporter
Obsoletes:	kerneloops

%description addon-kerneloops
This package contains plugin for collecting kernel crash information
from system log.

%description addon-kerneloops -l pl.UTF-8
Ten pakiet zawiera wtyczkę do zbierania informacji o awarii jądra z
logu systemowego.

%package addon-python
Summary:	ABRT's addon for catching and analyzing Python exceptions
Summary(pl.UTF-8):	Dodatek ABRT do przechwytywania i analizy wyjątków Pythona
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	gnome-python2-bugbuddy

%description addon-python
This package contains Python hook and Python analyzer plugin for
handling uncaught exception in Python programs.

%description addon-python -l pl.UTF-8
Ten pakiet zawiera pythonowy punkt zaczepienia oraz wtyczkę
analizatora Pythona do obsługi nie obsłużonych wyjątków w programach w
Pythonie.

%package addon-uefioops
Summary:	ABRT's uefioops addon
Summary(pl.UTF-8):	Dodatek uefioops do ABRT
Group:		Libraries
Requires:	%{name}-addon-kerneloops = %{version}-%{release}

%description addon-uefioops
This package contains plugin for collecting kernel oopses from UEFI
storage.

%description addon-uefioops -l pl.UTF-8
Ten pakiet zawiera wtyczkę do zbierania oopsów jądra z danych UEFI.

%package addon-vmcore
Summary:	ABRT's vmcore addon
Summary(pl.UTF-8):	Dodatek vmcore do ABRT
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-addon-kerneloops = %{version}-%{release}
# not available in PLD
#Requires:	crash

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
Requires:	libreport-web >= 2.1.6
Obsoletes:	libreport-plugin-bodhi

%description plugin-bodhi
Plugin to search for a new updates in bodhi server.

%description plugin-bodhi -l pl.UTF-8
Wtyczka do wyszukiwania nowych uaktualnień na serwerze bodhi.

%package retrace-client
Summary:	ABRT's retrace client
Summary(pl.UTF-8):	Klient Retrace dla ABRT
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xz

%description retrace-client
This package contains the client application for Retrace server which
is able to analyze C/C++ crashes remotely.

%description retrace-client -l pl.UTF-8
Ten pakiet zawiera aplikację kliencką dla serwera Retrace, który
potrafi zdalnie przeanalizować awarię programu w C/C++.

%package dbus
Summary:	ABRT DBus service
Summary(pl.UTF-8):	Usługa DBus ABRT
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	libreport >= 2.1.6

%description dbus
ABRT DBus service which provides org.freedesktop.problems API on DBus
and uses PolicyKit to authorize to access the problem data.

%description dbus -l pl.UTF-8
Usługa DBus ABRT, udostępniająca poprzez DBus API
org.freedesktop.problems, używająca PolicyKit do autoryzacji dostępu
do danych o problemach.

%package python
Summary:	ABRT Python API
Summary(pl.UTF-8):	API Pythona do ABRT
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5.0"
BuildArch:	noarch
%endif

%description python
High-level API for querying, creating and manipulating problems
handled by ABRT in Python.

%description python -l pl.UTF-8
Wysokopoziomowe API do odpytywania, tworzenia i obróbki z poziomu
Pythona problemów obsługiwanych przez ABRT.

%package cli
Summary:	ABRT's command line interface
Summary(pl.UTF-8):	Interfejs linii poleceń ABRT
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
# analyzers
Requires:	%{name}-addon-ccpp = %{version}-%{release}
Requires:	%{name}-addon-kerneloops = %{version}-%{release}
Requires:	%{name}-addon-python = %{version}-%{release}
Requires:	%{name}-addon-uefioops = %{version}-%{release}
# reporters
Requires:	libreport-plugin-bugzilla >= 2.1.6
Requires:	libreport-plugin-logger >= 2.1.6

%description cli
This package contains simple command line client for controling ABRT
daemon over the sockets.

%description cli -l pl.UTF-8
Ten pakiet zawiera prostego klienta obsługiwanego z linii poleceń,
pozwalającego na sterowanie demonem poprzez gniazda.

%package gui
Summary:	ABRT's GUI
Summary(pl.UTF-8):	Graficzny interfejs użytkownika do ABRT
Group:		X11/Applications
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-dbus = %{version}-%{release}
Suggests:	gnome-abrt
Provides:	abrt-applet = %{version}-%{release}
Obsoletes:	abrt-applet < 0.0.5
Conflicts:	abrt-applet < 0.0.5

%description gui
GTK+ wizard for convenient bug reporting.

%description gui -l pl.UTF-8
Oparty na GTK+ kreator do wygodnego zgłaszania błędów.

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
Requires:	%{name}-addon-python = %{version}-%{release}
Requires:	%{name}-addon-uefioops = %{version}-%{release}
Requires:	%{name}-addon-vmcore = %{version}-%{release}
Requires:	%{name}-addon-xorg = %{version}-%{release}
Requires:	%{name}-gui = %{version}-%{release}
Requires:	%{name}-plugin-bodhi = %{version}-%{release}
Requires:	%{name}-retrace-client = %{version}-%{release}
Requires:	libreport-plugin-bugzilla >= 2.1.6
Requires:	libreport-plugin-logger >= 2.1.6
Requires:	libreport-plugin-ureport >= 2.1.6
Provides:	bug-buddy
Obsoletes:	bug-buddy

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
Requires:	%{name}-cli = %{version}-%{release}

%description console-notification
A small script which prints a count of detected problems when someone
logs in to the shell.

%description console-notification -l pl.UTF-8
Mały skrypt wypisujący liczbę wykrytych problemów, kiedy ktoś loguje
się do powłoki.

%prep
%setup -q
%if "%{_rpmversion}" >= "5.0"
%patch0 -p1
%else
%patch1 -p1
%endif
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--with-systemdsystemunitdir=%{systemdunitdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la

install -D %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/abrtd
install -d $RPM_BUILD_ROOT/var/cache/%{name}
install -d $RPM_BUILD_ROOT/var/cache/%{name}-di
install -d $RPM_BUILD_ROOT/var/run/%{name}

install -d $RPM_BUILD_ROOT/usr/lib/tmpfiles.d
cat >$RPM_BUILD_ROOT/usr/lib/tmpfiles.d/abrt.conf <<EOF
/var/run/%{name} 0755 root root -
EOF

# API not exported
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libabrtconfigui.so
# outdated copy of lt
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/lt_LT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 248 abrt
%useradd -u 248 -g abrt -d /etc/abrt -s /sbin/nologin abrt

%post
/sbin/chkconfig --add abrtd
%service abrtd restart

%preun
if [ "$1" = "0" ]; then
	%service abrtd stop
	/sbin/chkconfig --del abrtd
fi

%postun
if [ "$1" = "0" ]; then
	%userremove abrt
	%groupremove abrt
fi

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post gui
/sbin/ldconfig
%update_icon_cache hicolor

%postun gui
/sbin/ldconfig
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/abrt-action-save-package-data
%attr(755,root,root) %{_bindir}/abrt-handle-upload
%attr(755,root,root) %{_bindir}/abrt-watch-log
%attr(755,root,root) %{_sbindir}/abrt-server
%attr(755,root,root) %{_sbindir}/abrtd
%attr(755,root,root) %{_libexecdir}/abrt-action-ureport
%attr(755,root,root) %{_libexecdir}/abrt-handle-event
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/abrt.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/abrt-action-save-package-data.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/gpg_keys
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/xorg.conf
%dir %{_sysconfdir}/%{name}/plugins
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libreport/events.d/abrt_event.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libreport/events.d/smart_event.conf
%attr(754,root,root) /etc/rc.d/init.d/abrtd
%{systemdunitdir}/abrtd.service
%attr(775,root,abrt) %dir /var/cache/%{name}
%dir /var/run/%{name}
/usr/lib/tmpfiles.d/abrt.conf
%{_mandir}/man1/abrt-action-save-package-data.1*
%{_mandir}/man1/abrt-handle-upload.1*
%{_mandir}/man1/abrt-server.1*
%{_mandir}/man1/abrt-watch-log.1*
%{_mandir}/man5/abrt.conf.5*
%{_mandir}/man5/abrt-action-save-package-data.conf.5*
%{_mandir}/man8/abrtd.8*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libabrt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libabrt.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libabrt.so
%{_includedir}/abrt
%{_pkgconfigdir}/abrt.pc

%files addon-ccpp
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/abrt-action-analyze-backtrace
%attr(755,root,root) %{_bindir}/abrt-action-analyze-c
%attr(755,root,root) %{_bindir}/abrt-action-analyze-ccpp-local
%attr(755,root,root) %{_bindir}/abrt-action-analyze-core
%attr(755,root,root) %{_bindir}/abrt-action-analyze-vulnerability
%attr(755,root,root) %{_bindir}/abrt-action-generate-backtrace
%attr(755,root,root) %{_bindir}/abrt-action-generate-core-backtrace
%attr(755,root,root) %{_bindir}/abrt-action-install-debuginfo
%attr(755,root,root) %{_bindir}/abrt-action-list-dsos
%attr(755,root,root) %{_bindir}/abrt-action-perform-ccpp-analysis
%attr(755,root,root) %{_bindir}/abrt-action-trim-files
%attr(755,root,root) %{_bindir}/abrt-dedup-client
%attr(755,root,root) %{_sbindir}/abrt-install-ccpp-hook
%attr(6755,abrt,abrt) %{_libexecdir}/abrt-action-install-debuginfo-to-abrt-cache
%attr(755,root,root) %{_libexecdir}/abrt-gdb-exploitable
%attr(755,root,root) %{_libexecdir}/abrt-hook-ccpp
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/plugins/CCpp.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libreport/events.d/ccpp_event.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libreport/events.d/gconf_event.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libreport/events.d/vimrc_event.conf
%attr(775,abrt,abrt) %dir %{_localstatedir}/cache/abrt-di
#%attr(754,root,root) /etc/rc.d/init.d/abrt-ccpp
%{_datadir}/libreport/events/analyze_CCpp.xml
%{_datadir}/libreport/events/analyze_LocalGDB.xml
%{_datadir}/libreport/events/collect_GConf.xml
%{_datadir}/libreport/events/collect_vimrc_system.xml
%{_datadir}/libreport/events/collect_vimrc_user.xml
%{_datadir}/libreport/events/collect_xsession_errors.xml
%{_datadir}/libreport/events/post_report.xml
%{systemdunitdir}/abrt-ccpp.service
%{_mandir}/man1/abrt-action-analyze-backtrace.1*
%{_mandir}/man1/abrt-action-analyze-c.1*
%{_mandir}/man1/abrt-action-analyze-ccpp-local.1*
%{_mandir}/man1/abrt-action-analyze-core.1*
%{_mandir}/man1/abrt-action-analyze-vulnerability.1*
%{_mandir}/man1/abrt-action-generate-backtrace.1*
%{_mandir}/man1/abrt-action-generate-core-backtrace.1*
%{_mandir}/man1/abrt-action-install-debuginfo.1*
%{_mandir}/man1/abrt-action-list-dsos.1*
%{_mandir}/man1/abrt-action-perform-ccpp-analysis.1*
%{_mandir}/man1/abrt-action-trim-files.1*
%{_mandir}/man1/abrt-dedup-client.1*
%{_mandir}/man1/abrt-install-ccpp-hook.1*

%files addon-kerneloops
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/abrt-action-analyze-oops
%attr(755,root,root) %{_bindir}/abrt-action-save-kernel-data
%attr(755,root,root) %{_bindir}/abrt-dump-oops
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libreport/events.d/koops_event.conf
#%attr(754,root,root) /etc/rc.d/init.d/abrt-oops
%{systemdunitdir}/abrt-oops.service
%{_mandir}/man1/abrt-action-analyze-oops.1*
%{_mandir}/man1/abrt-action-save-kernel-data.1*
%{_mandir}/man1/abrt-dump-oops.1*

%files addon-python
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/abrt-action-analyze-python
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/plugins/python.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libreport/events.d/python_event.conf
%{py_sitedir}/abrt_exception_handler.py[co]
%{py_sitedir}/abrt.pth
%{_mandir}/man1/abrt-action-analyze-python.1*

%files addon-uefioops
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/abrt-merge-uefioops
%attr(755,root,root) %{_sbindir}/abrt-harvest-uefioops
#%attr(754,root,root) /etc/rc.d/init.d/abrt-uefioops
%{systemdunitdir}/abrt-uefioops.service
%{_mandir}/man1/abrt-harvest-uefioops.1*
%{_mandir}/man1/abrt-merge-uefioops.1*

%files addon-vmcore
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/abrt-action-analyze-vmcore
%attr(755,root,root) %{_sbindir}/abrt-harvest-vmcore
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/abrt-harvest-vmcore.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libreport/events.d/vmcore_event.conf
#%attr(754,root,root) /etc/rc.d/init.d/abrt-vmcore
%{_datadir}/libreport/events/analyze_VMcore.xml
%{systemdunitdir}/abrt-vmcore.service
%{_mandir}/man1/abrt-action-analyze-vmcore.1*
%{_mandir}/man1/abrt-harvest-vmcore.1*

%files addon-xorg
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/abrt-action-analyze-xorg
%attr(755,root,root) %{_bindir}/abrt-dump-xorg
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libreport/events.d/xorg_event.conf
#%attr(754,root,root) /etc/rc.d/init.d/abrt-xorg
%{systemdunitdir}/abrt-xorg.service
%{_mandir}/man1/abrt-action-analyze-xorg.1*
%{_mandir}/man1/abrt-dump-xorg.1*

%files plugin-bodhi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/abrt-bodhi
%{_mandir}/man1/abrt-bodhi.1*

%files retrace-client
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libreport/events.d/ccpp_retrace_event.conf
%attr(755,root,root) %{_bindir}/abrt-retrace-client
%{_datadir}/libreport/events/analyze_RetraceServer.xml
%{_mandir}/man1/abrt-retrace-client.1*

%files dbus
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/abrt-dbus
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libreport/events.d/dbus_event.conf
/etc/dbus-1/system.d/dbus-abrt.conf
%{_datadir}/dbus-1/interfaces/org.freedesktop.Problems.xml
%{_datadir}/dbus-1/system-services/org.freedesktop.problems.service
%{_datadir}/polkit-1/actions/abrt_polkit.policy
%{_mandir}/man8/abrt-dbus.8*
%{_docdir}/abrt-dbus-%{version}

%files python
%defattr(644,root,root,755)
%{py_sitescriptdir}/problem
%{_mandir}/man5/abrt-python.5*
%{_docdir}/abrt-python-%{version}

%files cli
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/abrt-cli
%{_mandir}/man1/abrt-cli.1*

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/abrt-applet
%attr(755,root,root) %{_bindir}/system-config-abrt
%attr(755,root,root) %{_libdir}/libabrtconfigui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libabrtconfigui.so.0
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/icons
%{_datadir}/%{name}/ui
%{_desktopdir}/system-config-abrt.desktop
%{_iconsdir}/hicolor/*/apps/abrt.png
%{_iconsdir}/hicolor/*/status/abrt.png
%{_sysconfdir}/xdg/autostart/abrt-applet.desktop
%{_mandir}/man1/abrt-applet.1*
%{_mandir}/man1/system-config-abrt.1*

%files desktop
%defattr(644,root,root,755)

%files console-notification
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/profile.d/abrt-console-notification.sh
