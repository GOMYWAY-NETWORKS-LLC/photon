Summary:        Provide tools to manage multipath devices
Name:           device-mapper-multipath
Version:        0.8.3
Release:        2%{?dist}
License:        GPL+
Group:          System Environment/Base
Vendor:         VMware, Inc.
Distribution:   Photon
URL:            http://christophe.varoqui.free.fr/
Source0:        multipath-tools-6c3bd36.tar.gz
%define         git_commit_short 6c3bd36
%define         sha1 multipath-tools=474b8f09f96ae7d96bbfbaf60bb2f2864ef14517
BuildRequires:  userspace-rcu-devel
BuildRequires:  libaio-devel
BuildRequires:  device-mapper-devel
BuildRequires:  readline-devel
BuildRequires:  ncurses-devel
BuildRequires:  systemd-devel
BuildRequires:  json-c-devel
Requires:       userspace-rcu
Requires:       libaio
Requires:       device-mapper
Requires:       libselinux
Requires:       libsepol
Requires:       readline
Requires:       ncurses
Requires:       kpartx = %{version}-%{release}

%description
Device-mapper-multipath provides tools to manage multipath devices by
instructing the device-mapper multipath kernel module what to do.

%package -n     kpartx
Summary:        Partition device manager for device-mapper devices
Requires:       device-mapper
%description -n kpartx
kpartx manages partition creation and removal for device-mapper devices.

%package        devel
Summary:        Development libraries and headers for %{name}
Requires:       %{name} = %{version}-%{release}
%description    devel
It contains the libraries and header files to create applications

%prep
%setup -qn multipath-tools-%{git_commit_short}

%build
# json_object_object_get_ex return value is changed in json-c upgrade to 0.15
sed -i 's/(json_object_object_get_ex(j_obj, key, \&j_obj_tmp) != TRUE)/(!json_object_object_get_ex(j_obj, key, \&j_obj_tmp))/g' ./libdmmp/libdmmp_private.h
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} \
	SYSTEMDPATH=/lib \
	bindir=%{_sbindir} \
	syslibdir=%{_libdir} \
	libdir=%{_libdir}/multipath \
	pkgconfdir=%{_libdir}/pkgconfig
install -vd %{buildroot}/etc/multipath

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_sbindir}/mpathpersist
%{_sbindir}/multipath
%{_sbindir}/multipathd
/lib/udev/rules.d/*
/lib64/*.so
/lib64/*.so.*
%{_libdir}/*.so
%{_libdir}/*.so.*
%{_libdir}/multipath/*.so
/lib/systemd/system/multipathd.service
/lib/systemd/system/multipathd.socket

%{_mandir}/man5/*
%{_mandir}/man8/mpathpersist.8.gz
%{_mandir}/man8/multipath.8.gz
%{_mandir}/man8/multipathd.8.gz

%files devel
%defattr(-,root,root,-)
%{_mandir}/man3/*
%{_includedir}/*
%{_libdir}/pkgconfig/*

%files -n kpartx
%defattr(-,root,root,-)
%{_sbindir}/kpartx
/lib/udev/kpartx_id
%{_mandir}/man8/kpartx.8.gz

%changelog
*   Tue Aug 18 2020 Michelle Wang<michellew@vmware.com> 0.8.3-2
-   Fix how to call json_object_object_get_ex in ./libdmmp/libdmmp_private.h
-   due to json-c 0.15 update json_object_object_get_ex return value
*   Wed Apr 08 2020 Susant Sahani<ssahani@vmware.com> 0.8.3-1
-   Update to 0.8.3
*   Thu Dec 06 2018 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 0.7.3-3
-   Make device-mapper a runtime dependency of kpartx.
*   Wed Sep 26 2018 Anish Swaminathan <anishs@vmware.com>  0.7.3-2
-   Remove rados dependency
*   Wed Oct 04 2017 Dheeraj Shetty <dheerajs@vmware.com> 0.7.3-1
-   Update to 0.7.3
*   Tue May 9  2017 Bo Gan <ganb@vmware.com> 0.7.1-1
-   Update to 0.7.1
*   Fri Nov 18 2016 Anish Swaminathan <anishs@vmware.com>  0.5.0-3
-   Change systemd dependency
*   Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 0.5.0-2
-   GA - Bump release of all rpms
*   Mon Jun 22 2015 Divya Thaluru <dthaluru@vmware.com> 0.5.0-1
-   Initial build. First version

