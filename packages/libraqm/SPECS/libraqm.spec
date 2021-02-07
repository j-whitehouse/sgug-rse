Name:				libraqm
Version:			0.7.0
Release:			4%{?dist}
License:			MIT
Summary:			Complex Textlayout Library
URL:				https://github.com/HOST-Oman/libraqm
Source:				https://github.com/HOST-Oman/libraqm/releases/download/v%{version}/raqm-%{version}.tar.gz

%if 0%{?el7}
BuildRequires:      python2
%else
BuildRequires:      python3
%endif

BuildRequires:      gcc
BuildRequires:		freetype-devel
BuildRequires:		harfbuzz-devel
BuildRequires:		fribidi-devel
#BuildRequires:		gtk-doc

%package docs
Summary:			Libraqm Documentation
BuildArch:			noarch

%package devel
Summary:			Complex Textlayout Library
Requires:			libraqm%{?_isa} = %{version}-%{release}

%description
Library that encapsulates the logic for complex
text layout and provides a convenient API.


%description devel
Library that encapsulates the logic for complex
text layout and provides a convenient API.

%description docs
This package contains documentation files for raqm.

%prep
%setup -q -n raqm-%{version}
%if ! 0%{?el7}
sed s:python:%{__python3}:g -i tests/Makefile.in #Fixed in next release on upstream
%endif
%configure

%build
make %{?_smp_mflags}

%check
%if 0%{?el7}
export LC_ALL=en_US.UTF-8
%else
export LC_ALL=C.utf8
%endif
make check

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.{la,a}

#%%ldconfig_scriptlets devel

%files
%license COPYING
%{_libdir}/libraqm.so.*

%files devel
%license COPYING
%{_includedir}/raqm.h
%{_includedir}/raqm-version.h
%{_libdir}/libraqm.so
%{_libdir}/pkgconfig/raqm.pc

%files docs
%license COPYING
%doc AUTHORS NEWS README
%{_datadir}/gtk-doc/html/raqm

%changelog
* Mon Aug 17 2020  HAL <notes2@gmx.de> - 0.7.0-4
- compiles on Irix 6.5 with sgug-rse gcc 9.2.

* Fri Jan 10 2020 Mosaab Alzoubi <moceap@hotmail.com> - 0.7.0-4
- First build on EPEL8
- Use one branch to build on Fedora and EPEL
- Use python3 as BR except EPEL7
- Use LC_ALL=en_US.UTF-8 in EPEL7

* Sun Sep 8 2019 Mosaab Alzoubi <moceap@hotmail.com> - 0.7.0-1
- Updated to 0.7.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.5.0-3
- Use C.UTF-8 locale
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 14 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.0-1
- Update to latest version

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 1 2016 Mosaab Alzoubi <moceap@hotmail.com> - 0.1.1-1
- Updated to 0.1.1

* Mon Apr 25 2016 Mosaab Alzoubi <moceap@hotmail.com> - 0.1.0-3
- Use lib prefix in %%name
- Depends on same version -devel

* Sun Apr 24 2016 Mosaab Alzoubi <moceap@hotmail.com> - 0.1.0-2
- General revision

* Sat Apr 23 2016 Mosaab Alzoubi <moceap@hotmail.com> - 0.1.0-1
- Initial build
