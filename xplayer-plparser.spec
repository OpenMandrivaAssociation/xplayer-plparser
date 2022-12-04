%define major  18
%define gi_major 1.0
%define _name   xplayer-pl-parser
%define libname		%mklibname %{name} %{major}
%define libnamemini	%mklibname %{name}-mini %{major}
%define develname	%mklibname %{name} -d
%define girname		%mklibname %{name}-gir %{gi_major}

Name:           xplayer-plparser
Version:        1.0.3
Release:        2
Summary:        Simple GObject-based library to parse playlist formats
License:        LGPL-2.0+
Group:          System/Libraries
Url:            https://github.com/linuxmint/xplayer-plparser
Source:         https://github.com/linuxmint/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  meson
BuildRequires:  gnome-common
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(glib-2.0) >= 2.31.0
BuildRequires:  pkgconfig(gmime-3.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libarchive) >= 3.0
BuildRequires:  pkgconfig(libquvi-0.9) >= 0.9.1
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.43.0
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(gtk-doc)
Requires:       libquvi-scripts

%description
xplayer-plparser is a simple GObject-based library to parse a host
of playlist formats, to save them too.

%lang_package

%package -n %{libname}
Summary:        A simple GObject-based library to parse playlist formats
Group:          System/Libraries
# Main package contains libexec files needed for full functionality.
Requires:       %{name} >= %{version}

%description -n %{libname}
xplayer-plparser is a simple GObject-based library to parse a host
of playlist formats, to save them too.

%package -n %{girname}
Summary:        Simple GObject-based library to parse playlist formats -- Introspection Bindings
Group:          System/Libraries
# Main package contains libexec files needed for full functionality.
Requires:       %{name} >= %{version}

%description -n %{girname}
xplayer-plparser is a simple GObject-based library to parse a host
of playlist formats, to save them too.

This package provides the GObject Introspection bindings for the
xplayer-plparser library.

%package -n %{libnamemini}
Summary:        Simple GObject-based library to parse playlist formats -- Mini Version
Group:          System/Libraries
# Main package contains libexec files needed for full functionality.
Requires:       %{name} >= %{version}

%description -n %{libnamemini}
xplayer-plparser is a simple GObject-based library to parse a host
of playlist formats, to save them too.

%package -n %{develname}
Summary:        Simple GObject-based library to parse playlist formats
Group:          Development/C
Requires:       %{libnamemini} = %{version}
Requires:       %{libname} = %{version}
Requires:       %{girname} = %{version}

%description -n %{develname}
xplayer-plparser is a simple GObject-based library to parse a host
of playlist formats, to save them too.

%prep
%autosetup -p1

%build
%meson \
        -Denable-quvi=yes
%meson_build

%install
%meson_install

find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{_name}

%files  -f %{_name}.lang
%doc COPYING.LIB README debian/changelog
%{_prefix}/libexec/xplayer-pl-parser-videosite
#{_libexecdir}/%{name}/xplayer-pl-parser-videosite

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}{,.*}

%files -n %{girname}
%{_libdir}/girepository-1.0/XplayerPlParser-1.0.typelib

%files -n %{libnamemini}
%{_libdir}/lib%{name}-mini.so.%{major}{,.*}

%files -n %{develname}
%{_includedir}/%{_name}/
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}-mini.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}-mini.pc
%{_datadir}/gir-1.0/*.gir
