Summary:	Library for accessing the MPQ archives
Name:		StormLib
Version:	9.23
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://github.com/ladislav-zezula/StormLib/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a498eedeb97d0a49fcc8e8b509f1a95b
Patch0:		%{name}-paths.patch
Patch1:		%{name}-missing_typedefs.patch
URL:		http://www.zezula.net/mpq.html
BuildRequires:	bzip2-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	libstdc++-devel >= 6:4.8
BuildRequires:	libtomcrypt-devel
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The StormLib library is a pack of modules, written in C++, which are
able to read and also to write files from/to the MPQ archives.

%package devel
Summary:	Header files for the StormLib library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for the StormLib library.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%cmake -B build \
	-DWITH_LIBTOMCRYPT:BOOL=ON
%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md doc/History.txt
%attr(755,root,root) %{_libdir}/libstorm.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libstorm.so.9

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libstorm.so
%{_includedir}/StormLib.h
%{_includedir}/StormPort.h
