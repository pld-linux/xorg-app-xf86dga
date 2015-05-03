Summary:	xf86dga application - a simple test client for the XFree86-DGA extension
Summary(pl.UTF-8):	Aplikacja xf86dga - prosty testowy klient rozszerzenia XFree86-DGA
Name:		xorg-app-xf86dga
Version:	1.0.3
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xf86dga-%{version}.tar.bz2
# Source0-md5:	865a17eb6fe8892e58bb1bdb35f059df
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXxf86dga-devel >= 1.1
BuildRequires:	xorg-util-util-macros >= 1.8
Requires:	xorg-lib-libXxf86dga >= 1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xf86dga application is a simple test client for the XFree86-DGA
extension.

%description -l pl.UTF-8
Aplikacja xf86dga to prosty testowy klient rozszerzenia XFree86-DGA.

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
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/dga
%{_mandir}/man1/dga.1*
