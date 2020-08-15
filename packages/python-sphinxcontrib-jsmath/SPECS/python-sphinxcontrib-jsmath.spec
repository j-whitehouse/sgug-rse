%global pypi_name sphinxcontrib-jsmath

# when bootstrapping sphinx, we cannot run tests yet
%bcond_with check

Name:           python-%{pypi_name}
Version:        1.0.1
Release:        2%{?dist}
Summary:        Sphinx extension for math in HTML via JavaScript
License:        BSD
URL:            http://sphinx-doc.org/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%if %{with check}
BuildRequires:  python3-pytest
BuildRequires:  python3-sphinx >= 1:2
%endif

%description
sphinxcontrib-jsmath is a sphinx extension which renders display math in HTML
via JavaScript.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
sphinxcontrib-jsmath is a sphinx extension which renders display math in HTML
via JavaScript.


%prep
%autosetup -n %{pypi_name}-%{version}


%build
%py3_build


%install
%py3_install


%if %{with check}
%check
%{__python3} -m pytest
%endif


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/sphinxcontrib/
%{python3_sitelib}/sphinxcontrib_jsmath-%{version}-py%{python3_version}-*.pth
%{python3_sitelib}/sphinxcontrib_jsmath-%{version}-py%{python3_version}.egg-info/


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 01 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-1
- Initial package
