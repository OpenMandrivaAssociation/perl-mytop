%define upstream_name    mytop
%define upstream_version 1.6

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	A clone of top for MySQL 3.22.x to 4.x
License:	GPL
Group:		Databases
Url:		http://jeremy.zawodny.com/mysql/mytop/
Source0:	http://jeremy.zawodny.com/mysql/mytop/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Term::ReadKey)
BuildArch:	noarch
Requires:	perl(Term::ReadKey)

%description
Mytop is a console-based (non-gui) tool for monitoring the threads and overall
performance of a MySQL 3.22.x, 3.23.x, and 4.x server.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
# beware to use _std macros 
%makeinstall_std

%files
%{_bindir}/mytop
%{_mandir}/man1/%{upstream_name}.*
%doc README

%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.600.0-2mdv2010.0
+ Revision: 430508
- rebuild

  + Jérôme Quelin <jquelin@mandriva.org>
    - rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.6-4mdv2009.0
+ Revision: 257934
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.6-3mdv2009.0
+ Revision: 245995
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.6-1mdv2008.1
+ Revision: 140692
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - fix man pages

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 1.6-1mdv2008.0
+ Revision: 25296
- 1.6
- Import perl-mytop



* Tue Jan 31 2005 Nicolas Chipaux <chipaux@mandriva.com> 1.4-2mdk
- Fix BuildRequires

* Tue Jan 31 2005 Nicolas Chipaux <chipaux@mandriva.com> 1.4-1mdk
- First mandrake release

# end of file
