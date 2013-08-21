Summary:	Reimplementation of the SIL Graphite text processing engine
Name:		graphite2
Version:	1.2.3
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/silgraphite/%{name}-%{version}.tgz
# Source0-md5:	7042305e4208af4c2d5249d814ccce58
URL:		http://projects.palaso.org/projects/graphitedev
BuildRequires:	cmake
BuildRequires:	libstdc++-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Reimplementation of the SIL Graphite text processing engine.

%package devel
Summary:	Header files for graphite2 library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for graphite2 library.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DGRAPHITE2_COMPARE_RENDERER=OFF
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

/usr/sbin/ldconfig -n $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog doc/*.txt
%attr(755,root,root) %{_bindir}/gr2fonttest
%attr(755,root,root) %ghost %{_libdir}/libgraphite2.so.3
%attr(755,root,root) %{_libdir}/libgraphite2.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgraphite2.so
%{_includedir}/graphite2
%{_pkgconfigdir}/graphite2.pc
%{_datadir}/graphite2

