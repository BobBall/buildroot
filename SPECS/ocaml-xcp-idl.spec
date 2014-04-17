%global debug_package %{nil}

Name:           ocaml-xcp-idl
Version:        %(date +%%y%%m%%d)
Release:        1%{?dist}
Summary:        Common interface definitions for XCP services
License:        LGPL
Group:          Development/Libraries
URL:            https://github.com/xapi-project/xcp-idl
Source0:        https://github.com/xapi-project/xcp-idl/archive/master/xcp-idl-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  cmdliner-devel
BuildRequires:  message-switch-devel
BuildRequires:  ocaml-cohttp-devel
BuildRequires:  ocaml-fd-send-recv-devel
BuildRequires:  ocaml-rpc-devel
BuildRequires:  ocaml-xcp-rrd-devel
BuildRequires:  xmlm-devel
BuildRequires:  ocaml-ounit-devel

# XXX transitive dependencies of message-switch-devel
BuildRequires: ocaml-oclock-devel

#  "uri"
#"re"
#           "cohttp"
#           "xmlm"
#           "rpc" {> "1.4.0"}
#           "ocamlfind"
#           "syslog"
#           "message_switch"
Requires:       ocaml
Requires:       ocaml-findlib

%description
Common interface definitions for XCP services.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
#Requires:       %{name} = %{version}-%{release}
Requires:       message-switch-devel

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n xcp-idl-master
#%patch0 -p1

%build
ocaml setup.ml -configure --destdir %{buildroot}/%{_libdir}/ocaml
ocaml setup.ml -build

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
ocaml setup.ml -install


%files
#This space intentionally left blank

%files devel
%doc LICENSE README.md ChangeLog MAINTAINERS
%{_libdir}/ocaml/xcp/*

%changelog
* Thu Sep 26 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.14-1
- Support searching for executables on the XCP_PATH as well as the PATH

* Wed Sep 25 2013 David Scott <dave.scott@eu.citrix.com>
- Logging, channel passing and interface updates

* Wed Sep 04 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.12-1
- Allow domain 0 memory policy to be queried

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

