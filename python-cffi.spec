#
# Conditional build:
%bcond_without  python2 # CPython 2.x module
%bcond_without  python3 # CPython 3.x module
%bcond_without	doc	# sphinx based documentation
#
Summary:	Foreign Function Interface for Python 2 calling C code
Summary(pl.UTF-8):	Interfejs funkcji obcych (FFI) dla Pythona 2 wywołującego kod w C
Name:		python-cffi
Version:	1.9.1
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/pypi/cffi
Source0:	https://pypi.python.org/packages/a1/32/e3d6c3a8b5461b903651dd6ce958ed03c093d2e00128e3f33ea69f1d7965/cffi-%{version}.tar.gz
# Source0-md5:	b8fa7ccb87790531db3316ab17aa8244
URL:		http://cffi.readthedocs.org/
BuildRequires:	libffi-devel >= 3
BuildRequires:	pkgconfig
%if %{with python2}
BuildRequires:	python >= 1:2.6
BuildRequires:	python-devel >= 1:2.6
%endif
%if %{with python3}
BuildRequires:	python3 >= 1:3.2
BuildRequires:	python3-devel >= 1:3.2
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%{?with_doc:BuildRequires:	sphinx-pdg}
Requires:	python-modules
Requires:	python-pycparser
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Foreign Function Interface for Python calling C code. The aim of this
project is to provide a convenient and reliable way of calling C code
from Python without learning additional language or API.

This package contains Python 2 module.

%description -l pl.UTF-8
CFFI to interfejs funkcji obcych (FFI - foreign Function Interface) do
wywoływania kodu w C z Pythona. Celem projektu jest dostarczenie
wygodnego i wiarygodnego sposobu wywoływania kodu w C z Pythona bez
potrzeby nauki dodatkowego języka lub API.

Ten pakiet zawiera moduł Pythona 2.

%package -n python3-cffi
Summary:	Foreign Function Interface for Python 3 calling C code
Summary(pl.UTF-8):	Interfejs funkcji obcych (FFI) dla Pythona 3 wywołującego kod w C
Group:		Libraries/Python
Requires:	python3-modules
Requires:	python3-pycparser

%description -n python3-cffi
Foreign Function Interface for Python calling C code. The aim of this
project is to provide a convenient and reliable way of calling C code
from Python without learning additional language or API.

This package contains Python 3 module.

%description -n python3-cffi -l pl.UTF-8
CFFI to interfejs funkcji obcych (FFI - foreign Function Interface) do
wywoływania kodu w C z Pythona. Celem projektu jest dostarczenie
wygodnego i wiarygodnego sposobu wywoływania kodu w C z Pythona bez
potrzeby nauki dodatkowego języka lub API.

Ten pakiet zawiera moduł Pythona 3.

%prep
%setup -q -n cffi-%{version}

%build
%if %{with python2}
%py_build
%endif
%if %{with python3}
%py3_build
%endif

%if %{with doc}
%{__make} -C doc html
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
%doc AUTHORS LICENSE %{?with_doc:doc/build/html/{*.html,*.js,_static}}
%attr(755,root,root) %{py_sitedir}/_cffi_backend.so
%dir %{py_sitedir}/cffi
%{py_sitedir}/cffi/_cffi_include.h
%{py_sitedir}/cffi/_embedding.h
%{py_sitedir}/cffi/parse_c_type.h
%{py_sitedir}/cffi/*.py[co]
%{py_sitedir}/cffi-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-cffi
%defattr(644,root,root,755)
%doc AUTHORS LICENSE %{?with_doc:doc/build/html/{*.html,*.js,_static}}
%attr(755,root,root) %{py3_sitedir}/_cffi_backend.cpython-*.so
%dir %{py3_sitedir}/cffi
%{py3_sitedir}/cffi/_cffi_include.h
%{py3_sitedir}/cffi/_embedding.h
%{py3_sitedir}/cffi/parse_c_type.h
%{py3_sitedir}/cffi/*.py
%{py3_sitedir}/cffi/__pycache__
%{py3_sitedir}/cffi-%{version}-py*.egg-info
%endif
