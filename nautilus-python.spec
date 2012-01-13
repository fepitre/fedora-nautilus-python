%global NAUTILUS_MAYOR_VER  3.0

Name:           nautilus-python
Version:        1.0
Release:        2%{?dist}
Summary:        Python bindings for Nautilus

Group:          Development/Libraries
License:        GPLv2+
URL:            http://www.gnome.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  python-devel
BuildRequires:  nautilus-devel
BuildRequires:  pygobject2-devel
BuildRequires:  gtk-doc
BuildRequires:  autoconf automake libtool

Requires:       nautilus >= 3.0

# Patch0:       https://bugzilla.gnome.org/show_bug.cgi?id=653169
Patch0:         0001-Fixes-bug-653169-Update-the-COPYING-file-with-the-mo.patch
# Patch1:       https://bugzilla.gnome.org/show_bug.cgi?id=652032
Patch1:         0002-Fixes-bug-652032.patch
# Patch2:       https://bugzilla.gnome.org/show_bug.cgi?id=660283
Patch2:         0003-Fix-html-doc-installation-location.patch
# Patch3:       https://bugzilla.gnome.org/show_bug.cgi?id=660286
Patch3:         0004-Fix-underquoted-macro-warning.patch
# Patch4:       https://bugzilla.gnome.org/show_bug.cgi?id=660287
Patch4:         0005-Use-autoconf-s-variable.patch
# Patch5:       https://bugzilla.gnome.org/show_bug.cgi?id=660288
Patch5:         0006-Add-I-m4-to-top-Makefile.am.patch
# Patch6:       https://bugzilla.gnome.org/show_bug.cgi?id=660290
Patch6:         0007-Fix-fsf-address.patch

%description
Python bindings for Nautilus


%package devel
Summary:        Python bindings for Nautilus
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description devel
Python bindings for Nautilus


%prep
%setup -q
find m4 -type f -not -name 'python.m4' -delete
%patch0 -p1 -b .update-licence
%patch1 -p1 -b .bug-652032
%patch2 -p1 -b .fix-html-doc
%patch3 -p1 -b .underquoted-macro-warning
%patch4 -p1 -b .use-docdir-variable
%patch5 -p1 -b .add-I-m4
%patch6 -p1 -b .fix-fsf-address
autoreconf -if -I m4

%build
%configure \
   --enable-gtk-doc \
   --docdir=%{_datadir}/doc/%{name}-%{version}
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/extensions
find $RPM_BUILD_ROOT -name '*.la' -delete

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README AUTHORS COPYING NEWS
%{_libdir}/nautilus/extensions-%{NAUTILUS_MAYOR_VER}/lib%{name}.so
%dir %{_datadir}/%{name}/extensions

%files devel
%defattr(-,root,root,-)
%doc README AUTHORS COPYING NEWS
%{_datadir}/doc/%{name}-%{version}/examples/*.py
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gtk-doc/html/%{name}


%changelog
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 27 2011 Hicham HAOUARI <hicham.haouari@gmail.com> - 1.0-1
- Update to 1.0
- Remove BuildRoot tag and %%clean section
- Own /usr/share/nautilus-python/extensions instead of the old arch
  dependent locations

* Tue Feb 12 2011 Tim Lauridsen <timlau@fedoraproject.org> - 0.7.0-4
- Make it build with latest nautilus

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 26 2010 David Malcolm <dmalcolm@redhat.com> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 25 2010 Patrick Dignan <patrick.dignan at, gmail.com>
- New upstream version 0.7.0
                                                      
* Sun Jul 25 2010 Patrick Dignan <patrick.dignan at, gmail.com>
- Rebuild for F14

* Thu Jan 28 2010 Patrick Dignan <patrick.dignan at, gmail.com>
- New upstream release, bugfixes

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 19 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.5.1-3
- Patch to fix build (thanks to Nicholas Wourms)

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.5.1-2
- Rebuild for Python 2.6

* Wed Sep 24 2008 Trond Danielsen <trondd@fedoraproject.org> - 0.5.1-1
- New upstream version

* Mon Aug 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.4.3-6
- fix license tag

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4.3-5
- Autorebuild for GCC 4.3

* Wed May 02 2007 Trond Danielsen <trond.danielsen@gmail.com> - 0.4.3-4
- Added missing folder. Fixes bug #238591.

* Sat Apr 21 2007 Trond Danielsen <trond.danielsen@gmail.com> - 0.4.3-3
- Moved example code to devel package.

* Thu Apr 19 2007 Jef Spaleta <jspaleta@gmail.com> - 0.4.3-2
- Package review corrections

* Wed Apr 04 2007 Trond Danielsen <trond.danielsen@gmail.com> - 0.4.3-1
- Initial version
