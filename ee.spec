Summary:	Electric Eyes
Summary(pl):	Elektryczne Oczy
Name:		ee
Version:	0.3.8
Release:	7
Copyright:	GPL
Group:		X11/Utilities
Group(pl):	X11/Narzêdzia
Source:		ftp://ftp.gnome.org/pub/%{name}-%{version}.tar.gz
Patch:		ee-desktop.patch
URL:		http://www.gnome.org/
BuildPrereq:	gtk+-devel >= 1.2.0
BuildPrereq:	xpm-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix /usr/X11R6

%description
The Electric Eyes image viewer lets you view and manipulate
images in a variety of formats.

%description -l pl
"Elektryczne Oczy" s± przegl±dark± dla ró¿norodnych formatów graficznych,

%prep
%setup -q
%patch -p1

%build
autoconf
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--without-included-gettext
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{_prefix} install

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README}.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gnome/help/ee
%{_datadir}/gnome/apps/Graphics/*

%changelog
* Sun May 30 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.3.8-7]
- based on RH spec,
- spec rewrited by PLD team.
