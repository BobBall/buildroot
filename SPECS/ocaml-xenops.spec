%global debug_package %{nil}

Name:           ocaml-xenops
Version:        %(date +%%y%%m%%d)
Release:        1%{?dist}
Summary:        Low-level xen control operations OCaml
License:        LGPL
Group:          Development/Libraries
URL:            https://github.com/xapi-project/xenops
Source0:        https://github.com/xapi-project/xenops/archive/master/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-obuild
BuildRequires:  ocaml-rpc-devel
BuildRequires:  ocaml-stdext-devel
BuildRequires:  ocaml-xen-lowlevel-libs-devel
BuildRequires:  ocaml-xenstore-clients-devel
BuildRequires:  ocaml-xenstore-devel
BuildRequires:  ocaml-oclock-devel
BuildRequires:  ocaml-xcp-idl-devel
BuildRequires:  ocaml-xen-api-libs-transitional-devel
Requires:       ocaml
Requires:       ocaml-findlib

%description
Low-level xen control operations in OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
#Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n xenops-master

%build
make

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
make install


%files
#This space intentionally left blank

%files devel
%doc LICENSE README.md ChangeLog MAINTAINERS
%{_libdir}/ocaml/xenops/*

%changelog
* Wed Sep 25 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.2-1
- Update to 0.9.2

* Tue Sep 10 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.1

* Tue Jun 18 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

