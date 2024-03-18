Name:           ansible-collection-ansible-posix
Version:        1.5.2
Release:        1%{?dist}
Summary:        Selected modules from the ansible.posix collection for System Roles usage
License:        GPL-3.0-or-later and PSF-2.0
URL:            %{ansible_collection_url ansible posix}
%global forgeurl https://github.com/ansible-collections/ansible.posix
Source0:        %{forgeurl}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ansible-packaging
# Version 5 specifically requires ansible-core 2.11 or above
Requires:       ansible-core > 2.11

BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup -n ansible.posix-%{version_no_tilde}
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +

# plugins/callback/debug.py
# plugins/callback/profile_tasks.py
# plugins/modules/mount.py
# plugins/module_utils/__init__.py
# plugins/module_utils/mount.py

%build
%ansible_collection_build

%install
%ansible_collection_install

%files -f %{ansible_collection_filelist}
%license COPYING LICENSES .reuse/dep5
%doc README.md CHANGELOG.rst*

%changelog
* Mon Mar 18 2024 Sergei Petrosian <spetrosi@redhat.com> - 1.5.2-1
- Initial package.
