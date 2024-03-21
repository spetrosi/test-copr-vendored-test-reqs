%global srcname pywinrm
%global srcver 0.4.3

Name:           lsr-python3-%{srcname}-src
Version:        %{srcver}
Release:        1%{?dist}
Summary:        Sources for the %{srcname} module and its dependencies to be installed with pip3

License:        MIT
URL:            https://pypi.org/project/%{srcname}/

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(pip)
BuildRequires:  python3-pip

%description
To install %{srcname} from this RPM, run the following command:
$ pip3 install --no-index \
    --find-links=file:///usr/share/lsr-python3-%{srcname} \
    --ignore-installed

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
cd %{buildroot}%{_datadir}/%{name}
pip3 --version
pip3 download %{srcname}==%{version}

%files
/%{_datadir}/%{name}

%changelog
* Thu Mar 14 2024 Sergei Petrosian <spetrosi@redhat.com> - 0.4.3-1
- Initial package.
