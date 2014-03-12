Summary: Enhanced version of tapdisk
Name:    blktap
Version: 0.9.0
Release: 2%{?dist}
Group:   System/Hypervisor
License: LGPL+linking exception
URL:  https://github.com/xapi-project/blktap
Source0: https://github.com/xapi-project/%{name}/archive/4703674e72135e572cd89cd1616d627b78980c45/%{name}-%{version}.tar.gz
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libaio-devel
BuildRequires: libtool
BuildRequires: libuuid-devel
BuildRequires: xen-devel
BuildRequires: openssl-devel

%description
Enhanced version of tapdisk with support for storage mirroring.

%prep 
%setup -q -n blktap-4703674e72135e572cd89cd1616d627b78980c45


%build
sh autogen.sh
./configure --prefix %{_libdir}/%{name}
make

%install

mkdir -p %{buildroot}/%{_libdir}/%{name}
mkdir -p %{buildroot}/%{_libdir}/%{name}/lib
mkdir -p %{buildroot}/%{_libdir}/%{name}/sbin
mkdir -p %{buildroot}/%{_libdir}/%{name}/bin
mkdir -p %{buildroot}/%{_libdir}/%{name}/include/blktap
mkdir -p %{buildroot}/%{_libdir}/%{name}/include/vhd
mkdir -p %{buildroot}/%{_libdir}/%{name}/libexec
mkdir -p %{buildroot}/%{_libdir}/%{name}/etc/udev/rules.d

make install DESTDIR=%{buildroot}


%files
%{_libdir}/%{name}/bin/*
%{_libdir}/%{name}/etc/udev/rules.d/blktap.rules
%{_libdir}/%{name}/etc/cron.daily/blktap-log-cleanup
%{_libdir}/%{name}/etc/logrotate.d/blktap
%{_libdir}/%{name}/include/blktap/*
%{_libdir}/%{name}/include/vhd/*
%{_libdir}/%{name}/lib/*
%{_libdir}/%{name}/libexec/*
%{_libdir}/%{name}/sbin/*

%changelog
* Fri Jan 17 2014 Euan Harris <euan.harris@citrix.com> - 0.9.0-2
- Change to upstream source repository

* Thu Oct 24 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.0-1
- Initial package
