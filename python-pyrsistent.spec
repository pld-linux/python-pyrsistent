%define		module	pyrsistent
Summary:	Persistent/Functional/Immutable data structures
Name:		python-pyrsistent
Version:	0.9.1
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	5c8e33ccea9507ea9fd0d64386f33931
URL:		http://github.com/tobgu/pyrsistent/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-six
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pyrsistent is a number of persistent collections (by some referred to
as functional data structures). Persistent in the sense that they are
immutable.

%prep
%setup -q -n %{module}-%{version}

# Remove bundled egg-info
%{__rm} -r %{module}.egg-info

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitedir}/_pyrsistent_*.py[co]
%{py_sitedir}/pyrsistent.py[co]
%attr(755,root,root) %{py_sitedir}/pvectorc.so
%{py_sitedir}/pyrsistent-%{version}-py*.egg-info
