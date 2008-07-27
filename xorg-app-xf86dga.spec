Summary:	xf86dga application
Summary(pl.UTF-8):	Aplikacja xf86dga
Name:		xorg-app-xf86dga
Version:	1.0.2
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xf86dga-%{version}.tar.bz2
# Source0-md5:	66feef21fb4e769cc1e2f193ae461a8c
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXxf86dga-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xf86dga application.

%description -l pl.UTF-8
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
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/dga
%{_mandir}/man1/dga.1x*
