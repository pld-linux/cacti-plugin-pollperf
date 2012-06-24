%define		plugin	pollperf
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - pollperf
Summary(pl.UTF-8):	Wtyczka do Cacti - pollperf
Name:		cacti-plugin-pollperf
Version:	0.1
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://cactiusers.org/forums/download.php?id=54
#Source0:	http://download.cactiusers.org/downloads/%{plugin}.tar.gz
# Source0-md5:
URL:		http://www.cactiusers.org/
BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		plugindir		%{cactidir}/plugins/%{plugin}

%description
Plugin for Cacti - poller performance plugin.

%description -l pl.UTF-8
Wtyczka do Cacti - wtyczka sprawdzająca wydajność pobierania
informacji.

%prep
%setup -q -n %{plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README
%{plugindir}
