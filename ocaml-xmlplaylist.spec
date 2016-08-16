Name:     ocaml-xmlplaylist

Version:  0.1.4
Release:  1
Summary:  OCaml bindings for xmlplaylist
License:  GPLv2+
URL:      https://github.com/savonet/ocaml-xmlplaylist
Source0:  https://github.com/savonet/ocaml-xmlplaylist/releases/download/%{version}/ocaml-xmlplaylist-%{version}.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-xmlm-devel
Requires:      ocaml-xmlm

%prep
%setup -q 

%build
./configure \
   --prefix=%{_prefix} \
   -disable-ldconf
make all

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}$(ocamlfind printconf destdir)
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs

install -d $OCAMLFIND_DESTDIR/%{ocamlpck}
install -d $OCAMLFIND_DESTDIR/stublibs
make install

%files
/usr/lib64/ocaml/xmlplaylist/META
/usr/lib64/ocaml/xmlplaylist/xmlplaylist.a
/usr/lib64/ocaml/xmlplaylist/xmlplaylist.cma
/usr/lib64/ocaml/xmlplaylist/xmlplaylist.cmi
/usr/lib64/ocaml/xmlplaylist/xmlplaylist.cmxa
/usr/lib64/ocaml/xmlplaylist/xmlplaylist.mli
/usr/lib64/ocaml/xmlplaylist/xmlplaylist.cmx

%description
OCAML bindings for xmlplaylist


%changelog
* Sun Jul  3 2016 Lucas Bickel <hairmare@rabe.ch>
- initial version, mostly stolen from https://www.openmamba.org/showfile.html?file=/pub/openmamba/devel/specs/ocaml-xmlplaylist.spec
