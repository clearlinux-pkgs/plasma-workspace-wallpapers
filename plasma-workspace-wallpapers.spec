#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : plasma-workspace-wallpapers
Version  : 5.14.1
Release  : 5
URL      : https://download.kde.org/stable/plasma/5.14.1/plasma-workspace-wallpapers-5.14.1.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.14.1/plasma-workspace-wallpapers-5.14.1.tar.xz
Source99 : https://download.kde.org/stable/plasma/5.14.1/plasma-workspace-wallpapers-5.14.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-3.0
Requires: plasma-workspace-wallpapers-data = %{version}-%{release}
Requires: plasma-workspace-wallpapers-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde

%description
No detailed description available

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
%setup -q -n plasma-workspace-wallpapers-5.14.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539735008
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1539735008
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/plasma-workspace-wallpapers
cp COPYING %{buildroot}/usr/share/package-licenses/plasma-workspace-wallpapers/COPYING
cp COPYING.LGPL3 %{buildroot}/usr/share/package-licenses/plasma-workspace-wallpapers/COPYING.LGPL3
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
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
/usr/share/wallpapers/Autumn/metadata.desktop
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
/usr/share/wallpapers/BytheWater/metadata.desktop
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
/usr/share/wallpapers/ColdRipple/metadata.desktop
/usr/share/wallpapers/ColorfulCups/contents/images/1280x1024.jpg
/usr/share/wallpapers/ColorfulCups/contents/images/1280x800.jpg
/usr/share/wallpapers/ColorfulCups/contents/images/1440x900.jpg
/usr/share/wallpapers/ColorfulCups/contents/images/1600x1200.jpg
/usr/share/wallpapers/ColorfulCups/contents/images/1638x1024.jpg
/usr/share/wallpapers/ColorfulCups/contents/images/1680x1050.jpg
/usr/share/wallpapers/ColorfulCups/contents/images/1920x1080.jpg
/usr/share/wallpapers/ColorfulCups/contents/images/1920x1200.jpg
/usr/share/wallpapers/ColorfulCups/contents/images/2560x1440.jpg
/usr/share/wallpapers/ColorfulCups/contents/images/2560x1600.jpg
/usr/share/wallpapers/ColorfulCups/contents/images/640x480.jpg
/usr/share/wallpapers/ColorfulCups/contents/images/800x600.jpg
/usr/share/wallpapers/ColorfulCups/contents/screenshot.jpg
/usr/share/wallpapers/ColorfulCups/metadata.desktop
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
/usr/share/wallpapers/DarkestHour/metadata.desktop
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
/usr/share/wallpapers/EveningGlow/metadata.desktop
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
/usr/share/wallpapers/FallenLeaf/metadata.desktop
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
/usr/share/wallpapers/FlyingKonqui/metadata.desktop
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
/usr/share/wallpapers/Grey/metadata.desktop
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
/usr/share/wallpapers/Kite/metadata.desktop
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
/usr/share/wallpapers/OneStandsOut/metadata.desktop
/usr/share/wallpapers/PastelHills/contents/images/1024x768.jpg
/usr/share/wallpapers/PastelHills/contents/images/1280x1024.jpg
/usr/share/wallpapers/PastelHills/contents/images/1280x800.jpg
/usr/share/wallpapers/PastelHills/contents/images/1440x900.jpg
/usr/share/wallpapers/PastelHills/contents/images/1600x1200.jpg
/usr/share/wallpapers/PastelHills/contents/images/1638x1024.jpg
/usr/share/wallpapers/PastelHills/contents/images/1680x1050.jpg
/usr/share/wallpapers/PastelHills/contents/images/1920x1080.jpg
/usr/share/wallpapers/PastelHills/contents/images/2560x1440.jpg
/usr/share/wallpapers/PastelHills/contents/images/2560x1600.jpg
/usr/share/wallpapers/PastelHills/contents/images/3200x1800.jpg
/usr/share/wallpapers/PastelHills/contents/images/3200x2000.jpg
/usr/share/wallpapers/PastelHills/contents/screenshot.jpg
/usr/share/wallpapers/PastelHills/metadata.desktop
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
/usr/share/wallpapers/Path/metadata.desktop

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/plasma-workspace-wallpapers/COPYING
/usr/share/package-licenses/plasma-workspace-wallpapers/COPYING.LGPL3
