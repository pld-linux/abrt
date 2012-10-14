Summary:	Automatic bug detection and reporting tool
Name:		abrt
Version:	2.0.15
Release:	0.1
License:	GPL v2+
Group:		Applications/System
URL:		https://fedorahosted.org/abrt/
Source0:	https://fedorahosted.org/released/abrt/%{name}-%{version}.tar.gz
# Source0-md5:	0ac147b6e43ca873e6b1927601ec22a4
Source1:	%{name}.init
Patch0:		%{name}-rpm5.patch
Patch2:		rpmkey-pld.patch
Patch3:		format_security.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	bzip2-devel
BuildRequires:	curl-devel
BuildRequires:	dbus-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel
BuildRequires:	intltool
BuildRequires:	libmagic-devel
BuildRequires:	libnotify-devel
BuildRequires:	libtar-devel
BuildRequires:	libtool
BuildRequires:	libzip-devel
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	rpm-devel >= 4.5-28
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sqlite3-devel
BuildRequires:	xmlrpc-c-client
BuildRequires:	xmlrpc-c-devel >= 1.20.3-1
BuildRequires:	zlib-devel
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires:	%{name}-libs = %{version}-%{release}
Provides:	group(abrt)
Provides:	user(abrt)
Obsoletes:	abrt-plugin-sqlite3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
abrt is a tool to help users to detect defects in applications and to
create a bug report with all informations needed by maintainer to fix
it. It uses plugin system to extend its functionality.

%package libs
Summary:	Libraries for abrt
Group:		Libraries

%description libs
Libraries for %{name}.

%package devel
Summary:	Development libraries for abrt
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Development libraries and headers for %{name}.

%package gui
Summary:	abrt's gui
Group:		X11/Applications
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	%{name} = %{version}-%{release}
Requires:	python-dbus
Requires:	python-gnome-desktop-keyring
Requires:	python-gnome-vfs
Requires:	python-pygtk-glade
Requires:	python-pygtk-gtk
# only if gtk2 version < 2.17
#Requires: python-sexy
Provides:	abrt-applet = %{version}-%{release}
Obsoletes:	abrt-applet < 0.0.5
Conflicts:	abrt-applet < 0.0.5

%description gui
GTK+ wizard for convenient bug reporting.

%package addon-ccpp
Summary:	abrt's C/C++ addon
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	elfutils
Requires:	yum-utils

%description addon-ccpp
This package contains hook for C/C++ crashed programs and abrt's C/C++
analyzer plugin.

%package addon-kerneloops
Summary:	abrt's kerneloops addon
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	curl
Obsoletes:	abrt-plugin-kerneloops
Obsoletes:	abrt-plugin-kerneloopsreporter
Obsoletes:	kerneloops

%description addon-kerneloops
This package contains plugin for collecting kernel crash information
and reporter plugin which sends this information to specified server,
usually to kerneloops.org.

%package plugin-rhfastcheck
Summary:	%{name}'s rhfastcheck plugin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plugin-rhfastcheck
Plugin to quickly check RH support DB for known solution.

%package plugin-rhticket
Summary:	%{name}'s rhticket plugin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plugin-rhticket
Plugin to report bugs into RH support system.

%package plugin-logger
Summary:	abrt's logger reporter plugin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plugin-logger
The simple reporter plugin which writes a report to a specified file.

%package plugin-mailx
Summary:	abrt's mailx reporter plugin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	mailx

%description plugin-mailx
The simple reporter plugin which sends a report via mailx to a
specified email.

%package plugin-runapp
Summary:	abrt's runapp plugin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plugin-runapp
Plugin to run external programs.

%package plugin-sosreport
Summary:	abrt's sosreport plugin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	sosreport

%description plugin-sosreport
Plugin to include an sosreport in an abrt report.

%package plugin-bugzilla
Summary:	abrt's bugzilla plugin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plugin-bugzilla
Plugin to report bugs into the bugzilla.

%package plugin-catcut
Summary:	abrt's catcut plugin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plugin-catcut
Plugin to report bugs into the catcut.

