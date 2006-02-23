Summary:	glitz - OpenGL compositing library
Summary(pl):	glitz - biblioteka mieszania OpenGL
Name:		glitz
Version:	0.5.4
%define		_snap	20060223
Release:	0.%{_snap}.1
License:	BSD-like
Group:		Libraries
#Source0:	http://cairographics.org/snapshots/%{name}-%{version}.tar.gz
Source0:	%{name}-%{_snap}.tar.bz2
# Source0-md5:	bba2d598850965c0cabc393bfcd0e3b4
Patch0:		%{name}-link.patch
# it's not directory, don't add /
URL:		http://www.freedesktop.org/Software/glitz
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	xorg-lib-libX11-devel
# incompatible with glitz 0.2.x despite same soname
Conflicts:	cairo < 0.3.0-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Glitz is a portable 2D graphics library that uses OpenGL to render
hardware accelerated graphics. It supports many of the latest OpenGL
features, such as efficient off-screen rendering using pbuffers.
Rendering can be carried out by arbitrary OpenGL layers, thanks to
glitz's extensible backend system. Glitz is designed to match the X
Render Extension semantics and provides a general way for accelerating
this imaging model. Glitz can be used as a stand-alone layer above
OpenGL but is also designed to act as a backend for cairo, providing
it with OpenGL accelerated output.

%description -l pl
Glitz to przeno¶na biblioteka grafiki 2D u¿ywaj±ca OpenGL-a do
renderowania grafiki ze sprzêtow± akceleracj±. Obs³uguje wiele
nowych mo¿liwo¶ci OpenGL-a, takich jak wydajny rendering poza ekranem
przy u¿yciu p-buforów. Renderowanie mo¿e byæ wykonywane przez dowolne
warstwy OpenGL-a dziêki rozszerzalnemu systemowi backendów glitza.
Glitz zosta³ zaprojektowany aby pasowa³ do semantyki rozszerzenia
X Render i dostarcza ogólny sposób akceleracji tego modelu rysowania.
Glitz mo¿e byæ u¿ywany jako samodzielna warstwa ponad OpenGL, ale
zosta³ zaprojektowany tak¿e, ¿eby s³u¿y³ jako backend dla cairo,
udostêpniaj±c akcelerowane wyj¶cie OpenGL.

%package devel
Summary:	Header files for glitz libraries
Summary(pl):	Pliki nag³ówkowe bibliotek glitz
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
# for glitz-glx
Requires:	OpenGL-devel
Requires:	xorg-lib-libX11-devel

%description devel
Header files for glitz libraries.

%description devel -l pl
Pliki nag³ówkowe bibliotek glitz.

%package static
Summary:	Static glitz libraries
Summary(pl):	Statyczne biblioteki glitz
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static glitz libraries.

%description static -l pl
Statyczne biblioteki glitz.

%prep
%setup -q -n %{name}-%{_snap}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-agl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/glitz*.h
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
