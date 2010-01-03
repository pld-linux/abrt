# TODO
# - fixes to get working with jbj rpm
Summary:	Automatic bug detection and reporting tool
Name:		abrt
Version:	1.0.0
Release:	0.3
License:	GPL v2+
Group:		Applications/System
URL:		https://fedorahosted.org/abrt/
#Source0:	http://jmoskovc.fedorapeople.org/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	62a8a6a1d7712472133b97b38469683e
Source1:	%{name}.init
Patch0:		%{name}-rpm.patch
BuildRequires:	bzip2-devel
BuildRequires:	curl-devel
BuildRequires:	dbus-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	gtk+2-devel
BuildRequires:	intltool
BuildRequires:	libmagic-devel
BuildRequires:	libnotify-devel
BuildRequires:	libtar-devel
BuildRequires:	libzip-devel
BuildRequires:	nss-devel
BuildRequires:	polkit-devel
BuildRequires:	python-devel
BuildRequires:	rpm-devel >= 4.5-28
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sqlite3-devel
BuildRequires:	xmlrpc-c-devel >= 1.20.3-1
BuildRequires:	zlib-devel
Requires(postun):	/usr/sbin/groupdel
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires:	%{name}-libs = %{version}-%{release}
Provides:	group(abrt)
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
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-python
Requires:	gnome-python2-gnomekeyring
Requires:	gnome-python2-gnomevfs
Requires:	pygtk2-libglade
Requires:	python-pygtk
# only if gtk2 version < 2.17
#Requires: python-sexy
Provides:	abrt-applet = %{version}-%{release}
Provides:	bug-buddy
Obsoletes:	abrt-applet < 0.0.5
Obsoletes:	bug-buddy
Obsoletes:	bug-buddy
Conflicts:	abrt-applet < 0.0.5

%description gui
GTK+ wizard for convenient bug reporting.

%package addon-ccpp
Summary:	abrt's C/C++ addon
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	elfutils
Requires:	gdb >= 7.0-3
Requires:	yum-utils

%description addon-ccpp
This package contains hook for C/C++ crashed programs and abrt's C/C++
analyzer plugin.

%package plugin-firefox
Summary:	abrt's Firefox analyzer plugin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	elfutils
Requires:	gdb >= 7.0-3
Requires:	yum-utils

%description plugin-firefox
This package contains hook for Firefox

%package addon-kerneloops
Summary:	abrt's kerneloops addon
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-plugin-kerneloopsreporter = %{version}-%{release}
Obsoletes:	abrt-plugin-kerneloops
Obsoletes:	kerneloops

%description addon-kerneloops
This package contains plugins for kernel crashes information
collecting.

%package plugin-kerneloopsreporter
Summary:	abrt's kerneloops reporter plugin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	curl

%description plugin-kerneloopsreporter
This package contains reporter plugin, that sends, collected by abrt's
kerneloops addon, information about kernel crashes to specified
server, e.g. kerneloops.org.

%package plugin-sqlite3
Summary:	abrt's SQLite3 database plugin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plugin-sqlite3
This package contains SQLite3 database plugin. It is used for storing
the data required for creating a bug report.

%package plugin-logger
Summary:	abrt's logger reporter plugin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plugin-logger
The simple reporter plugin, which writes a report to a specified file.

%package plugin-mailx
Summary:	abrt's mailx reporter plugin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	mailx

%description plugin-mailx
The simple reporter plugin, which sends a report via mailx to a
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
Requires:	sos

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
hadnling uncaught exception in python programs.

%package cli
Summary:	abrt's command line interface
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description cli
This package contains simple command line client for controling abrt
daemon over the sockets.

%package desktop
Summary:	Virtual package to install all necessary packages for usage from desktop environment
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-addon-ccpp = %{version}-%{release}
Requires:	%{name}-addon-kerneloops = %{version}-%{release}
Requires:	%{name}-addon-python = %{version}-%{release}
Requires:	%{name}-plugin-bugzilla = %{version}-%{release}
#Requires:	%{name}-plugin-firefox = %{version}-%{release}
Requires:	%{name}-plugin-logger = %{version}-%{release}
Requires:	%{name}-plugin-sqlite3 = %{version}-%{release}

%description desktop
Virtual package to make easy default instalation on desktop
environments.

%prep
%setup -q
%patch0 -p1

%build
%configure
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	mandir=%{_mandir} \
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
%groupadd -g 182 abrt

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
	%groupremove abrt