%package plugin-ticketuploader
Summary:	abrt's ticketuploader plugin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plugin-ticketuploader
Plugin to report bugs into anonymous FTP site associated with
ticketing system.

%package plugin-filetransfer
Summary:	abrt's File Transfer plugin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plugin-filetransfer
Plugin to uploading files to a server.

%package addon-python
Summary:	abrt's addon for catching and analyzing Python exceptions
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description addon-python
This package contains python hook and python analyzer plugin for
handling uncaught exception in python programs.

%package cli
Summary:	abrt's command line interface
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
# analyzers
Requires:	%{name}-addon-ccpp
Requires:	%{name}-addon-kerneloops
Requires:	%{name}-addon-python
# reporters
Requires:	%{name}-plugin-logger
Requires:	%{name}-plugin-runapp

%description cli
This package contains simple command line client for controling abrt
daemon over the sockets.

%package desktop
Summary:	Virtual package to install all necessary packages for usage from desktop environment
Group:		X11/Applications
# This package gets installed when anything requests bug-buddy -
# happens when users upgrade Fn to Fn+1;
# or if user just wants "typical desktop installation".
# Installing abrt-desktop should result in the abrt which works without
# any tweaking in abrt.conf (IOW: all plugins mentioned there must be installed)
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-addon-ccpp = %{version}-%{release}
Requires:	%{name}-addon-kerneloops = %{version}-%{release}
Requires:	%{name}-addon-python = %{version}-%{release}
# Default config of addon-ccpp requires gdb
Requires:	%{name}-gui
Requires:	%{name}-plugin-logger
Requires:	%{name}-plugin-runapp
Requires:	gdb >= 7.0-3
Provides:	bug-buddy
Obsoletes:	bug-buddy

%description desktop
Virtual package to make easy default installation on desktop
environments.

