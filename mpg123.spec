%define major 0
%define libname %mklibname mpg123_ %major
%define develname %mklibname -d mpg123

Summary:	MPEG audio player
Name:		mpg123
Version:	1.5.1
Release:	%mkrel 1
License:	LGPLv2+
Group:		Sound
URL:		http://www.mpg123.de
Source0:	http://prdownloads.sourceforge.net/mpg123/mpg123-%version.tar.gz
Source1:	mp3license.tar.bz2
BuildRequires:	libalsa-devel
BuildRequires:	libarts-devel kdelibs-common
BuildRequires:	libltdl-devel
BuildRequires:	libjack-devel
BuildRequires:	libnas-devel
BuildRequires:	libportaudio-devel
BuildRequires:	libpulseaudio-devel
BuildRequires:	libSDL-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Mpg123 is a fast, free and portable MPEG audio player for Unix.
It supports MPEG 1.0/2.0 layers 1, 2 and 3 ("mp3" files).  For
full CD quality playback (44 kHz, 16 bit, stereo) a fast CPU
is required. Mono and/or reduced quality playback (22 kHz or
11 kHz) is possible on slow CPUs (like Intel 486).

For information on the MP3 License, please visit:
http://www.mpeg.org

%package pulse
Group: Sound
Summary: Pulse audio output plugin for mpg123
Requires: %name = %version

%description pulse
Mpg123 is a fast, free and portable MPEG audio player for Unix.
It supports MPEG 1.0/2.0 layers 1, 2 and 3 ("mp3" files).  For
full CD quality playback (44 kHz, 16 bit, stereo) a fast CPU
is required. Mono and/or reduced quality playback (22 kHz or
11 kHz) is possible on slow CPUs (like Intel 486).

For information on the MP3 License, please visit:
http://www.mpeg.org

%package jack
Group: Sound
Summary: Jack audio output plugin for mpg123
Requires: %name = %version

%description jack
Mpg123 is a fast, free and portable MPEG audio player for Unix.
It supports MPEG 1.0/2.0 layers 1, 2 and 3 ("mp3" files).  For
full CD quality playback (44 kHz, 16 bit, stereo) a fast CPU
is required. Mono and/or reduced quality playback (22 kHz or
11 kHz) is possible on slow CPUs (like Intel 486).

For information on the MP3 License, please visit:
http://www.mpeg.org

%package arts
Group: Sound
Summary: Arts audio output plugin for mpg123
Requires: %name = %version

%description arts
Mpg123 is a fast, free and portable MPEG audio player for Unix.
It supports MPEG 1.0/2.0 layers 1, 2 and 3 ("mp3" files).  For
full CD quality playback (44 kHz, 16 bit, stereo) a fast CPU
is required. Mono and/or reduced quality playback (22 kHz or
11 kHz) is possible on slow CPUs (like Intel 486).

For information on the MP3 License, please visit:
http://www.mpeg.org


%package portaudio
Group: Sound
Summary: Portaudio output plugin for mpg123
Requires: %name = %version

%description portaudio
Mpg123 is a fast, free and portable MPEG audio player for Unix.
It supports MPEG 1.0/2.0 layers 1, 2 and 3 ("mp3" files).  For
full CD quality playback (44 kHz, 16 bit, stereo) a fast CPU
is required. Mono and/or reduced quality playback (22 kHz or
11 kHz) is possible on slow CPUs (like Intel 486).

For information on the MP3 License, please visit:
http://www.mpeg.org

%package nas
Group: Sound
Summary: NAS audio output plugin for mpg123
Requires: %name = %version

%description nas
Mpg123 is a fast, free and portable MPEG audio player for Unix.
It supports MPEG 1.0/2.0 layers 1, 2 and 3 ("mp3" files).  For
full CD quality playback (44 kHz, 16 bit, stereo) a fast CPU
is required. Mono and/or reduced quality playback (22 kHz or
11 kHz) is possible on slow CPUs (like Intel 486).

