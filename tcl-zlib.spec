%define oname zlib

Summary:	Zlib support for Tcl
Name:		tcl-%{oname}
Version:	2.0.1
Release:	0.svn40.2
Group:		System/Libraries
License:	MIT
Url:		http://svn.scheffers.net/
# Snapshot of SVN40 downloaded on June 26, 2008
# Originally found at http://svn.scheffers.net/zlib.tar.gz
Source0:	%{oname}.tar.gz
BuildRequires:	tcl-devel
BuildRequires:	pkgconfig(tk)
BuildRequires:	pkgconfig(zlib)

%description
This is extension is a standalone version of the tclkit [zlib]
command/extension. See http://wiki.tcl.tk/zlib for command syntax.

%files
%doc README ChangeLog
%dir %{tcl_sitearch}/%{oname}%{version}
%{tcl_sitearch}/%{oname}%{version}/*.so
%{tcl_sitearch}/%{oname}%{version}/pkgIndex.tcl
%{_libdir}/*.so

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description devel
Development files for %{name}.

%files devel
%{tcl_sitearch}/%{oname}%{version}/libzlibstub*.a
%{_includedir}/*.h

#----------------------------------------------------------------------------

%prep
%setup -q -n %{oname}

%build
%configure2_5x \
	--with-tcl=%{_libdir}
make

%install
make DESTDIR=%{buildroot} install-binaries install-libraries

install -d %{buildroot}%{tcl_sitearch}
mv %{buildroot}%{_libdir}/%{oname}%{version} %{buildroot}%{tcl_sitearch}/%{oname}%{version}
ln -s tcl%{tcl_version}/%{oname}%{version}/lib%{oname}%{version}.so %{buildroot}%{_libdir}/lib%{oname}%{version}.so

rm -rf %{buildroot}%{tcl_sitearch}/%{oname}%{version}/zlib.c
chmod -x %{buildroot}%{tcl_sitearch}/%{oname}%{version}/libzlibstub*.a

