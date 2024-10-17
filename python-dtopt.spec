%define module dtopt

Name:           python-%{module}
Version:        0.1
Release:        3
Summary:        Add options to doctest examples while they are running
Group:          Development/Python
License:        MIT License
URL:            https://pypi.python.org/pypi/dtopt
Source0:        %{module}-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:  python-setuptools
Buildarch:	noarch

%description
When using the doctest module it is often convenient to use the ELLIPSIS
option, which allows you to use ... as a wildcard. But you either have to
setup the test runner to use this option, or you must put #doctest: +ELLIPSIS
on every example that uses this feature.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{optflags}" python setup.py build

%{__python} setup.py install --root %{buildroot} --install-purelib=%{python_sitelib}


%files 
%defattr(-,root,root)
%doc docs/
%{python_sitelib}/*



%changelog
* Wed Jun 08 2011 Antoine Ginies <aginies@mandriva.com> 0.1-1mdv2011.0
+ Revision: 683246
- import python-dtopt


* Wed Jun 8 2011 Antoine Ginies <aginies@mandriva.com> 0.1
- first release for Mandriva 

