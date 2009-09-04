%define upstream_name    mytop
%define upstream_version 1.6

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    A clone of top for MySQL 3.22.x to 4.x
License:    GPL
Group:      Databases
Url:        http://jeremy.zawodny.com/mysql/mytop/
Source0:    http://jeremy.zawodny.com/mysql/mytop/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires: perl-Term-ReadKey
BuildArch:  noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

Requires: perl-Term-ReadKey

%description
Mytop is a console-based (non-gui) tool for monitoring the threads and overall
performance of a MySQL 3.22.x, 3.23.x, and 4.x server.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
# beware to use _std macros 
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/mytop
%{_mandir}/man1/%{upstream_name}.*
%doc README
