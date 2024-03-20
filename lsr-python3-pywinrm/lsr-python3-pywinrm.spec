%global srcname pywinrm

Name:           lsr-python3-%{srcname}
Version:        0.4.3
Release:        1%{?dist}
Summary:        %{srcname} module and its dependencies to be installed with pip3

License:        MIT
URL:            https://pypi.org/project/%{srcname}/

BuildArch:      noarch
BuildRequires:  python3dist(pip)

%description
To install pywinrm from this RPM, run the following command:
$ pip3 install --no-index \
    --find-links=file:///usr/share/lsr-python3-%{srcname} \
    --ignore-installed

%install
# mkdir %{_datadir}/%{name}
# mkdir %{buildroot}%{_datadir}/%{name}
# pip3 download -I %{srcname}==%{version} -U --root %{buildroot}
# cd %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}
cd %{buildroot}%{_datadir}/%{name}
pip3 download %{srcname}==%{version}

%files
/%{_datadir}/%{name}

%changelog
* Thu Mar 14 2024 Sergei Petrosian <spetrosi@redhat.com> - 0.4.3-1
- Initial package.
