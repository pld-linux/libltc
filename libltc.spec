#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	Linear/longitudinal timecode library
Summary(pl.UTF-8):	Biblioteka do liniowego kodu czasowego
Name:		libltc
Version:	1.3.1
Release:	1
License:	LGPL v3+
Group:		Libraries
#Source0Download: https://github.com/x42/libltc/releases
Source0:	https://github.com/x42/libltc/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a854f586b20a2732c93bc67d7b4f3813
URL:		https://github.com/x42/libltc
BuildRequires:	doxygen
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linear (or Longitudinal) Timecode (LTC) is an encoding of SMPTE
timecode data as a Manchester-Biphase encoded audio signal. The audio
signal is commonly recorded on a VTR track or other storage media.

libltc provides functionality to encode and decode LTC audio from/to
SMPTE or EBU timecode, including SMPTE date support.

%description -l pl.UTF-8
Liniowy kod czasowy (LTC - Linear/Longitudinal Timecode) to kodowanie
danych kodu czasowego SMPTE w postaci sygnału dźwiękowego z kodowaniem
Manchester-Biphase. Sygnał dźwiękowy jest zwykle nagrywany na ścieżce
VTR lub innego nośnika.

libltc udostępnia funkcjonalność kodowania i dekodowania dźwiękowego
LTC z/do kodu SMPTE lub EBU, wraz z obsługą dat SMPTE.

%package devel
Summary:	Header files for ltc library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki ltc
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for ltc library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki ltc.

%package static
Summary:	Static ltc library
Summary(pl.UTF-8):	Statyczna biblioteka ltc
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ltc library.

%description static -l pl.UTF-8
Statyczna biblioteka ltc.

%prep
%setup -q

%build
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libltc.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.md
%attr(755,root,root) %{_libdir}/libltc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libltc.so.11

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libltc.so
%{_includedir}/ltc.h
%{_pkgconfigdir}/ltc.pc
%{_mandir}/man3/ltc.h.3*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libltc.a
%endif
