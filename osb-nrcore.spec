Summary:	GTK-Webcore Core library
Summary(pl.UTF-8):   Główna biblioteka GTK-Webcore
Name:		osb-nrcore
Version:	0.5.0
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/gtk-webcore/%{name}-%{version}.tar.gz
# Source0-md5:	16d9a9a322025cae1a7fe8225690695a
URL:		http://gtk-webcore.sourceforge.net/
BuildRequires:	gtk+2-devel >= 2:2.2.0
BuildRequires:	libxml2-devel >= 1:2.6.0
BuildRequires:	osb-jscore-devel >= 0.4.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK-Webcore Core library.

%description -l pl.UTF-8
Główna biblioteka GTK-Webcore.

%package devel
Summary:	Header files for osb-nrcore library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki osb-nrcore
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.2.0
Requires:	libxml2-devel >= 1:2.6.0
Requires:	osb-jscore-devel >= 0.4.0

%description devel
This is the package containing the header files for osb-nrcore.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki osb-nrcore

%package static
Summary:	Static osb-nrcore library
Summary(pl.UTF-8):   Statyczna biblioteka osb-nrcore
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static osb-nrcore library.

%description static -l pl.UTF-8
Statyczna biblioteka osb-nrcore

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
%doc README
%attr(755,root,root) %{_libdir}/libnrcore.so.0.0.0
%attr(755,root,root) %{_libdir}/libnrcore_kwiq_gtk.so.0.0.0
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnrcore.so
%{_libdir}/libnrcore.la
%attr(755,root,root) %{_libdir}/libnrcore_kwiq_gtk.so
%{_libdir}/libnrcore_kwiq_gtk.la
%{_includedir}/osb/NRCore
%{_pkgconfigdir}/osb-nrcore.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libnrcore.a
%{_libdir}/libnrcore_kwiq_gtk.a
