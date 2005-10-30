#
Summary:	GTK-Webcore Core library
Name:		osb-nrcore
Version:	0.5.0
Release:	0.1
License:	GPL
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/gtk-webcore/%{name}-%{version}.tar.gz
# Source0-md5:	16d9a9a322025cae1a7fe8225690695a
URL:		http://gtk-webcore.sourceforge.net/
BuildRequires:	gtk+2-devel
BuildRequires:	osb-jscore-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK Webcore Core library

%package devel
Summary:	Development libraries and header files for osb-nrcore library
Group:		Development/Libraries
#Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the development libraries and header
files for osb-nrcore.

%package static
Summary:	Static osb-nrcore library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static osb-nrcore library.

%prep
%setup -q

%build
%configure
%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%dir %{_includedir}/osb
%{_includedir}/osb/NRCore
%{_libdir}/libnrcore.so.0.0.0
%{_libdir}/libnrcore_kwiq_gtk.so.0.0.0
%{_datadir}/%{name}

%files devel
%{_libdir}/libnrcore.la
%{_libdir}/libnrcore.so
%{_libdir}/libnrcore_kwiq_gtk.la
%{_libdir}/libnrcore_kwiq_gtk.so
%{_libdir}/pkgconfig/osb-nrcore.pc

%files static
%{_libdir}/libnrcore.a
%{_libdir}/libnrcore_kwiq_gtk.a
