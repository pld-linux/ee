Summary:	The Electric Eyes image viewer application
Summary(es):	Electric Eyes - Visualizador de Im�genes
Summary(fr):	Le visualiseur d'images Electric Eyes
Summary(pl):	Elektryczne Oczy - przegl�darka plik�w graficznych
Summary(pt_BR): Electric Eyes - Visualizador de Imagens
Name:		ee
Version:	0.3.12
Release:	5
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/ee/%{name}-%{version}.tar.gz
Icon:		ee.xpm
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	imlib-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gnome-libs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _prefix /usr/X11R6

%description
The ee package contains the Electric Eyes image viewer for the GNOME
desktop environment. Electric Eyes is primary an image viewer, but it
also allows many types of image manipulations. Electric Eyes can
handle almost any type of image.

%description -l es
El visor de im�genes Electric Eyes permite visualizar y manejar una
variedad de formatos de im�genes.

%description -l fr
Le package ee contient le visualiseur d'images Electric Eyes pour le
bureau graphique GNOME. Electric Eyes est d'abord un visualiseur
d'images, mais il peut aussi les modifier. Electric Eyes peut g�rer
quasiment tous les types d'images.

%description -l pl
"Elektryczne Oczy" s� przegl�dark� plik�w graficznych w r�nych
formatach dla GNOME. Electric Eyes jest przede wszystkim przegl�dark�,
ale mo�e te� s�u�y� do wykonywania niekt�rych operacji spotykanych w
programach do obr�bki grafiki.

%description -l pt_BR
O visualizador de imagens Electric Eyes permite a visualiza��o e
manipula��o de uma variedade de formatos de imagens.

%prep
%setup -q

%build
rm -rf missing
libtoolize --copy --force
gettextize --copy --force
aclocal -I macros
autoconf
automake -a -c
%configure \
	--without-included-gettext
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Graphicsdir=%{_applnkdir}/Graphics/Viewers

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/mime-info/*
%{_applnkdir}/Graphics/Viewers/ee.desktop
%{_pixmapsdir}/*
