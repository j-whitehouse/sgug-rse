Name:           perl-Test-Is
Version:        20140823.1
Release:        10%{?dist}
Summary:        Skip test in a declarative way
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Test-Is
Source0:        https://cpan.metacpan.org/authors/id/D/DO/DOLMEN/Test-Is-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# This can check only for Perl 5 versions
BuildRequires:  perl(:VERSION) < 6
# This is a plug-in into Test::More. It calls skip_all().
BuildRequires:  perl(Test::More) >= 0.88
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
# Optional tests:
BuildRequires:  perl(TAP::Harness)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
# This can check only for Perl 5 versions
Requires:       perl(:VERSION) >= 5
Requires:       perl(:VERSION) < 6
# This is a plug-in into Test::More. It calls skip_all().
Requires:       perl(Test::More) >= 0.88

%description
This module is a simple way of following the specifications of the
environment variables available for Perl tests as defined as one of
the "Lancaster Consensus" at Perl QA Hackathon 2013. Those variables
(NONINTERACTIVE_TESTING, EXTENDED_TESTING) define which tests should
be skipped.

%prep
%setup -q -n Test-Is-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20140823.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 20140823.1-9
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20140823.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20140823.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 20140823.1-6
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20140823.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20140823.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 20140823.1-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20140823.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 21 2016 Petr Pisar <ppisar@redhat.com> 20140823.1-1
- Specfile autogenerated by cpanspec 1.78.
