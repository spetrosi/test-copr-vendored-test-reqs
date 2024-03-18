%global collection_namespace ansible
%global collection_name windows

Name:           lsr-ansible-collection-%{collection_namespace}-%{collection_name}
Version:        8.4.0
Release:        1%{?dist}
Summary:        Selected modules from the %{collection_namespace}.%{collection_name} collection for System Roles usage
License:        GPL-3.0-or-later AND BSD-2-Clause AND MIT AND PSF-2.0
URL:            %{ansible_collection_url %{collection_namespace} %{collection_name}}
%global forgeurl https://github.com/ansible-collections/%{collection_namespace}.%{collection_name}
Source0:        %{forgeurl}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ansible-packaging
# Version 5 specifically requires ansible-core 2.11 or above
Requires:       ansible-core > 2.11
BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup -n ansible.posix-%{version}
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +

# Remove unnecessary files
rm -rf .azure-pipelines bindep.txt CHANGELOG.rst changelogs codecov.yml docs \
    .github .gitignore hacking README.md requirements.txt shippable.yml \
    test-requirements.txt tests meta .reuse CHANGELOG.md CONTRIBUTING.md

# Keep only required modules
mkdir -p plugins-tmp/modules
cp plugins/modules/win_shell.py plugins/modules/win_shell.ps1 \
    plugins/modules/win_command.py plugins/modules/win_command.ps1 \
    plugins-tmp/modules/
rm -rf plugins
mv plugins-tmp plugins

%build
%ansible_collection_build

%install
%ansible_collection_install

%files -f %{ansible_collection_filelist}
%license COPYING

%changelog
* Mon Mar 18 2024 Sergei Petrosian <spetrosi@redhat.com> - 1.5.2-1
- Initial package.