Summary:	Electric Eyes
Summary(pl):	Elektryczne Oczy
Name:		ee
Version:	0.3.8
Release:	2
Copyright:	GPL
Group:		X11/Utilities
Group(pl):	X11/Narzêdzia
Source:		ftp://ftp.gnome.org/pub/%{name}-%{version}.tar.gz
URL:		http://www.gnome.org/
BuildRoot:	/tmp/%{name}-%{version}-root

%description
The Electric Eyes image viewer lets you view and manipulate
images in a variety of formats.

%description -l pl
"Elektryczne Oczy" s± przegl±dark± dla ró¿norodnych formatów graficznych,

%prep
%setup -q

%build
autoconf
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr/X11R6 \
	--with-included-gettext
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr/X11R6 install

strip $RPM_BUILD_ROOT/usr/X11R6/bin/*

bzip2 -9 AUTHORS ChangeLog NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README}.bz2

%attr(755,root,root) /usr/X11R6/bin/*

/usr/X11R6/share/gnome/help/ee
/usr/X11R6/share/apps/Graphics/*

%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/ee.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/ee.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/ee.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/ee.mo
%lang(ga) /usr/X11R6/share/locale/ga/LC_MESSAGES/ee.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/ee.mo
%lang(ja) /usr/X11R6/share/locale/ja/LC_MESSAGES/ee.mo
%lang(ko) /usr/X11R6/share/locale/ko/LC_MESSAGES/ee.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/ee.mo
%lang(pt) /usr/X11R6/share/locale/pt/LC_MESSAGES/ee.mo
%lang(ru) /usr/X11R6/share/locale/ru/LC_MESSAGES/ee.mo
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/ee.mo

%changelog
* Sun Mar 14 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.3.8-2]
- removed Requires (autogenerate).

* Sat Feb 27 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.3.8-1]
- Requires changed to imlib = 1.9.3, gtk+ = 1.2.0,
- more locales (ru, sv),
- changed Group(pl).

* Tue Jan 05 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.3.5-1]
- added LDFLAGS="-s" to ./configure enviroment,
- added --with-included-gettext to configure parameters,
- added full %attr description in %files,
- more locales (ja),
- build against GNU libc-2.1.

* Sun Sep 27 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.3-7]
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added full %attr description in %files,
- added stripping binaries,
- chnged install pprefix to /usr/X11R6
- removed COPYING from %doc (copyright statment is in Copyright field).

* Thu Sep 24 1998 Cristian Gafton <gafton@redhat.com>
- add again the Obsoletes tag (commented out)
- rebuild to link against the static gnome-libs

* Tue Sep 22 1998 Carsten Haitzler <raster@redhat.com>
- requires imlib 1.8
- more minor bug fixes.

* Fri Sep 11 1998 Cristian Gafton <gafton@redhat.com>
- packaged for 5.2

* Thu Aug 13 1998 Marc Ewing <marc@redhat.com>
- Initial spec file copied from gnome-graphics
