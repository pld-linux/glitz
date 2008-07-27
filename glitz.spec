Summary:	glitz - OpenGL compositing library
Summary(pl.UTF-8):	glitz - biblioteka składania OpenGL
Name:		glitz
Version:	0.5.6
Release:	2
License:	BSD-like
Group:		Libraries
Source0:	http://cairographics.org/snapshots/%{name}-%{version}.tar.gz
# Source0-md5:	c507f140ecccc06aed8888c958edda4c
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

%description -l pl.UTF-8
Glitz to przenośna biblioteka grafiki 2D używająca OpenGL-a do
renderowania grafiki ze sprzętową akceleracją. Obsługuje wiele
nowych możliwości OpenGL-a, takich jak wydajny rendering poza ekranem
przy użyciu p-buforów. Renderowanie może być wykonywane przez dowolne
warstwy OpenGL-a dzięki rozszerzalnemu systemowi backendów glitza.
Glitz został zaprojektowany aby pasował do semantyki rozszerzenia
X Render i dostarcza ogólny sposób akceleracji tego modelu rysowania.
Glitz może być używany jako samodzielna warstwa ponad OpenGL, ale
został zaprojektowany także, żeby służył jako backend dla cairo,
udostępniając akcelerowane wyjście OpenGL.

%package devel
Summary:	Header files for glitz libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek glitz
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
# for glitz-glx
Requires:	OpenGL-devel
Requires:	xorg-lib-libX11-devel

%description devel
Header files for glitz libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek glitz.

%package static
Summary:	Static glitz libraries
Summary(pl.UTF-8):	Statyczne biblioteki glitz
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static glitz libraries.

%description static -l pl.UTF-8
Statyczne biblioteki glitz.

%prep
%setup -q
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
