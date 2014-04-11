Name:           ocaml-opasswd
Version:        %(date +%%y%%m%%d)
Release:        1%{?dist}
Summary:        OCaml interface to the glibc passwd/shadow password functions
License:        ISC
Group:          Development/Other
URL:            http://github.com/xapi-project/ocaml-opasswd
Source0:        https://github.com/xapi-project/%{name}/archive/master/%{name}-%{version}.tar.gz
Patch0:		opasswd_ocaml4_compatability.patch
BuildRequires:  ocaml ocaml-findlib ocaml-ctypes-devel libffi-devel
Requires:       ocaml ocaml-findlib

%description
This is an OCaml binding to the glibc passwd file and shadow password
file interface. It can be used to read, parse, manipulate and write
passwd and shadow files on Linux systems. It might also work on other
nixes, but it has not been tested.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-master
%patch0 -p1

%build
ocaml setup.ml -configure --destdir %{buildroot}%{_libdir}/ocaml
ocaml setup.ml -build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
export OCAMLFIND_LDCONF=%{buildroot}%{_libdir}/ocaml/ld.conf
ocaml setup.ml -install

%clean
rm -rf %{buildroot}

%files
# This space intentionally left blank

%files devel
%defattr(-,root,root)
%doc README.md

%{_libdir}/ocaml/oPasswd/*

%changelog
* Fri Apr 11 2014 Bob Ball <bob.ball@citrix.com> - %(date +%%y%%m%%d)
- Updated to build daily snapshot

* Thu Oct 31 2013 Mike McClurg <mike.mcclurg@citrix.com>
- Initial package


