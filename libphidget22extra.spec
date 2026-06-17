Name:           libphidget22extra
Version:        1.25.20260512
Release:        %autorelease
Summary:        Drivers and API for Phidget devices
License:        LGPL-3.0-or-later and BSD-2-Clause and BSD-3-Clause
URL:            https://www.phidgets.com
Source0:        https://www.phidgets.com/downloads/phidget22/libraries/linux/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  libphidget22-devel
BuildRequires:  autoconf
BuildRequires:  avahi-compat-libdns_sd-devel
BuildRequires:  avahi-devel
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  libusb1-devel
BuildRequires:  make
BuildRequires:  udev

Requires:       libphidget22
Requires:       avahi-compat-libdns_sd
Requires:       udev

%description
Phidgets are a set of "plug and play" building blocks for low cost USB
sensing and control from your PC.  All the USB complexity is taken care
of by the robust libphidget API.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup

%build
%configure --disable-silent-rules --disable-static --enable-zeroconf=avahi --disable-ldconfig --enable-jni
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%doc AUTHORS README
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/%{name}/
%{_includedir}/%{name}.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog