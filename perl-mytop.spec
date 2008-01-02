%define name perl-mytop
%define realname mytop
%define version 1.6
%define release %mkrel 1

Summary: A clone of top for MySQL 3.22.x to 4.x
Name: %{name}
Version: %{version}
Release: %{release}
Source: http://jeremy.zawodny.com/mysql/mytop/%{realname}-%{version}.tar.bz2
URL: http://jeremy.zawodny.com/mysql/mytop/
License: GPL
Group: Databases
BuildArch:  noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildRequires: perl-Term-ReadKey
Requires: perl-Term-ReadKey

%description
Mytop is a console-based (non-gui) tool for monitoring the threads and overall
performance of a MySQL 3.22.x, 3.23.x, and 4.x server.

%prep
%setup -q -n %{realname}-%{version}

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
%{_mandir}/man1/%{realname}.*
%doc README
