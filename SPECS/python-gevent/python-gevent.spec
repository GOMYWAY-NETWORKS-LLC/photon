%{!?python3_sitelib: %define python3_sitelib %(python3 -c "from distutils.sysconfig import get_python_lib;print(get_python_lib())")}

Summary:        Coroutine-based network library
Name:           python3-gevent
Version:        20.6.2
Release:        1%{?dist}
License:        MIT
Group:          Development/Languages/Python
Vendor:         VMware, Inc.
Distribution:   Photon
Url:            https://pypi.python.org/pypi/gevent
Source0:        gevent-%{version}.tar.gz
%define sha1    gevent=03389b622ae39715879dbfb6b71624abc8a03017

BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-libs
BuildRequires:  python3-setuptools
BuildRequires:  python3-xml
%if %{with_check}
BuildRequires: lsof
BuildRequires: curl-devel
BuildRequires: openssl-devel
BuildRequires: python3-test
%endif

Requires:       python3
Requires:       python3-libs
Requires:       python3-greenlet

%description
gevent is a coroutine-based Python networking library.
Features include:
    Fast event loop based on libev.
    Lightweight execution units based on greenlet.
    Familiar API that re-uses concepts from the Python standard library.
    Cooperative sockets with SSL support.
    DNS queries performed through c-ares or a threadpool.
    Ability to use standard library and 3rd party modules written for standard blocking sockets


%prep
%setup -q -n gevent-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%check
easy_install_3=$(ls /usr/bin |grep easy_install |grep 3)
$easy_install_3 nose
python3 setup.py develop
nosetests


%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
*   Fri Jul 24 2020 Gerrit Photon <photon-checkins@vmware.com> 20.6.2-1
-   Automatic Version Bump
*   Sat Jun 20 2020 Tapas Kundu <tkundu@vmware.com> 1.3.6-3
-   Mass removal python2
*   Mon Jan 14 2019 Tapas Kundu <tkundu@vmware.com> 1.3.6-2
-   Fix make check
*   Wed Sep 12 2018 Tapas Kundu <tkundu@vmware.com> 1.3.6-1
-   Updated to version 1.3.6
*   Wed Sep 20 2017 Bo Gan <ganb@vmware.com> 1.2.1-6
-   Fix build and make check issues
*   Wed Sep 13 2017 Rongrong Qiu <rqiu@vmware.com> 1.2.1-5
-   Update make check for bug 1900401
*   Wed Jun 07 2017 Xiaolin Li <xiaolinl@vmware.com> 1.2.1-4
-   Add python3-setuptools and python3-xml to python3 sub package Buildrequires.
*   Thu Jun 01 2017 Dheeraj Shetty <dheerajs@vmware.com> 1.2.1-3
-   Removed erroneous line
*   Tue May 16 2017 Rongrong Qiu <rqiu@vmware.com> 1.2.1-2
-   Add requires python-greenlet and python3-greenlet
*   Thu Mar 02 2017 Xiaolin Li <xiaolinl@vmware.com> 1.2.1-1
-   Initial packaging for Photon
