Name:           ocaml-xmlm
Version:        1.0.1
Release:        %mkrel 1
Summary:        Streaming XML input/output for OCaml
License:        new-BSD
Group:          Development/Other
URL:            http://erratique.ch/software/xmlm
Source0:        http://erratique.ch/software/xmlm/releases/xmlm-%{version}.tbz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
Requires:       ocaml

%description
Xmlm is an OCaml module providing streaming XML input/output. It aims at
making XML processing robust and painless. The streaming interface can
process documents without building an in-memory representation. It lets
the programmer translate its data structures to XML documents and
vice-versa. Functions are provided to easily transform arborescent data
structures to/from XML documents.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n xmlm-%{version}

%build
./build module
./build doc

%install
rm -rf %{buildroot}
export INSTALLDIR=%{buildroot}/%{_libdir}/ocaml/xmlm
./build install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_libdir}/ocaml/xmlm/META
%{_libdir}/ocaml/xmlm/xmlm.cmi
%{_libdir}/ocaml/xmlm/xmlm.cmo

%files devel
%defattr(-,root,root)
%doc test doc CHANGES
%{_libdir}/ocaml/xmlm/xmlm.cmx
%{_libdir}/ocaml/xmlm/xmlm.o
%{_libdir}/ocaml/xmlm/xmlm.mli
%{_libdir}/ocaml/xmlm/xmlm.ml