For information on the MP3 License, please visit:
http://www.mpeg.org

%package sdl
Group: Sound
Summary: SDL audio output plugin for mpg123
Requires: %name = %version

%description sdl
Mpg123 is a fast, free and portable MPEG audio player for Unix.
It supports MPEG 1.0/2.0 layers 1, 2 and 3 ("mp3" files).  For
full CD quality playback (44 kHz, 16 bit, stereo) a fast CPU
is required. Mono and/or reduced quality playback (22 kHz or
11 kHz) is possible on slow CPUs (like Intel 486).

For information on the MP3 License, please visit:
http://www.mpeg.org

%package esd
Group: Sound
Summary:Esound audio output plugin for mpg123
Requires: %name = %version

%description esd
Mpg123 is a fast, free and portable MPEG audio player for Unix.
It supports MPEG 1.0/2.0 layers 1, 2 and 3 ("mp3" files).  For
full CD quality playback (44 kHz, 16 bit, stereo) a fast CPU
is required. Mono and/or reduced quality playback (22 kHz or
11 kHz) is possible on slow CPUs (like Intel 486).

For information on the MP3 License, please visit:
http://www.mpeg.org

%package -n %libname
Group:System/Libraries
Summary: MPEG audio decoding library

%description -n %libname
libmpg123 is a fast, free and portable MPEG audio decoding library for Unix.
It supports MPEG 1.0/2.0 layers 1, 2 and 3 ("mp3" files).  For full CD
quality playback (44 kHz, 16 bit, stereo) a fast CPU is required. Mono
and/or reduced quality playback (22 kHz or 11 kHz) is possible on slow
CPUs (like Intel 486).

For information on the MP3 License, please visit:
http://www.mpeg.org

%package -n %develname
Group: Development/C
Summary: MPEG audio decoding library - development files
Requires: %libname = %version
Provides: libmpg123-devel = %version-%release

%description -n %develname
libmpg123 is a fast, free and portable MPEG audio decoding library for Unix.
It supports MPEG 1.0/2.0 layers 1, 2 and 3 ("mp3" files).  For full CD
quality playback (44 kHz, 16 bit, stereo) a fast CPU is required. Mono
and/or reduced quality playback (22 kHz or 11 kHz) is possible on slow
CPUs (like Intel 486).

For information on the MP3 License, please visit:
http://www.mpeg.org

%prep

%setup -q -n %name-%version -a 1
rm -f doc//README.WIN32

%build
export PATH="$PATH:/opt/kde3/bin"

%configure2_5x \
    --with-default-audio=alsa \
    --enable-ipv6=yes \
    --enable-network=yes

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -r %{buildroot}

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files 
%defattr(-,root,root)
%doc doc/* NEWS README AUTHORS ChangeLog
%doc mp3license
%defattr (-,root,root)
%{_bindir}/*
%{_mandir}/man1/*
%dir %_libdir/%name
%_libdir/%name/output_alsa*
%_libdir/%name/output_dummy*
%_libdir/%name/output_oss*


%files pulse
%defattr(-,root,root)
%_libdir/%name/output_pulse*

%files jack
%defattr(-,root,root)
%_libdir/%name/output_jack*

%files arts
%defattr(-,root,root)
%_libdir/%name/output_arts*

%files nas
%defattr(-,root,root)
%_libdir/%name/output_nas*

%files portaudio
%defattr(-,root,root)
%_libdir/%name/output_portaudio*

%files sdl
%defattr(-,root,root)
%_libdir/%name/output_sdl*

%files esd
%defattr(-,root,root)
%_libdir/%name/output_esd*

%files -n %libname
%defattr(-,root,root)
%_libdir/libmpg123.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%_libdir/libmpg123.so
%_libdir/libmpg123.la
%_includedir/mpg123.h
%_libdir/pkgconfig/libmpg123.pc
