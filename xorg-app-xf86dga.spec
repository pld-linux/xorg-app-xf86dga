# $Rev: 3386 $, $Date: 2005-08-15 12:17:57 $
#
Summary:	xf86dga application
Summary(pl):	Aplikacja xf86dga
Name:		xorg-app-xf86dga
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/xf86dga-%{version}.tar.bz2
# Source0-md5:	df8e8e055067a3b2ced2b80b0257a43e
Patch0:		xf86dga-man.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXxf86dga-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/xf86dga-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
xf86dga application.

%description -l pl
Aplikacja xf86dga.


%prep
%setup -q -n xf86dga-%{version}
%patch0 -p1


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
%attr(755,root,wheel) %{_bindir}/*
%{_mandir}/man1/*.1*
