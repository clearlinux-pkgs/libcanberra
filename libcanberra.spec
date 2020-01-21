#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libcanberra
Version  : 0.30
Release  : 16
URL      : http://0pointer.de/lennart/projects/libcanberra/libcanberra-0.30.tar.xz
Source0  : http://0pointer.de/lennart/projects/libcanberra/libcanberra-0.30.tar.xz
Summary  : Event Sound API
Group    : Development/Tools
License  : LGPL-2.1
Requires: libcanberra-bin = %{version}-%{release}
Requires: libcanberra-data = %{version}-%{release}
Requires: libcanberra-lib = %{version}-%{release}
BuildRequires : cairo-dev32
BuildRequires : docbook-xml
BuildRequires : fontconfig-dev32
BuildRequires : freetype-dev32
BuildRequires : fribidi-dev
BuildRequires : fribidi-dev32
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : gdk-pixbuf-dev32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libtool-dev
BuildRequires : libtool-dev32
BuildRequires : libxslt-bin
BuildRequires : pango-dev32
BuildRequires : pkg-config
BuildRequires : pkgconfig(32alsa)
BuildRequires : pkgconfig(32atk)
BuildRequires : pkgconfig(32gdk-2.0)
BuildRequires : pkgconfig(32gdk-3.0)
BuildRequires : pkgconfig(32glib-2.0)
BuildRequires : pkgconfig(32gstreamer-1.0)
BuildRequires : pkgconfig(32gthread-2.0)
BuildRequires : pkgconfig(32gtk+-2.0)
BuildRequires : pkgconfig(32gtk+-3.0)
BuildRequires : pkgconfig(32harfbuzz)
BuildRequires : pkgconfig(32libpulse)
BuildRequires : pkgconfig(32libudev)
BuildRequires : pkgconfig(32vorbisfile)
BuildRequires : pkgconfig(32x11)
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(atk)
BuildRequires : pkgconfig(gdk-2.0)
BuildRequires : pkgconfig(gdk-3.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gstreamer-1.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(harfbuzz)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(vorbisfile)
BuildRequires : pkgconfig(x11)

%description
libcanberra 0.30
(dot) de>
* [1]License
* [2]News
* [3]Overview
* [4]Current Status
* [5]Documentation
* [6]Requirements
* [7]Installation
* [8]Acknowledgements
* [9]Download

%package bin
Summary: bin components for the libcanberra package.
Group: Binaries
Requires: libcanberra-data = %{version}-%{release}

%description bin
bin components for the libcanberra package.


%package data
Summary: data components for the libcanberra package.
Group: Data

%description data
data components for the libcanberra package.


%package dev
Summary: dev components for the libcanberra package.
Group: Development
Requires: libcanberra-lib = %{version}-%{release}
Requires: libcanberra-bin = %{version}-%{release}
Requires: libcanberra-data = %{version}-%{release}
Provides: libcanberra-devel = %{version}-%{release}
Requires: libcanberra = %{version}-%{release}

%description dev
dev components for the libcanberra package.


%package dev32
Summary: dev32 components for the libcanberra package.
Group: Default
Requires: libcanberra-lib32 = %{version}-%{release}
Requires: libcanberra-bin = %{version}-%{release}
Requires: libcanberra-data = %{version}-%{release}
Requires: libcanberra-dev = %{version}-%{release}

%description dev32
dev32 components for the libcanberra package.


%package doc
Summary: doc components for the libcanberra package.
Group: Documentation

%description doc
doc components for the libcanberra package.


%package lib
Summary: lib components for the libcanberra package.
Group: Libraries
Requires: libcanberra-data = %{version}-%{release}

%description lib
lib components for the libcanberra package.


%package lib32
Summary: lib32 components for the libcanberra package.
Group: Default
Requires: libcanberra-data = %{version}-%{release}

%description lib32
lib32 components for the libcanberra package.


%prep
%setup -q -n libcanberra-0.30
cd %{_builddir}/libcanberra-0.30
pushd ..
cp -a libcanberra-0.30 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1579639230
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static --disable-oss --disable-alsa --disable-gstreamer --disable-tdb
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static --disable-oss --disable-alsa --disable-gstreamer --disable-tdb --disable-oss  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check
cd ../build32;
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1579639230
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)
/usr/lib32/gnome-settings-daemon-3.0/gtk-modules/canberra-gtk-module.desktop
/usr/lib64/gnome-settings-daemon-3.0/gtk-modules/canberra-gtk-module.desktop

