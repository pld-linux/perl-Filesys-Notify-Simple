#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Filesys
%define		pnam	Notify-Simple
Summary:	Filesys::Notify::Simple - Simple and dumb file system watcher
Name:		perl-Filesys-Notify-Simple
Version:	0.08
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Filesys/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	82a1ae968a457c7dc37367ab43a97da8
URL:		http://search.cpan.org/dist/Filesys-Notify-Simple/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Filesys::Notify::Simple is a simple but unified interface to get
notifications of changes to a given filesystem path. It utilizes
inotify2 on Linux and fsevents on OS X if they're installed, with a
fallback to the full directory scan if they're not available.

There are some limitations in this module. If you don't like it, use
File::ChangeNotify.

In return, this module doesn't depend on any non-core modules.
Platform specific optimizations with Linux::Inotify2 and Mac::FSEvents
are truely optional.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Filesys/Notify
%{perl_vendorlib}/Filesys/Notify/*.pm
%{_mandir}/man3/*
