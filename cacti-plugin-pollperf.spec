%define		plugin	pollperf
%define		php_min_version 5.0.0
Summary:	Plugin for Cacti - pollperf
Summary(pl.UTF-8):	Wtyczka do Cacti - pollperf
Name:		cacti-plugin-%{plugin}
Version:	0.1
Release:	2
License:	GPL v2
Group:		Applications/WWW
Source0:	http://forums.cacti.net/download/file.php?id=4956#/%{plugin}.zip
# Source0-md5:	50aff104fa7b232dfa9ac62bdacbdb83
URL:		http://forums.cacti.net/viewtopic.php?t=12369
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	cacti
Requires:	php(core) >= %{php_min_version}
Requires:	php(date)
Requires:	php(pcre)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		plugindir		%{cactidir}/plugins/%{plugin}

%description
Analyzing Poller Performance from DEBUG Log.

%description -l pl.UTF-8
Wtyczka do Cacti - wtyczka sprawdzająca wydajność pobierania
informacji.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a %{plugin}/* $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{plugindir}
