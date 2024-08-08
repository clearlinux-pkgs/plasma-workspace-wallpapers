#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v18
# autospec commit: f35655a
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : plasma-workspace-wallpapers
Version  : 6.1.4
Release  : 101
URL      : https://download.kde.org/stable/plasma/6.1.4/plasma-workspace-wallpapers-6.1.4.tar.xz
Source0  : https://download.kde.org/stable/plasma/6.1.4/plasma-workspace-wallpapers-6.1.4.tar.xz
Source1  : https://download.kde.org/stable/plasma/6.1.4/plasma-workspace-wallpapers-6.1.4.tar.xz.sig
Source2  : D7574483BB57B18D.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-3.0
Requires: plasma-workspace-wallpapers-data = %{version}-%{release}
Requires: plasma-workspace-wallpapers-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Plasma Workspace Wallpapers
Plasma Workspace Wallpapers provides additional wallpapers for Plasma.

%package data
Summary: data components for the plasma-workspace-wallpapers package.
Group: Data

%description data
data components for the plasma-workspace-wallpapers package.


%package license
Summary: license components for the plasma-workspace-wallpapers package.
Group: Default

%description license
license components for the plasma-workspace-wallpapers package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) D7574483BB57B18D' gpg.status
%setup -q -n plasma-workspace-wallpapers-6.1.4
cd %{_builddir}/plasma-workspace-wallpapers-6.1.4
pushd ..
cp -a plasma-workspace-wallpapers-6.1.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1723134306
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1723134306
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/plasma-workspace-wallpapers
cp %{_builddir}/plasma-workspace-wallpapers-%{version}/COPYING %{buildroot}/usr/share/package-licenses/plasma-workspace-wallpapers/7c203dee3a03037da436df03c4b25b659c073976 || :
cp %{_builddir}/plasma-workspace-wallpapers-%{version}/COPYING.LGPL3 %{buildroot}/usr/share/package-licenses/plasma-workspace-wallpapers/f45ee1c765646813b442ca58de72e20a64a7ddba || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/wallpapers/Altai/contents/images/1080x1920.png
/usr/share/wallpapers/Altai/contents/images/5120x2880.png
/usr/share/wallpapers/Altai/contents/screenshot.png
/usr/share/wallpapers/Altai/metadata.json
/usr/share/wallpapers/Autumn/contents/images/1280x1024.jpg
/usr/share/wallpapers/Autumn/contents/images/1280x800.jpg
/usr/share/wallpapers/Autumn/contents/images/1440x900.jpg
/usr/share/wallpapers/Autumn/contents/images/1600x1200.jpg
/usr/share/wallpapers/Autumn/contents/images/1638x1024.jpg
/usr/share/wallpapers/Autumn/contents/images/1680x1050.jpg
/usr/share/wallpapers/Autumn/contents/images/1920x1080.jpg
/usr/share/wallpapers/Autumn/contents/images/1920x1200.jpg
/usr/share/wallpapers/Autumn/contents/images/2560x1440.jpg
/usr/share/wallpapers/Autumn/contents/images/2560x1600.jpg
/usr/share/wallpapers/Autumn/contents/images/640x480.jpg
/usr/share/wallpapers/Autumn/contents/images/800x600.jpg
/usr/share/wallpapers/Autumn/contents/screenshot.jpg
/usr/share/wallpapers/Autumn/metadata.json
/usr/share/wallpapers/BytheWater/contents/images/1280x1024.jpg
/usr/share/wallpapers/BytheWater/contents/images/1280x800.jpg
/usr/share/wallpapers/BytheWater/contents/images/1440x900.jpg
/usr/share/wallpapers/BytheWater/contents/images/1600x1200.jpg
/usr/share/wallpapers/BytheWater/contents/images/1638x1024.jpg
/usr/share/wallpapers/BytheWater/contents/images/1680x1050.jpg
/usr/share/wallpapers/BytheWater/contents/images/1920x1080.jpg
/usr/share/wallpapers/BytheWater/contents/images/1920x1200.jpg
/usr/share/wallpapers/BytheWater/contents/images/2560x1440.jpg
/usr/share/wallpapers/BytheWater/contents/images/2560x1600.jpg
/usr/share/wallpapers/BytheWater/contents/images/640x480.jpg
/usr/share/wallpapers/BytheWater/contents/images/800x600.jpg
/usr/share/wallpapers/BytheWater/contents/screenshot.jpg
/usr/share/wallpapers/BytheWater/metadata.json
/usr/share/wallpapers/Canopee/contents/images/3840x2160.png
/usr/share/wallpapers/Canopee/contents/screenshot.png
/usr/share/wallpapers/Canopee/metadata.json
/usr/share/wallpapers/Cascade/contents/images/3840x2160.png
/usr/share/wallpapers/Cascade/contents/screenshot.png
/usr/share/wallpapers/Cascade/metadata.json
/usr/share/wallpapers/Cluster/contents/images/3840x2160.png
/usr/share/wallpapers/Cluster/contents/screenshot.png
/usr/share/wallpapers/Cluster/metadata.json
/usr/share/wallpapers/ColdRipple/contents/images/1280x1024.jpg
/usr/share/wallpapers/ColdRipple/contents/images/1280x800.jpg
/usr/share/wallpapers/ColdRipple/contents/images/1440x900.jpg
/usr/share/wallpapers/ColdRipple/contents/images/1600x1200.jpg
/usr/share/wallpapers/ColdRipple/contents/images/1638x1024.jpg
/usr/share/wallpapers/ColdRipple/contents/images/1680x1050.jpg
/usr/share/wallpapers/ColdRipple/contents/images/1920x1080.jpg
/usr/share/wallpapers/ColdRipple/contents/images/1920x1200.jpg
/usr/share/wallpapers/ColdRipple/contents/images/2560x1440.jpg
/usr/share/wallpapers/ColdRipple/contents/images/2560x1600.jpg
/usr/share/wallpapers/ColdRipple/contents/images/640x480.jpg
/usr/share/wallpapers/ColdRipple/contents/images/800x600.jpg
/usr/share/wallpapers/ColdRipple/contents/screenshot.jpg
/usr/share/wallpapers/ColdRipple/metadata.json
/usr/share/wallpapers/ColorfulCups/contents/images/2560x1600.jpg
/usr/share/wallpapers/ColorfulCups/contents/screenshot.jpg
/usr/share/wallpapers/ColorfulCups/metadata.json
/usr/share/wallpapers/DarkestHour/contents/images/1280x1024.jpg
/usr/share/wallpapers/DarkestHour/contents/images/1280x800.jpg
/usr/share/wallpapers/DarkestHour/contents/images/1440x900.jpg
/usr/share/wallpapers/DarkestHour/contents/images/1600x1200.jpg
/usr/share/wallpapers/DarkestHour/contents/images/1638x1024.jpg
/usr/share/wallpapers/DarkestHour/contents/images/1680x1050.jpg
/usr/share/wallpapers/DarkestHour/contents/images/1920x1080.jpg
/usr/share/wallpapers/DarkestHour/contents/images/1920x1200.jpg
/usr/share/wallpapers/DarkestHour/contents/images/2560x1440.jpg
/usr/share/wallpapers/DarkestHour/contents/images/2560x1600.jpg
/usr/share/wallpapers/DarkestHour/contents/images/640x480.jpg
/usr/share/wallpapers/DarkestHour/contents/images/800x600.jpg
/usr/share/wallpapers/DarkestHour/contents/screenshot.jpg
/usr/share/wallpapers/DarkestHour/metadata.json
/usr/share/wallpapers/Elarun/contents/images/2560x1600.png
/usr/share/wallpapers/Elarun/contents/screenshot.jpg
/usr/share/wallpapers/Elarun/metadata.json
/usr/share/wallpapers/EveningGlow/contents/images/1280x1024.jpg
/usr/share/wallpapers/EveningGlow/contents/images/1280x800.jpg
/usr/share/wallpapers/EveningGlow/contents/images/1440x900.jpg
/usr/share/wallpapers/EveningGlow/contents/images/1600x1200.jpg
/usr/share/wallpapers/EveningGlow/contents/images/1638x1024.jpg
/usr/share/wallpapers/EveningGlow/contents/images/1680x1050.jpg
/usr/share/wallpapers/EveningGlow/contents/images/1920x1080.jpg
/usr/share/wallpapers/EveningGlow/contents/images/1920x1200.jpg
/usr/share/wallpapers/EveningGlow/contents/images/2560x1440.jpg
/usr/share/wallpapers/EveningGlow/contents/images/2560x1600.jpg
/usr/share/wallpapers/EveningGlow/contents/images/640x480.jpg
/usr/share/wallpapers/EveningGlow/contents/images/800x600.jpg
/usr/share/wallpapers/EveningGlow/contents/screenshot.jpg
/usr/share/wallpapers/EveningGlow/metadata.json
/usr/share/wallpapers/FallenLeaf/contents/images/1280x1024.jpg
/usr/share/wallpapers/FallenLeaf/contents/images/1280x800.jpg
/usr/share/wallpapers/FallenLeaf/contents/images/1440x900.jpg
/usr/share/wallpapers/FallenLeaf/contents/images/1600x1200.jpg
/usr/share/wallpapers/FallenLeaf/contents/images/1638x1024.jpg
/usr/share/wallpapers/FallenLeaf/contents/images/1680x1050.jpg
/usr/share/wallpapers/FallenLeaf/contents/images/1920x1080.jpg
/usr/share/wallpapers/FallenLeaf/contents/images/1920x1200.jpg
/usr/share/wallpapers/FallenLeaf/contents/images/2560x1440.jpg
/usr/share/wallpapers/FallenLeaf/contents/images/2560x1600.jpg
/usr/share/wallpapers/FallenLeaf/contents/images/640x480.jpg
/usr/share/wallpapers/FallenLeaf/contents/images/800x600.jpg
/usr/share/wallpapers/FallenLeaf/contents/screenshot.jpg
/usr/share/wallpapers/FallenLeaf/metadata.json
/usr/share/wallpapers/Flow/contents/images/5120x2880.jpg
/usr/share/wallpapers/Flow/contents/images/720x1440.jpg
/usr/share/wallpapers/Flow/contents/images_dark/5120x2880.jpg
/usr/share/wallpapers/Flow/contents/images_dark/720x1440.jpg
/usr/share/wallpapers/Flow/contents/screenshot.png
/usr/share/wallpapers/Flow/metadata.json
/usr/share/wallpapers/FlyingKonqui/contents/images/1280x1024.png
/usr/share/wallpapers/FlyingKonqui/contents/images/1280x800.png
/usr/share/wallpapers/FlyingKonqui/contents/images/1440x900.png
/usr/share/wallpapers/FlyingKonqui/contents/images/1600x1200.png
/usr/share/wallpapers/FlyingKonqui/contents/images/1638x1024.png
/usr/share/wallpapers/FlyingKonqui/contents/images/1680x1050.png
/usr/share/wallpapers/FlyingKonqui/contents/images/1920x1080.png
/usr/share/wallpapers/FlyingKonqui/contents/images/1920x1200.png
/usr/share/wallpapers/FlyingKonqui/contents/images/2560x1440.png
/usr/share/wallpapers/FlyingKonqui/contents/images/2560x1600.png
/usr/share/wallpapers/FlyingKonqui/contents/images/640x480.png
/usr/share/wallpapers/FlyingKonqui/contents/images/800x600.png
/usr/share/wallpapers/FlyingKonqui/contents/screenshot.png
/usr/share/wallpapers/FlyingKonqui/metadata.json
/usr/share/wallpapers/Grey/contents/images/1280x1024.jpg
/usr/share/wallpapers/Grey/contents/images/1280x800.jpg
/usr/share/wallpapers/Grey/contents/images/1440x900.jpg
/usr/share/wallpapers/Grey/contents/images/1600x1200.jpg
/usr/share/wallpapers/Grey/contents/images/1638x1024.jpg
/usr/share/wallpapers/Grey/contents/images/1680x1050.jpg
/usr/share/wallpapers/Grey/contents/images/1920x1080.jpg
/usr/share/wallpapers/Grey/contents/images/1920x1200.jpg
/usr/share/wallpapers/Grey/contents/images/2560x1440.jpg
/usr/share/wallpapers/Grey/contents/images/2560x1600.jpg
/usr/share/wallpapers/Grey/contents/images/640x480.jpg
/usr/share/wallpapers/Grey/contents/images/800x600.jpg
/usr/share/wallpapers/Grey/contents/screenshot.jpg
/usr/share/wallpapers/Grey/metadata.json
/usr/share/wallpapers/Honeywave/contents/images/1080x1920.jpg
/usr/share/wallpapers/Honeywave/contents/images/5120x2880.jpg
/usr/share/wallpapers/Honeywave/contents/screenshot.png
/usr/share/wallpapers/Honeywave/metadata.json
/usr/share/wallpapers/IceCold/contents/images/5120x2880.png
/usr/share/wallpapers/IceCold/contents/screenshot.png
/usr/share/wallpapers/IceCold/metadata.json
/usr/share/wallpapers/Kay/contents/images/1080x1920.png
/usr/share/wallpapers/Kay/contents/images/5120x2880.png
/usr/share/wallpapers/Kay/contents/images_dark/1080x1920.png
/usr/share/wallpapers/Kay/contents/images_dark/5120x2880.png
/usr/share/wallpapers/Kay/metadata.json
/usr/share/wallpapers/Kite/contents/images/1280x1024.jpg
/usr/share/wallpapers/Kite/contents/images/1280x800.jpg
/usr/share/wallpapers/Kite/contents/images/1440x900.jpg
/usr/share/wallpapers/Kite/contents/images/1600x1200.jpg
/usr/share/wallpapers/Kite/contents/images/1638x1024.jpg
/usr/share/wallpapers/Kite/contents/images/1680x1050.jpg
/usr/share/wallpapers/Kite/contents/images/1920x1080.jpg
/usr/share/wallpapers/Kite/contents/images/1920x1200.jpg
/usr/share/wallpapers/Kite/contents/images/2560x1440.jpg
/usr/share/wallpapers/Kite/contents/images/2560x1600.jpg
/usr/share/wallpapers/Kite/contents/images/640x480.jpg
/usr/share/wallpapers/Kite/contents/images/800x600.jpg
/usr/share/wallpapers/Kite/contents/screenshot.jpg
/usr/share/wallpapers/Kite/metadata.json
/usr/share/wallpapers/Kokkini/contents/images/3840x2160.png
/usr/share/wallpapers/Kokkini/contents/screenshot.png
/usr/share/wallpapers/Kokkini/metadata.json
/usr/share/wallpapers/MilkyWay/contents/images/1080x1920.png
/usr/share/wallpapers/MilkyWay/contents/images/5120x2880.png
/usr/share/wallpapers/MilkyWay/contents/screenshot.png
/usr/share/wallpapers/MilkyWay/metadata.json
/usr/share/wallpapers/Mountain/contents/images/1080x1920.png
/usr/share/wallpapers/Mountain/contents/images/5120x2880.png
/usr/share/wallpapers/Mountain/contents/images_dark/1080x1920.png
/usr/share/wallpapers/Mountain/contents/images_dark/5120x2880.png
/usr/share/wallpapers/Mountain/metadata.json
/usr/share/wallpapers/OneStandsOut/contents/images/1280x1024.jpg
/usr/share/wallpapers/OneStandsOut/contents/images/1280x800.jpg
/usr/share/wallpapers/OneStandsOut/contents/images/1440x900.jpg
/usr/share/wallpapers/OneStandsOut/contents/images/1600x1200.jpg
/usr/share/wallpapers/OneStandsOut/contents/images/1638x1024.jpg
/usr/share/wallpapers/OneStandsOut/contents/images/1680x1050.jpg
/usr/share/wallpapers/OneStandsOut/contents/images/1920x1080.jpg
/usr/share/wallpapers/OneStandsOut/contents/images/1920x1200.jpg
/usr/share/wallpapers/OneStandsOut/contents/images/2560x1440.jpg
/usr/share/wallpapers/OneStandsOut/contents/images/2560x1600.jpg
/usr/share/wallpapers/OneStandsOut/contents/images/640x480.jpg
/usr/share/wallpapers/OneStandsOut/contents/images/800x600.jpg
/usr/share/wallpapers/OneStandsOut/contents/screenshot.jpg
/usr/share/wallpapers/OneStandsOut/metadata.json
/usr/share/wallpapers/Opal/contents/images/3840x2160.png
/usr/share/wallpapers/Opal/contents/screenshot.png
/usr/share/wallpapers/Opal/metadata.json
/usr/share/wallpapers/PastelHills/contents/images/1280x1024.jpg
/usr/share/wallpapers/PastelHills/contents/images/1280x800.jpg
/usr/share/wallpapers/PastelHills/contents/images/1440x900.jpg
/usr/share/wallpapers/PastelHills/contents/images/1600x1200.jpg
/usr/share/wallpapers/PastelHills/contents/images/1638x1024.jpg
/usr/share/wallpapers/PastelHills/contents/images/1680x1050.jpg
/usr/share/wallpapers/PastelHills/contents/images/1920x1080.jpg
/usr/share/wallpapers/PastelHills/contents/images/1920x1200.jpg
/usr/share/wallpapers/PastelHills/contents/images/2560x1440.jpg
/usr/share/wallpapers/PastelHills/contents/images/3200x2000.jpg
/usr/share/wallpapers/PastelHills/contents/images/640x480.jpg
/usr/share/wallpapers/PastelHills/contents/images/800x600.jpg
/usr/share/wallpapers/PastelHills/contents/screenshot.jpg
/usr/share/wallpapers/PastelHills/metadata.json
/usr/share/wallpapers/Patak/contents/images/1080x1920.png
/usr/share/wallpapers/Patak/contents/images/5120x2880.png
/usr/share/wallpapers/Patak/contents/images_dark/3840x2160.png
/usr/share/wallpapers/Patak/contents/screenshot.png
/usr/share/wallpapers/Patak/metadata.json
/usr/share/wallpapers/Path/contents/images/1280x1024.jpg
/usr/share/wallpapers/Path/contents/images/1280x800.jpg
/usr/share/wallpapers/Path/contents/images/1440x900.jpg
/usr/share/wallpapers/Path/contents/images/1600x1200.jpg
/usr/share/wallpapers/Path/contents/images/1638x1024.jpg
/usr/share/wallpapers/Path/contents/images/1680x1050.jpg
/usr/share/wallpapers/Path/contents/images/1920x1080.jpg
/usr/share/wallpapers/Path/contents/images/1920x1200.jpg
/usr/share/wallpapers/Path/contents/images/2560x1440.jpg
/usr/share/wallpapers/Path/contents/images/2560x1600.jpg
/usr/share/wallpapers/Path/contents/images/640x480.jpg
/usr/share/wallpapers/Path/contents/images/800x600.jpg
/usr/share/wallpapers/Path/contents/screenshot.jpg
/usr/share/wallpapers/Path/metadata.json
/usr/share/wallpapers/SafeLanding/contents/images/1622x2880.jpg
/usr/share/wallpapers/SafeLanding/contents/images/5120x2880.jpg
/usr/share/wallpapers/SafeLanding/contents/screenshot.jpg
/usr/share/wallpapers/SafeLanding/metadata.json
/usr/share/wallpapers/Shell/contents/images/5120x2880.jpg
/usr/share/wallpapers/Shell/contents/images/720x1440.jpg
/usr/share/wallpapers/Shell/contents/screenshot.png
/usr/share/wallpapers/Shell/metadata.json
/usr/share/wallpapers/Volna/contents/images/5120x2880.jpg
/usr/share/wallpapers/Volna/contents/screenshot.png
/usr/share/wallpapers/Volna/metadata.json
/usr/share/wallpapers/summer_1am/contents/images/1280x1024.jpg
/usr/share/wallpapers/summer_1am/contents/images/1280x800.jpg
/usr/share/wallpapers/summer_1am/contents/images/1440x900.jpg
/usr/share/wallpapers/summer_1am/contents/images/1600x1200.jpg
/usr/share/wallpapers/summer_1am/contents/images/1638x1024.jpg
/usr/share/wallpapers/summer_1am/contents/images/1680x1050.jpg
/usr/share/wallpapers/summer_1am/contents/images/1920x1080.jpg
/usr/share/wallpapers/summer_1am/contents/images/1920x1200.jpg
/usr/share/wallpapers/summer_1am/contents/images/2560x1440.jpg
/usr/share/wallpapers/summer_1am/contents/images/2560x1600.jpg
/usr/share/wallpapers/summer_1am/contents/images/640x480.jpg
/usr/share/wallpapers/summer_1am/contents/images/800x600.jpg
/usr/share/wallpapers/summer_1am/contents/screenshot.jpg
/usr/share/wallpapers/summer_1am/metadata.json

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/plasma-workspace-wallpapers/7c203dee3a03037da436df03c4b25b659c073976
/usr/share/package-licenses/plasma-workspace-wallpapers/f45ee1c765646813b442ca58de72e20a64a7ddba
