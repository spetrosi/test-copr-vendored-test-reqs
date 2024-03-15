%global srcname pywinrm
%global srcdirname winrm

Name:           python-%{srcname}
Version:        0.4.3
Release:        1%{?dist}
Summary:        winrm python module

License:        MIT
URL:            https://pypi.org/project/pywinrm/
Source:         %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
A pywinrm python module vendored by RHEL System Roles. It is required for
ansible.windows.win_shell Ansible module}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
# BuildRequires:  python3-setuptools

# BuildRequires:  python3-devel
# BuildRequires:  python3dist(setuptools)
# BuildRequires:  python3dist(pytest)
# BuildRequires:  python3dist(mock)
# BuildRequires:  python3dist(xmltodict)
# BuildRequires:  python3dist(requests) >= 2.9.1
# BuildRequires:  python3dist(requests-ntlm) >= 0.3
# BuildRequires:  python3dist(six)

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/pywinrm-*.egg-info/
%{python3_sitelib}/%{srcdirname}/

%changelog
* Thu Mar 14 2024 Sergei Petrosian <spetrosi@redhat.com> - 0.4.3-1
- Initial package.
