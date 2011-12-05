Name: libcxgb3
Version: 1.2.5
Release: 4%{?dist}
Summary: Chelsio T3 iWARP HCA Userspace Driver
Group: System Environment/Libraries
License: GPLv2 or BSD
Url: http://www.openfabrics.org/
Source: http://www.openfabrics.org/downloads/cxgb3/%{name}-%{version}.tar.gz
Source1: libcxgb3-modprobe.conf
Patch0: libcxgb3-1.2.5-verbs-api.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: libibverbs-devel >= 1.1.3, libtool
Obsoletes: %{name}-devel
ExcludeArch: s390 s390x
Provides: libibverbs-driver
%description
Userspace hardware driver for use with the libibverbs InfiniBand/iWARP verbs
library.  This driver enables Chelsio iWARP capable ethernet devices.

%package static
Summary: Static version of the libcxgb3 driver
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}
%description static
Static version of libcxgb3 that may be linked directly to an application.

%prep
%setup -q
%patch0 -p1 -b .api

%build
%configure
%{__make} %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
install -p -m 644 -D %{SOURCE1} ${RPM_BUILD_ROOT}%{_sysconfdir}/modprobe.d/libcxgb3.conf
# remove unpackaged files from the buildroot
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/*.so*
%{_sysconfdir}/libibverbs.d/*.driver
%{_sysconfdir}/modprobe.d/libcxgb3.conf
%doc AUTHORS COPYING README

%files static
%defattr(-,root,root,-)
%{_libdir}/*.a

%changelog
* Mon Jan 11 2010 Doug Ledford <dledford@redhat.com> - 1.2.5-4
- ExcludeArch s390(x) as the hardware doesn't exist there

* Fri Nov 06 2009 Doug Ledford <dledford@redhat.com> - 1.2.5-3
- Update BuildRequires to reflect the necessary libibverbs release for the
  new verbs API change

* Fri Nov 06 2009 Doug Ledford <dledford@redhat.com> - 1.2.5-2
- Update to libibverbs-1.1.3 API

* Wed Oct 28 2009 Doug Ledford <dledford@redhat.com> - 1.2.5-1
- Update to latest version
- Add provides of libibverbs-driver

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jun 12 2008 Doug Ledford <dledford@redhat.com> - 1.2.1-1
- Update to latest upstream version
- Submit package to Fedora review process

* Tue Apr 01 2008 Doug Ledford <dledford@redhat.com> - 1.1.4-1
- Update to 1.1.4 to match OFED 1.3
- Add a modprobe conf file in /etc/modprobe.d so that the iw_cxgb3 module
  will always be loaded after the cxgb3 net module
- Related: bz428197

* Thu Feb 14 2008 Doug Ledford <dledford@redhat.com> - 1.1.2-2
- Obsolete the old -devel package (which really was just a static
  lib, no real devel environment, hence the name change to -static)
- Resolves: bz432769

* Fri Jan 25 2008 Doug Ledford <dledford@redhat.com> - 1.1.2-1
- Build against latest libibverbs
- Related: bz428197

* Tue Jan 15 2008 Doug Ledford <dledford@redhat.com> - 1.1.2-0.1
- Initial driver import

