Summary:	The Electric Eyes image viewer application
Summary(es):	Electric Eyes - Visualizador de Imágenes
Summary(fr):	Le visualiseur d'images Electric Eyes
Summary(pl):	Elektryczne Oczy - przegl±darka plików graficznych
Summary(pt_BR):	Electric Eyes - Visualizador de Imagens
Name:		ee
Version:	0.3.12
Release:	5
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/ee/0.3/%{name}-%{version}.tar.gz
Icon:		ee.xpm
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	imlib-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
The ee package contains the Electric Eyes image viewer for the GNOME
desktop environment. Electric Eyes is primary an image viewer, but it
also allows many types of image manipulations. Electric Eyes can
handle almost any type of image.

%description -l es
El visor de imágenes Electric Eyes permite visualizar y manejar una
variedad de formatos de imágenes.

%description -l fr
Le package ee contient le visualiseur d'images Electric Eyes pour le
bureau graphique GNOME. Electric Eyes est d'abord un visualiseur
d'images, mais il peut aussi les modifier. Electric Eyes peut gérer
quasiment tous les types d'images.

%description -l pl
"Elektryczne Oczy" s± przegl±dark± plików graficznych w ró¿nych
formatach dla GNOME. Electric Eyes jest przede wszystkim przegl±dark±,
ale mo¿e te¿ s³u¿yæ do wykonywania niektórych operacji spotykanych w
programach do obróbki grafiki.

%description -l pt_BR
O visualizador de imagens Electric Eyes permite a visualização e
manipulação de uma variedade de formatos de imagens.

%prep
%setup -q

%build
rm -rf missing
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure \
	--without-included-gettext
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Graphicsdir=%{_applnkdir}/Graphics/Viewers

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/mime-info/*
%{_applnkdir}/Graphics/Viewers/ee.desktop
%{_pixmapsdir}/*
