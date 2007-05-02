Name:           nautilus-python
Version:        0.4.3
Release:        4%{?dist}
Summary:        Python bindings for Nautilus

Group:          Development/Libraries
License:        GPL
URL:            http://www.gnome.org/
Source0:        http://ftp.acc.umu.se/pub/GNOME/sources/%{name}/0.4/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python-devel
BuildRequires:  nautilus-devel
BuildRequires:  gnome-python2-devel
BuildRequires:  eel2-devel
BuildRequires:  pygtk2-devel
Requires:       nautilus

%description
Python bindings for Nautilus


%package devel
Summary:        Python bindings for Nautilus
Group:          Development/Libraries
License:        GPL
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
rm $RPM_BUILD_ROOT/%{_libdir}/nautilus/extensions-1.0/*.la
rm $RPM_BUILD_ROOT/%{_libdir}/%{name}/*.la
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/nautilus/extensions-1.0/python/
%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README AUTHORS COPYING NEWS
%{_libdir}/%{name}
%{_libdir}/nautilus/extensions-1.0/lib%{name}.*
%dir %{_libdir}/nautilus/extensions-1.0/python/


%files devel
%defattr(-,root,root,-)
%doc installed_docs/examples
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Wed May 02 2007 Trond Danielsen <trond.danielsen@gmail.com> - 0.4.3-4
- Added missing folder. Fixes bug #238591.

* Sat Apr 21 2007 Trond Danielsen <trond.danielsen@gmail.com> - 0.4.3-3
- Moved example code to devel package.

* Thu Apr 19 2007 Jef Spaleta <jspaleta@gmail.com> - 0.4.3-2
- Package review corrections

* Wed Apr 04 2007 Trond Danielsen <trond.danielsen@gmail.com> - 0.4.3-1
- Initial version
