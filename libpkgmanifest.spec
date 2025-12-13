%define major 0
%define libname %mklibname pkgmanifest
%define devname %mklibname pkgmanifest -d

%global optflags %{optflags} -Wno-error=unused-private-field

Name:		libpkgmanifest
Version:	0.5.9
Release:	1
Source0:	https://github.com/rpm-software-management/libpkgmanifest/archive/refs/tags/v%{version}.tar.gz
Summary:	Library for parsing and serializing RPM package manifest files
URL:		https://github.com/rpm-software-management/libpkgmanifest
License:	LGPL-2.1
Group:		System/Libraries
BuildRequires:	cmake
BuildSystem:	cmake
BuildRequires:	pkgconfig(yaml-cpp)
BuildRequires:	pkgconfig(gtest)
BuildRequires:	pkgconfig(gmock)
BuildRequires:	pkgconfig(python)
BuildRequires:	swig

%description
This library provides functionality for parsing and serializing RPM package
manifest files.

It is primarily designed for use by package managers like DNF, which populate
information into manifest files. However, it can also be used directly to
interact with manifest objects in custom applications.

The primary purpose of this library is to streamline internal workflows for
building container images, while also providing foundational building blocks
to tackle general build system management challenges highlighted in this
upstream ticket.

Written in C++ with TDD, the library offers a simple, ABI-compatible API layer
for users. Python bindings are also available, automatically generated from
the C++ API.

%package -n %{libname}
Summary:	Library for parsing and serializing RPM package manifest files
Group:		System/Libraries

%description -n %{libname}
This library provides functionality for parsing and serializing RPM package
manifest files.

It is primarily designed for use by package managers like DNF, which populate
information into manifest files. However, it can also be used directly to
interact with manifest objects in custom applications.

The primary purpose of this library is to streamline internal workflows for
building container images, while also providing foundational building blocks
to tackle general build system management challenges highlighted in this
upstream ticket.

Written in C++ with TDD, the library offers a simple, ABI-compatible API layer
for users. Python bindings are also available, automatically generated from
the C++ API.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

This library provides functionality for parsing and serializing RPM package
manifest files.

It is primarily designed for use by package managers like DNF, which populate
information into manifest files. However, it can also be used directly to
interact with manifest objects in custom applications.

The primary purpose of this library is to streamline internal workflows for
building container images, while also providing foundational building blocks
to tackle general build system management challenges highlighted in this
upstream ticket.

Written in C++ with TDD, the library offers a simple, ABI-compatible API layer
for users. Python bindings are also available, automatically generated from
the C++ API.

%package -n python-%{name}
Summary:	Python bindings for the RPM package manifest library
Group:		Development/Python
Requires:	%{libname} = %{EVRD}

%description -n python-%{name}
Python bindings for the RPM package manifest library

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files -n python-%{name}
%{py_platsitedir}/libpkgmanifest
%{py_platsitedir}/libpkgmanifest-%{version}.dist-info
