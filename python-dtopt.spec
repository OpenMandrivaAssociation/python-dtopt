%define module dtopt

Name:           python-%{module}
Version:        0.1
Release:        %mkrel 1
Summary:        Add options to doctest examples while they are running
Group:          Development/Python
License:        MIT License
URL:            http://pypi.python.org/pypi/dtopt
Source0:        %{module}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-buildroot
BuildRequires:  python-devel
BuildRequires:  python-setuptools
Buildarch:	noarch

%description
When using the doctest module it is often convenient to use the ELLIPSIS option,
which allows you to use ... as a wildcard. But you either have to setup the test
runner to use this option, or you must put #doctest: +ELLIPSIS on every example
that uses this feature.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{optflags}" python setup.py build

rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT --install-purelib=%{python_sitelib}

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc docs/
%{python_sitelib}/*
