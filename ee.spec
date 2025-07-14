Summary:	The Electric Eyes image viewer application
Summary(es.UTF-8):	Electric Eyes - Visualizador de Imágenes
Summary(fr.UTF-8):	Le visualiseur d'images Electric Eyes
Summary(pl.UTF-8):	Elektryczne Oczy - przeglądarka plików graficznych
Summary(pt_BR.UTF-8):	Electric Eyes - Visualizador de Imagens
Summary(ru.UTF-8):	Программа просмотра изображений Electric Eyes
Summary(uk.UTF-8):	Програма перегляду зображень Electric Eyes
Name:		ee
Version:	0.3.12
Release:	16
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/ee/0.3/%{name}-%{version}.tar.gz
# Source0-md5:	d7e92c1cc560ce76e439353462b8aa7e
Patch0:		%{name}-uk.po.patch
Patch1:		%{name}-pt_BR.po.patch
Patch2:		%{name}-desktop.patch
Patch3:		%{name}-locale_names.patch
Patch4:		%{name}-zh_and_ja.po.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
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

%description -l es.UTF-8
El visor de imágenes Electric Eyes permite visualizar y manejar una
variedad de formatos de imágenes.

%description -l fr.UTF-8
Le package ee contient le visualiseur d'images Electric Eyes pour le
bureau graphique GNOME. Electric Eyes est d'abord un visualiseur
d'images, mais il peut aussi les modifier. Electric Eyes peut gérer
quasiment tous les types d'images.

%description -l pl.UTF-8
"Elektryczne Oczy" są przeglądarką plików graficznych w różnych
formatach dla GNOME. Electric Eyes jest przede wszystkim przeglądarką,
ale może też służyć do wykonywania niektórych operacji spotykanych w
programach do obróbki grafiki.

%description -l pt_BR.UTF-8
O visualizador de imagens Electric Eyes permite a visualização e
manipulação de uma variedade de formatos de imagens.

%description -l ru.UTF-8
Пакет ee содержит программу просмотра изображений Electric Eyes для
среды рабочего стола GNOME. Electric Eyes в первую очередь программа
просмотра, хотя и поддерживает много типов манипуляций над
изображениями. Electric Eyes может работать практически с любым типом
изображений.

%description -l uk.UTF-8
Пакет ee містить програму перегляду зображень Electric Eyes для
середовища робочого столу GNOME. Electric Eyes в першу чергу є
програмою перегляду, хоча й підтримує багато типів маніпуляцій над
зображеннями. Electric Eyes може працювати практично з будь-яким типом
зображень.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

mv -f po/zh_TW{.Big5,}.po
mv -f po/zh_CN{.GB2312,}.po
mv -f po/{no,nb}.po

%build
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
	Graphicsdir=%{_desktopdir}

rm -rf $RPM_BUILD_ROOT%{_datadir}/mime-info

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/*
