Summary:	xf86dga application
Summary(pl):	Aplikacja xf86dga
Name:		xorg-app-xf86dga
Version:	0.99.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/app/xf86dga-%{version}.tar.bz2
# Source0-md5:	c66dfe0e8247022d8dff634d7e96bf9b
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXxf86dga-devel
BuildRequires:	xorg-util-util-macros >= 0.99.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xf86dga application.

%description -l pl
Aplikacja xf86dga.

%prep
%setup -q -n xf86dga-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	appmandir=%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1x*