fi

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/abrtd
%attr(755,root,root) %{_bindir}/%{name}-debuginfo-install
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
/etc/dbus-1/system.d/dbus-%{name}.conf
%attr(754,root,root) /etc/rc.d/init.d/abrtd
%dir %attr(775,root,abrt) /var/cache/%{name}
%dir /var/cache/%{name}-di
%dir /var/run/%{name}
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/plugins
%dir %{_libdir}/%{name}
%{_mandir}/man8/abrtd.8*
%{_mandir}/man5/%{name}.conf.5*
%{_mandir}/man7/%{name}-plugins.7*
%{_mandir}/man5/pyhook.conf.5*
%{_datadir}/polkit-1/actions/org.fedoraproject.abrt.policy
%{_datadir}/dbus-1/system-services/com.redhat.abrt.service

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libABRTUtils.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libABRTUtils.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libABRTUtils.so

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-gui
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/abrt.png
%{_iconsdir}/hicolor/48x48/apps/*.png
%attr(755,root,root) %{_bindir}/%{name}-applet
%{_sysconfdir}/xdg/autostart/%{name}-applet.desktop

%files addon-ccpp
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/%{name}/plugins/CCpp.conf
%attr(755,root,root) %{_libdir}/%{name}/libCCpp.so
%attr(755,root,root) %{_libexecdir}/hookCCpp

#%files plugin-firefox
#%{_libdir}/%{name}/libFirefox.so*

%files addon-kerneloops
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/%{name}/plugins/Kerneloops.conf
%config(noreplace) %{_sysconfdir}/%{name}/plugins/KerneloopsScanner.conf
%attr(755,root,root) %{_bindir}/dumpoops
%attr(755,root,root) %{_libdir}/%{name}/libKerneloops.so
%attr(755,root,root) %{_libdir}/%{name}/libKerneloopsScanner.so
%{_mandir}/man7/%{name}-KerneloopsScanner.7*

%files plugin-kerneloopsreporter
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/%{name}/plugins/KerneloopsReporter.conf
%attr(755,root,root) %{_libdir}/%{name}/libKerneloopsReporter.so
%{_libdir}/%{name}/KerneloopsReporter.GTKBuilder
%{_mandir}/man7/%{name}-KerneloopsReporter.7*

%files plugin-sqlite3
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/%{name}/plugins/SQLite3.conf
%attr(755,root,root) %{_libdir}/%{name}/libSQLite3.so
%{_mandir}/man7/%{name}-SQLite3.7*

%files plugin-logger
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/%{name}/plugins/Logger.conf
%attr(755,root,root) %{_libdir}/%{name}/libLogger.so
%{_libdir}/%{name}/Logger.GTKBuilder
%{_mandir}/man7/%{name}-Logger.7*

%files plugin-mailx
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/%{name}/plugins/Mailx.conf
%attr(755,root,root) %{_libdir}/%{name}/libMailx.so
%{_libdir}/%{name}/Mailx.GTKBuilder
%{_mandir}/man7/%{name}-Mailx.7*

%files plugin-runapp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libRunApp.so
%{_mandir}/man7/%{name}-RunApp.7*

%files plugin-sosreport
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libSOSreport.so

%files plugin-bugzilla
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/%{name}/plugins/Bugzilla.conf
%attr(755,root,root) %{_libdir}/%{name}/libBugzilla.so
%{_libdir}/%{name}/Bugzilla.GTKBuilder
%{_mandir}/man7/%{name}-Bugzilla.7*

%files plugin-catcut
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/%{name}/plugins/Catcut.conf
%attr(755,root,root) %{_libdir}/%{name}/libCatcut.so
%{_libdir}/%{name}/Catcut.GTKBuilder
#%{_mandir}/man7/%{name}-Catcut.7*

%files plugin-ticketuploader
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/%{name}/plugins/TicketUploader.conf
%attr(755,root,root) %{_libdir}/%{name}/libTicketUploader.so
%{_libdir}/%{name}/TicketUploader.GTKBuilder
%{_mandir}/man7/%{name}-TicketUploader.7*

%files plugin-filetransfer
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/%{name}/plugins/FileTransfer.conf
%attr(755,root,root) %{_libdir}/%{name}/libFileTransfer.so
%{_mandir}/man7/%{name}-FileTransfer.7*

%files addon-python
%defattr(644,root,root,755)
%attr(2755, root, abrt) %{_bindir}/%{name}-pyhook-helper
%config(noreplace) %{_sysconfdir}/%{name}/pyhook.conf
#%{python_sitearch}/ABRTUtils.so
%attr(755,root,root) %{_libdir}/%{name}/libPython.so
%{py_sitescriptdir}/*.py[co]

%files cli
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/abrt-cli
%{_mandir}/man1/abrt-cli.1*
/etc/bash_completion.d/abrt-cli.bash

%files desktop
%defattr(644,root,root,755)
