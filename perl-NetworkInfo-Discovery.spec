#
# Conditional build:
%bcond_without  tests           # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	NetworkInfo
%define	pnam	Discovery
Summary:	NetworkInfo::Discovery - Modules for network discovery and mapping
#Summary(pl):	
Name:		perl-NetworkInfo-Discovery
Version:	0.12
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/T/TS/TSCANLAN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5763876ab950dd965d3cf1501b623453
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-NetPacket >= 0.03
BuildRequires:	perl-Net-Pcap >= 0.04
BuildRequires:	perl-Net-Traceroute >= 1.05
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NetworkInfo::Discovery is a set of modules that can be used to discover
network topology, interfaces on the network, and information about
the links between subnets.  This information is brought together into
C<NetworkInfo::Discovery::Register> where it can be examined and used
to build a unified map of the network.  The network map is controlled
from a single location.

Host detection currently runs from a single location, but in the future
there will be support for having remote agents that contribute to the
central map.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a example $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/NetworkInfo/*.pm
%{perl_vendorlib}/NetworkInfo/Discovery
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
