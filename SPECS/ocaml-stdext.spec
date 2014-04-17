%global debug_package %{nil}

Name:           ocaml-stdext
Version:        %(date +%%y%%m%%d)
Release:        1%{?dist}
Summary:        Deprecated misc library functions for OCaml
License:        LGPL
Group:          Development/Libraries
URL:            https://github.com/xapi-project/stdext
Source0:        https://github.com/xapi-project/stdext/archive/master/%{name}-%{version}.tar.gz
Patch0:         stdext-ocaml401.patch
BuildRequires:  ocaml
BuildRequires:  ocaml-fd-send-recv-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-uuidm-devel
Requires:       ocaml
Requires:       ocaml-findlib

%description
Deprecated misc library functions for OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
#Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n stdext-master
%patch0 -p1

%build
make

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
mkdir -p %{buildroot}/%{_libdir}/ocaml/stublibs
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
make install DESTDIR=${buildroot}


%files
#This space intentionally left blank

%files devel
%doc README.md
%{_libdir}/ocaml/stdext/*
%{_libdir}/ocaml/stublibs/dllstdext_stubs.so
%{_libdir}/ocaml/stublibs/dllstdext_stubs.so.owner

%changelog
* Tue Apr 1 2014 Euan Harris <euan.harris@citrix.com> - 0.10.0-1
- Update to 0.10.0, removing the Tar module (use ocaml-tar instead)

* Tue Sep 10 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.1-1
- Update to 0.9.1

* Mon Jun  3 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