%prep
%setup -q
%patch0 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-systemdsystemunitdir=%{systemdunitdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%py_postclean

# remove all .la files
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/lib*.la $RPM_BUILD_ROOT%{_libdir}/lib*.la

install -d $RPM_BUILD_ROOT/etc/rc.d/init.d
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/abrtd
install -d $RPM_BUILD_ROOT/var/cache/%{name}
install -d $RPM_BUILD_ROOT/var/cache/%{name}-di
install -d $RPM_BUILD_ROOT/var/run/%{name}

cp -a src/Gui/abrt.desktop $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
cp -a src/Applet/%{name}-applet.desktop $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart

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

%post gui
%update_icon_cache hicolor

%postun gui
%update_icon_cache hicolor

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/abrtd
%attr(755,root,root) %{_bindir}/%{name}-debuginfo-install
%attr(755,root,root) %{_bindir}/%{name}-backtrace
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/gpg_keys
/etc/dbus-1/system.d/dbus-%{name}.conf
%attr(754,root,root) /etc/rc.d/init.d/abrtd
%dir %attr(775,root,abrt) /var/cache/%{name}
%dir /var/run/%{name}
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/plugins
%dir %{_libdir}/%{name}
%{_mandir}/man1/%{name}-backtrace.1*
%{_mandir}/man8/abrtd.8*
%{_mandir}/man5/%{name}.conf.5*
%{_mandir}/man7/%{name}-plugins.7*
%{_datadir}/polkit-1/actions/org.fedoraproject.abrt.policy
%{_datadir}/dbus-1/system-services/com.redhat.abrt.service

# plugin-sqlite3
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/plugins/SQLite3.conf
%attr(755,root,root) %{_libdir}/%{name}/libSQLite3.so
%{_mandir}/man7/%{name}-SQLite3.7*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libABRTUtils.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libABRTUtils.so.0
%attr(755,root,root) %{_libdir}/libABRTdUtils.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libABRTdUtils.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libABRTUtils.so
%attr(755,root,root) %{_libdir}/libABRTdUtils.so

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-gui
%dir %{_datadir}/%{name}
# all glade, gtkbuilder and py files for gui
%{_datadir}/%{name}/*.py*
%{_datadir}/%{name}/*.glade
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/*
# XXX ... should be in hicolor dir?
%dir %{_datadir}/%{name}/icons
%dir %{_datadir}/%{name}/icons/hicolor
%dir %{_datadir}/%{name}/icons/hicolor/*
%dir %{_datadir}/%{name}/icons/hicolor/*/status
%{_datadir}/%{name}/icons/hicolor/*/status/*.png
%attr(755,root,root) %{_bindir}/%{name}-applet
%{_sysconfdir}/xdg/autostart/%{name}-applet.desktop

%files addon-ccpp
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/plugins/CCpp.conf
%attr(755,root,root) %{_libdir}/%{name}/libCCpp.so
%attr(755,root,root) %{_libexecdir}/abrt-hook-ccpp
%dir %{_localstatedir}/cache/%{name}-di

%files addon-kerneloops
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/plugins/Kerneloops.conf
%attr(755,root,root) %{_bindir}/dumpoops
%attr(755,root,root) %{_libdir}/%{name}/libKerneloops.so
%attr(755,root,root) %{_libdir}/%{name}/libKerneloopsScanner.so
%attr(755,root,root) %{_libdir}/%{name}/libKerneloopsReporter.so
%{_libdir}/%{name}/KerneloopsReporter.GTKBuilder
%{_mandir}/man7/%{name}-KerneloopsScanner.7*
%{_mandir}/man7/%{name}-KerneloopsReporter.7*

%files plugin-logger
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/plugins/Logger.conf
%attr(755,root,root) %{_libdir}/%{name}/libLogger.so
%{_libdir}/%{name}/Logger.GTKBuilder
%{_mandir}/man7/%{name}-Logger.7*

%files plugin-mailx
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/plugins/Mailx.conf
%attr(755,root,root) %{_libdir}/%{name}/libMailx.so
%{_libdir}/%{name}/Mailx.GTKBuilder
%{_mandir}/man7/%{name}-Mailx.7*

%files plugin-runapp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libRunApp.so
%{_mandir}/man7/%{name}-RunApp.7*

%files plugin-sosreport
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/plugins/SOSreport.conf
%attr(755,root,root) %{_libdir}/%{name}/libSOSreport.so

%files plugin-bugzilla
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/plugins/Bugzilla.conf
%attr(755,root,root) %{_libdir}/%{name}/libBugzilla.so
%{_libdir}/%{name}/Bugzilla.GTKBuilder
%{_mandir}/man7/%{name}-Bugzilla.7*

%files plugin-rhfastcheck
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/librhfastcheck.so

%files plugin-rhticket
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/librhticket.so

%files plugin-catcut
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/plugins/Catcut.conf
%attr(755,root,root) %{_libdir}/%{name}/libCatcut.so
%{_libdir}/%{name}/Catcut.GTKBuilder
#%{_mandir}/man7/%{name}-Catcut.7*

%files plugin-ticketuploader
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/plugins/TicketUploader.conf
%attr(755,root,root) %{_libdir}/%{name}/libTicketUploader.so
%{_libdir}/%{name}/TicketUploader.GTKBuilder
%{_mandir}/man7/%{name}-TicketUploader.7*

%files plugin-filetransfer
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/plugins/FileTransfer.conf
%attr(755,root,root) %{_libdir}/%{name}/libFileTransfer.so
%{_mandir}/man7/%{name}-FileTransfer.7*

%files addon-python
%defattr(644,root,root,755)
%attr(4755,abrt,abrt) %{_libexecdir}/abrt-hook-python
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/plugins/Python.conf
%attr(755,root,root) %{_libdir}/%{name}/libPython.so
%{py_sitescriptdir}/*.py[co]
%{py_sitescriptdir}/abrt.pth

%files cli
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/abrt-cli
%{_mandir}/man1/abrt-cli.1*
/etc/bash_completion.d/abrt-cli.bash

%files desktop
%defattr(644,root,root,755)
