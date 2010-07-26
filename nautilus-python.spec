Name:           nautilus-python
Version:        0.7.0
Release:        2%{?dist}
Summary:        Python bindings for Nautilus

Group:          Development/Libraries
License:        GPLv2+
URL:            http://www.gnome.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%{name}/0.7/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python-devel
BuildRequires:  nautilus-devel
BuildRequires:  gnome-vfs2-devel
BuildRequires:  gnome-python2-devel
BuildRequires:  pygtk2-devel
Requires:       nautilus

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

%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT/%{_docdir}/%{name} installed_docs
rm $RPM_BUILD_ROOT/%{_libdir}/nautilus/extensions-2.0/*.la
rm $RPM_BUILD_ROOT/%{_libdir}/%{name}/*.la
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/nautilus/extensions-2.0/python/

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README AUTHORS COPYING NEWS
%{_libdir}/%{name}
%{_libdir}/nautilus/extensions-2.0/lib%{name}.*
%dir %{_libdir}/nautilus/extensions-2.0/python/


%files devel
%defattr(-,root,root,-)
%doc installed_docs/examples
%{_libdir}/pkgconfig/%{name}.pc


%changelog
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
