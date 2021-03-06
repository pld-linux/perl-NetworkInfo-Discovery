#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	NetworkInfo
%define		pnam	Discovery
Summary:	NetworkInfo::Discovery - modules for network discovery and mapping
Summary(pl.UTF-8):	NetworkInfo::Discovery - moduły do wykrywania i odwzorowywania sieci
Name:		perl-NetworkInfo-Discovery
Version:	0.12
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/T/TS/TSCANLAN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5763876ab950dd965d3cf1501b623453
URL:		http://search.cpan.org/dist/NetworkInfo-Discovery/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Net-Pcap >= 0.04
BuildRequires:	perl-Net-Traceroute >= 1.05
BuildRequires:	perl-NetPacket >= 0.03
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NetworkInfo::Discovery is a set of modules that can be used to
discover network topology, interfaces on the network, and information
about the links between subnets. This information is brought together
into NetworkInfo::Discovery::Register where it can be examined and
used to build a unified map of the network. The network map is
controlled from a single location.

Host detection currently runs from a single location, but in the
future there will be support for having remote agents that contribute
to the central map.

%description -l pl.UTF-8
NetworkInfo::Discovery to zbiór modułów, których można używać do
wykrywania topologii sieci, interfejsów w sieci oraz informacji o
połączeniach między podsieciami. Informacje są gromadzone w
NetworkInfo::Discovery::Register, gdzie mogą być sprawdzane i używane
do zbudowania ujednoliconej mapy sieci. Mapa sieci jest kontrolowana z
jednego miejsca.

Wykrywanie hostów aktualnie działa z jednego miejsca, ale w
przyszłości będzie obsługa zdalnych agentów dostarczających informacji
do centralnej mapy.

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
%dir %{perl_vendorlib}/NetworkInfo
%{perl_vendorlib}/NetworkInfo/*.pm
%{perl_vendorlib}/NetworkInfo/Discovery
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
