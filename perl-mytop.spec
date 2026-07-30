%define upstream_name    mytop
Name:		perl-%{upstream_name}
Version:	1.2
Release:	1

Summary:	A clone of top for MySQL 3.22.x to 4.x
License:	GPL
Group:		Databases
Url:		https://jeremy.zawodny.com/mysql/mytop/
Source0:	https://cpan.metacpan.org/authors/id/J/JZ/JZAWODNY/mytop-1.2.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Term::ReadKey)
BuildArch:	noarch
Requires:	perl(Term::ReadKey)

%description
Mytop is a console-based (non-gui) tool for monitoring the threads and overall
performance of a MySQL 3.22.x, 3.23.x, and 4.x server.

%prep
%setup -q -n mytop-1.2

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test || :

%install
# beware to use _std macros 
%makeinstall_std

%files
%{_bindir}/mytop
%{_mandir}/man1/%{upstream_name}.*
%doc README

