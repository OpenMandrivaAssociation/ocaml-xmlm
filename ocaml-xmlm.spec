%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Streaming XML input/output for OCaml
Name:		ocaml-xmlm
Version:	1.0.2
Release:	2
License:	BSD
Group:		Development/Other
Url:		http://erratique.ch/software/xmlm
Source0:	http://erratique.ch/software/xmlm/releases/xmlm-%{version}.tbz
BuildRequires:	ocaml

%description
Xmlm is an OCaml module providing streaming XML input/output. It aims at
making XML processing robust and painless. The streaming interface can
process documents without building an in-memory representation. It lets
the programmer translate its data structures to XML documents and
vice-versa. Functions are provided to easily transform arborescent data
structures to/from XML documents.

%files
%doc README
%{_libdir}/ocaml/xmlm/META
%{_libdir}/ocaml/xmlm/xmlm.cmi
%{_libdir}/ocaml/xmlm/xmlm.cmo

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%files devel
%doc test doc CHANGES
%{_libdir}/ocaml/xmlm/xmlm.cmx
%{_libdir}/ocaml/xmlm/xmlm.o
%{_libdir}/ocaml/xmlm/xmlm.mli
%{_libdir}/ocaml/xmlm/xmlm.ml

#----------------------------------------------------------------------------

%prep
%setup -q -n xmlm-%{version}

%build
./build module
./build doc

%install
export INSTALLDIR=%{buildroot}/%{_libdir}/ocaml/xmlm
./build install

