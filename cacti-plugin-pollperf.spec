%define		namesrc	pollperf
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - pollperf
Summary(pl.UTF-8):	Wtyczka do Cacti - pollperf
Name:		cacti-plugin-pollperf
Version:	0.1
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://cactiusers.org/forums/download.php?id=54
#Source0:	http://download.cactiusers.org/downloads/%{namesrc}.tar.gz
# Source0-md5:
URL:		http://www.cactiusers.org/
BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactipluginroot /usr/share/cacti/plugins/%{namesrc}

%description
Plugin for Cacti - poller performance plugin.

%description -l pl.UTF-8
Wtyczka do Cacti - wtyczka sprawdzająca wydajność pobierania
informacji.

%prep
%setup -q -n %{namesrc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{webcactipluginroot}
cp -a * $RPM_BUILD_ROOT%{webcactipluginroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README
%{webcactipluginroot}
