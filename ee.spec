Summary:	The Electric Eyes image viewer application
Summary(es):	Electric Eyes - Visualizador de Im�genes
Summary(fr):	Le visualiseur d'images Electric Eyes
Summary(pl):	Elektryczne Oczy - przegl�darka plik�w graficznych
Summary(pt_BR):	Electric Eyes - Visualizador de Imagens
Summary(ru):	��������� ��������� ����������� Electric Eyes
Summary(uk):	�������� ��������� ��������� Electric Eyes
Name:		ee
Version:	0.3.12
Release:	13
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/ee/0.3/%{name}-%{version}.tar.gz
# Source0-md5:	d7e92c1cc560ce76e439353462b8aa7e
Patch0:		%{name}-uk.po.patch
Patch1:		%{name}-pt_BR.po.patch
Patch2:		%{name}-desktop.patch
Patch3:		%{name}-locale_names.patch
Patch4:		%{name}-zh_and_ja.po.patch
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

%description -l ru
����� ee �������� ��������� ��������� ����������� Electric Eyes ���
����� �������� ����� GNOME. Electric Eyes � ������ ������� ���������
���������, ���� � ������������ ����� ����� ����������� ���
�������������. Electric Eyes ����� �������� ����������� � ����� �����
�����������.

%description -l uk
����� ee ͦ����� �������� ��������� ��������� Electric Eyes ���
���������� �������� ����� GNOME. Electric Eyes � ����� ����� �
��������� ���������, ���� � Ц�����դ ������ ��Ц� ��Φ����æ� ���
������������. Electric Eyes ���� ��������� ��������� � ����-���� �����
���������.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

mv -f po/zh_TW{.Big5,}.po
mv -f po/zh_CN{.GB2312,}.po
mv -f po/{no,nb}.po

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
	Graphicsdir=%{_desktopdir}

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/zh_CN{.GB2312,}
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/zh_TW{.Big5,}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/mime-info/*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/*