%files bin
%defattr(-,root,root,-)
/usr/bin/canberra-gtk-play

%files data
%defattr(-,root,root,-)
/usr/share/gdm/autostart/LoginWindow/libcanberra-ready-sound.desktop
/usr/share/gnome/autostart/libcanberra-login-sound.desktop
/usr/share/gnome/shutdown/libcanberra-logout-sound.sh
/usr/share/vala/vapi/libcanberra-gtk.vapi
/usr/share/vala/vapi/libcanberra.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/canberra-gtk.h
/usr/include/canberra.h
/usr/lib64/libcanberra-gtk.so
/usr/lib64/libcanberra-gtk3.so
/usr/lib64/libcanberra.so
/usr/lib64/pkgconfig/libcanberra-gtk.pc
/usr/lib64/pkgconfig/libcanberra-gtk3.pc
/usr/lib64/pkgconfig/libcanberra.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libcanberra-gtk.so
/usr/lib32/libcanberra-gtk3.so
/usr/lib32/libcanberra.so
/usr/lib32/pkgconfig/32libcanberra-gtk.pc
/usr/lib32/pkgconfig/32libcanberra-gtk3.pc
/usr/lib32/pkgconfig/32libcanberra.pc
/usr/lib32/pkgconfig/libcanberra-gtk.pc
/usr/lib32/pkgconfig/libcanberra-gtk3.pc
/usr/lib32/pkgconfig/libcanberra.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libcanberra/*
/usr/share/gtk-doc/html/libcanberra/ch01.html
/usr/share/gtk-doc/html/libcanberra/home.png
/usr/share/gtk-doc/html/libcanberra/index.html
/usr/share/gtk-doc/html/libcanberra/index.sgml
/usr/share/gtk-doc/html/libcanberra/left.png
/usr/share/gtk-doc/html/libcanberra/libcanberra-canberra-gtk.html
/usr/share/gtk-doc/html/libcanberra/libcanberra-canberra.html
/usr/share/gtk-doc/html/libcanberra/libcanberra.devhelp2
/usr/share/gtk-doc/html/libcanberra/right.png
/usr/share/gtk-doc/html/libcanberra/style.css
/usr/share/gtk-doc/html/libcanberra/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/gtk-2.0/modules/libcanberra-gtk-module.so
/usr/lib64/gtk-3.0/modules/libcanberra-gtk-module.so
/usr/lib64/gtk-3.0/modules/libcanberra-gtk3-module.so
/usr/lib64/libcanberra-0.30/libcanberra-multi.so
/usr/lib64/libcanberra-0.30/libcanberra-null.so
/usr/lib64/libcanberra-0.30/libcanberra-pulse.so
/usr/lib64/libcanberra-gtk.so.0
/usr/lib64/libcanberra-gtk.so.0.1.9
/usr/lib64/libcanberra-gtk3.so.0
/usr/lib64/libcanberra-gtk3.so.0.1.9
/usr/lib64/libcanberra.so.0
/usr/lib64/libcanberra.so.0.2.5

%files lib32
%defattr(-,root,root,-)
/usr/lib32/gtk-2.0/modules/libcanberra-gtk-module.so
/usr/lib32/gtk-3.0/modules/libcanberra-gtk-module.so
/usr/lib32/gtk-3.0/modules/libcanberra-gtk3-module.so
/usr/lib32/libcanberra-0.30/libcanberra-multi.so
/usr/lib32/libcanberra-0.30/libcanberra-null.so
/usr/lib32/libcanberra-0.30/libcanberra-pulse.so
/usr/lib32/libcanberra-gtk.so.0
/usr/lib32/libcanberra-gtk.so.0.1.9
/usr/lib32/libcanberra-gtk3.so.0
/usr/lib32/libcanberra-gtk3.so.0.1.9
/usr/lib32/libcanberra.so.0
/usr/lib32/libcanberra.so.0.2.5
