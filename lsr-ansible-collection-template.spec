%global collection_namespace COLLECTION_NAMESPACE
%global collection_name COLLECTION_NAME

Name:           lsr-temp-ansible-collection-%{collection_namespace}-%{collection_name}
Version:        COLLECTION_VERSION
Release:        1%{?dist}
Summary:        Selected modules from the %{collection_namespace}.%{collection_name} collection for System Roles usage
License:        GPL-3.0-or-later AND BSD-2-Clause AND MIT AND PSF-2.0
URL:            %{ansible_collection_url %{collection_namespace} %{collection_name}}
%global forgeurl https://github.com/ansible-collections/%{collection_namespace}.%{collection_name}
Source0:        %{forgeurl}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ansible-packaging
Requires:       ansible-core > 2.11
BuildArch:      noarch

%description
%{summary}.

%prep
# autosetup script werdly reads macros. Using %collection_namespace works though
%autosetup -n %collection_namespace.%{collection_name}-%{version}
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +

# Remove unnecessary files
rm -rf .azure-pipelines bindep.txt CHANGELOG.rst changelogs codecov.yml docs \
    .github .gitignore hacking README.md requirements.txt shippable.yml \
    test-requirements.txt tests meta .reuse CHANGELOG.md CONTRIBUTING.md

MODULE_TEMPLATE

%build
%ansible_collection_build

%install
%ansible_collection_install

%files -f %{ansible_collection_filelist}
%license COPYING

%changelog
* Mon Mar 18 2024 Sergei Petrosian <spetrosi@redhat.com> - 1.5.2-1
- Initial package.
