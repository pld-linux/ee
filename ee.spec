Summary:	The Electric Eyes image viewer application
Summary(es):	Electric Eyes - Visualizador de Imágenes
Summary(fr):	Le visualiseur d'images Electric Eyes
Summary(pl):	Elektryczne Oczy - przegl±darka plików graficznych
Summary(pt_BR):	Electric Eyes - Visualizador de Imagens
Name:		ee
Version:	0.3.11
Release:	1
Copyright:	GPL
Group:		X11/Utilities
Group(pl):	X11/Narzêdzia
Source:		ftp://ftp.gnome.org/pub/%{name}-%{version}.tar.gz
Patch:		ee-applnk.patch
Icon		ee.xpm.
URL:		http://www.gnome.org/
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	imlib-devel
BuildRequires:	gettext-devel
BuildRequires:	XFree86-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix /usr/X11R6

%description
The ee package contains the Electric Eyes image viewer for the GNOME desktop
environment.  Electric Eyes is primary an image viewer, but it also allows
many types of image manipulations. Electric Eyes can handle almost any type
of image.

%description -l es
El visor de imágenes Electric Eyes permite visualizar y manejar una variedad
de formatos de imágenes.

%description -l fr
Le package ee contient le visualiseur d'images Electric Eyes pour le bureau
graphique GNOME. Electric Eyes est d'abord un visualiseur d'images, mais il
peut aussi les modifier. Electric Eyes peut gérer quasiment tous les types
d'images.

%description -l pl
"Elektryczne Oczy" s± przegl±dark± plików graficznych w ró¿nych formatach
dla GNOME. Electric Eyes jest przedewszystkim przegl±dark± ale moze te¿
s³u¿yæ do wykonywania niektórych operacji spotykanych w programach do
obróbki grafiki.

%description -l pt_BR
O visualizador de imagens Electric Eyes permite a visualização e manipulação
de uma variedade de formatos de imagens.

%prep
%setup -q
%patch -p1

%build
gettextize --copy --force
automake
LDFLAGS="-s"; export LDFLAGS
%configure \
	--without-included-gettext
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README}.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gnome/help/ee
%{_datadir}/applnk/Graphics/ee.desktop
