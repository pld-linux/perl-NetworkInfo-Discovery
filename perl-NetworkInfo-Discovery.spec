#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	NetworkInfo
%define	pnam	Discovery
Summary:	NetworkInfo::Discovery - modules for network discovery and mapping
Summary(pl):	NetworkInfo::Discovery - modu³y do wykrywania i odwzorowywania sieci
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
NetworkInfo::Discovery is a set of modules that can be used to
discover network topology, interfaces on the network, and information
about the links between subnets. This information is brought together
into NetworkInfo::Discovery::Register where it can be examined and
used to build a unified map of the network. The network map is
controlled from a single location.

Host detection currently runs from a single location, but in the
future there will be support for having remote agents that contribute
to the central map.

%description -l pl
NetworkInfo::Discovery to zbiór modu³ów, których mo¿na u¿ywaæ do
wykrywania topologii sieci, interfejsów w sieci oraz informacji o
po³±czeniach miêdzy podsieciami. Informacje s± gromadzone w
NetworkInfo::Discovery::Register, gdzie mog± byæ sprawdzane i u¿ywane
do zbudowania ujednoliconej mapy sieci. Mapa sieci jest kontrolowana z
jednego miejsca.

Wykrywanie hostów aktualnie dzia³a z jednego miejsca, ale w
przysz³o¶ci bêdzie obs³uga zdalnych agentów dostarczaj±cych informacji
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
%{perl_vendorlib}/NetworkInfo/*.pm
%{perl_vendorlib}/NetworkInfo/Discovery
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
