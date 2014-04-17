%global debug_package %{nil}

Name:           ocaml-xcp-rrd
Version:        %(date +%%y%%m%%d)
Release:        1%{?dist}
Summary:        Round-Robin Datasources in OCaml
License:        LGPL
Group:          Development/Libraries
URL:            https://github.com/xapi-project/xcp-rrd
Source0:        https://github.com/xapi-project/xcp-rrd/archive/master/xcp-rrd-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-obuild
BuildRequires:  ocaml-rpc-devel
BuildRequires:  ocaml-stdext-devel
Requires:       ocaml
Requires:       ocaml-findlib

%description
Round-Robin Datasources in OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
#Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n xcp-rrd-master

%build
make

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
make install


%files
#This space intentionally left blank

%files devel
%doc LICENSE README.md ChangeLog MAINTAINERS
%{_libdir}/ocaml/xcp-rrd/*

%changelog
* Thu Jun  6 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.0-1
- Initial package

