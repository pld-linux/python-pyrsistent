#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_without	tests	# unit tests

%define		module	pyrsistent
Summary:	Persistent/Functional/Immutable data structures
Summary(pl.UTF-8):	Trwałe/funkcyjne/niezmienne struktury danych
Name:		python-pyrsistent
Version:	0.15.7
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pyrsistent/
Source0:	https://files.pythonhosted.org/packages/source/p/pyrsistent/%{module}-%{version}.tar.gz
# Source0-md5:	da9486d00ef5b213f40d5cf3c5bca82d
URL:		http://github.com/tobgu/pyrsistent/
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-hypothesis < 5
BuildRequires:	python-pytest < 5
BuildRequires:	python-six
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-hypothesis
# < 5? works also with 5.4.1
BuildRequires:	python3-pytest < 5
BuildRequires:	python3-six
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pyrsistent is a number of persistent collections (by some referred to
as functional data structures). Persistent in the sense that they are
immutable.

%description -l pl.UTF-8
Pyrsistent to zbiór trwałych kolekcji (nazywanych także funkcyjnymi
strukturami danych). Są trwałe w tym sensie, że są niezmienne.

%package -n python3-pyrsistent
Summary:	Persistent/Functional/Immutable data structures
Summary(pl.UTF-8):	Trwałe/funkcyjne/niezmienne struktury danych
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-pyrsistent
Pyrsistent is a number of persistent collections (by some referred to
as functional data structures). Persistent in the sense that they are
immutable.

%description -n python3-pyrsistent -l pl.UTF-8
Pyrsistent is a number of persistent collections (by some referred to
as functional data structures). Persistent in the sense that they are
immutable.

%prep
%setup -q -n %{module}-%{version}

# Remove bundled egg-info
%{__rm} -r %{module}.egg-info

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m pytest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.txt LICENCE.mit README.rst
%attr(755,root,root) %{py_sitedir}/pvectorc.so
%{py_sitedir}/_pyrsistent_version.py[co]
%{py_sitedir}/pyrsistent
%{py_sitedir}/pyrsistent-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pyrsistent
%defattr(644,root,root,755)
%doc CHANGES.txt LICENCE.mit README.rst
%attr(755,root,root) %{py3_sitedir}/pvectorc.cpython-*.so
%{py3_sitedir}/_pyrsistent_version.py
%{py3_sitedir}/__pycache__/_pyrsistent_version.cpython-*.py[co]
%{py3_sitedir}/pyrsistent
%{py3_sitedir}/pyrsistent-%{version}-py*.egg-info
%endif
