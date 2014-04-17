Name:           xcp-networkd
Version:        %(date +%%y%%m%%d)
Release:        1%{?dist}
Summary:        Simple host network management service for the xapi toolstack
License:        LGPL
Group:          Development/Other
URL:            https://github.com/xapi-project/xcp-networkd
Source0:        https://github.com/xapi-project/%{name}/archive/ea1254/%{name}-%{version}.tar.gz
Source1:        xcp-networkd-init
Source2:        xcp-networkd-conf
Source3:        xcp-networkd-network-conf
Source4:        xcp-networkd-bridge-conf
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-obuild
BuildRequires:  ocaml-rpc-devel
BuildRequires:  ocaml-xcp-idl-devel
BuildRequires:  forkexecd-devel
BuildRequires:  ocaml-stdext-devel
BuildRequires:  ocaml-xen-api-libs-transitional-devel
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-xcp-inventory-devel
BuildRequires:  cmdliner-devel
BuildRequires:  ocaml-cohttp-devel
BuildRequires:  ocaml-re-devel
BuildRequires:  ocaml-xen-api-client-devel
BuildRequires:  message-switch-devel
BuildRequires:  ocaml-oclock-devel
Requires:       ethtool
Requires:       redhat-lsb-core

%description
Simple host networking management service for the xapi toolstack.

%prep
%setup -q -n xcp-networkd-ea1254
cp %{SOURCE1} xcp-networkd-init
cp %{SOURCE2} xcp-networkd-conf
cp %{SOURCE3} xcp-networkd-network-conf
cp %{SOURCE4} xcp-networkd-bridge-conf

%build
make

%install
mkdir -p %{buildroot}/%{_sbindir}
install dist/build/xcp-networkd/xcp-networkd %{buildroot}/%{_sbindir}/xcp-networkd
mkdir -p %{buildroot}%{_sysconfdir}/init.d
install -m 0755 xcp-networkd-init %{buildroot}%{_sysconfdir}/init.d/xcp-networkd
mkdir -p %{buildroot}/etc/xcp
install -m 0644 xcp-networkd-network-conf %{buildroot}/etc/xcp/network.conf
install -m 0644 xcp-networkd-conf %{buildroot}/etc/xcp-networkd.conf
mkdir -p %{buildroot}/etc/modprobe.d
install -m 0644 xcp-networkd-bridge-conf %{buildroot}/etc/modprobe.d/bridge.conf


%files
%doc README.markdown LICENSE MAINTAINERS
%{_sbindir}/xcp-networkd
%{_sysconfdir}/init.d/xcp-networkd
/etc/modprobe.d/bridge.conf
%config(noreplace) /etc/xcp/network.conf
%config(noreplace) /etc/xcp-networkd.conf

%post
/sbin/chkconfig --add xcp-networkd

%preun
if [ $1 -eq 0 ]; then
  /sbin/service xcp-networkd stop > /dev/null 2>&1
  /sbin/chkconfig --del xcp-networkd
fi

%changelog
* Fri Apr 11 2014 Bob Ball <bob.ball@citrix.com> - %(date +%%y%%m%%d)-1
- Updated to build daily snapshots

* Wed Sep 25 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.3-1
- Update to 0.9.3

* Wed Aug 28 2013 David Scott <dave.scott@eu.citrix.com>
- When loading the bridge module, prevent guest traffic being
  processed by the domain 0 firewall

* Sun Jun  9 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.2

* Fri Jun  7 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.1

* Wed Jun  5 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

