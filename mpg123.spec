%define	major	0
%define	libname	%mklibname mpg123_ %{major}
%define	devname	%mklibname -d mpg123

Summary:	MPEG audio player
Name:		mpg123
Version:	1.13.5
Release:	1
License:	LGPLv2+
Group:		Sound
URL:		http://www.mpg123.de
Source0:	http://prdownloads.sourceforge.net/mpg123/%{name}-%{version}.tar.bz2
Source1:	mp3license.tar.bz2
BuildRequires:	pkgconfig(alsa)
BuildRequires:	libltdl-devel
BuildRequires:	pkgconfig(jack)
BuildRequires:	nas-devel
BuildRequires:	pkgconfig(portaudio-2.0)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(esound)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(zlib)

%description
Mpg123 is a fast, free and portable MPEG audio player for Unix.
It supports MPEG 1.0/2.0 layers 1, 2 and 3 ("mp3" files).  For
full CD quality playback (44 kHz, 16 bit, stereo) a fast CPU
is required. Mono and/or reduced quality playback (22 kHz or
11 kHz) is possible on slow CPUs (like Intel 486).

For information on the MP3 License, please visit:
http://www.mpeg.org

%package	pulse
Group:		Sound
Summary:	Pulse audio output plugin for mpg123
Requires:	%{name} = %{version}

%description pulse
Mpg123 is a fast, free and portable MPEG audio player for Unix.
It supports MPEG 1.0/2.0 layers 1, 2 and 3 ("mp3" files).  For
full CD quality playback (44 kHz, 16 bit, stereo) a fast CPU
is required. Mono and/or reduced quality playback (22 kHz or
11 kHz) is possible on slow CPUs (like Intel 486).

For information on the MP3 License, please visit:
http://www.mpeg.org

%package	jack
Group:		Sound
Summary:	Jack audio output plugin for mpg123
Requires:	%{name} = %{version}

%description	jack
Mpg123 is a fast, free and portable MPEG audio player for Unix.
It supports MPEG 1.0/2.0 layers 1, 2 and 3 ("mp3" files).  For
full CD quality playback (44 kHz, 16 bit, stereo) a fast CPU
is required. Mono and/or reduced quality playback (22 kHz or
11 kHz) is possible on slow CPUs (like Intel 486).

For information on the MP3 License, please visit:
http://www.mpeg.org


%package	portaudio
Group:		Sound
Summary:	Portaudio output plugin for mpg123
Requires:	%{name} = %{version}

%description	portaudio
Mpg123 is a fast, free and portable MPEG audio player for Unix.
It supports MPEG 1.0/2.0 layers 1, 2 and 3 ("mp3" files).  For
full CD quality playback (44 kHz, 16 bit, stereo) a fast CPU
is required. Mono and/or reduced quality playback (22 kHz or
11 kHz) is possible on slow CPUs (like Intel 486).

For information on the MP3 License, please visit:
http://www.mpeg.org

%package	nas
Group:		Sound
Summary:	NAS audio output plugin for mpg123
Requires:	%{name} = %{version}

%description	nas
Mpg123 is a fast, free and portable MPEG audio player for Unix.
It supports MPEG 1.0/2.0 layers 1, 2 and 3 ("mp3" files).  For
full CD quality playback (44 kHz, 16 bit, stereo) a fast CPU
is required. Mono and/or reduced quality playback (22 kHz or
11 kHz) is possible on slow CPUs (like Intel 486).

For information on the MP3 License, please visit:
http://www.mpeg.org

%package	sdl
Group:		Sound
Summary:	SDL audio output plugin for mpg123
Requires:	%{name} = %{version}

%description	sdl
Mpg123 is a fast, free and portable MPEG audio player for Unix.
It supports MPEG 1.0/2.0 layers 1, 2 and 3 ("mp3" files).  For
full CD quality playback (44 kHz, 16 bit, stereo) a fast CPU
is required. Mono and/or reduced quality playback (22 kHz or
11 kHz) is possible on slow CPUs (like Intel 486).

For information on the MP3 License, please visit:
http://www.mpeg.org

%package	esd
Group:		Sound
Summary:	Esound audio output plugin for mpg123
Requires:	%{name} = %{version}

%description	esd
Mpg123 is a fast, free and portable MPEG audio player for Unix.
It supports MPEG 1.0/2.0 layers 1, 2 and 3 ("mp3" files).  For
full CD quality playback (44 kHz, 16 bit, stereo) a fast CPU
is required. Mono and/or reduced quality playback (22 kHz or
11 kHz) is possible on slow CPUs (like Intel 486).

For information on the MP3 License, please visit:
http://www.mpeg.org

%package	openal
Group:		Sound
Summary:	OpenAL audio output plugin for mpg123
Requires:	%{name} = %{version}

%description	openal
Mpg123 is a fast, free and portable MPEG audio player for Unix.
It supports MPEG 1.0/2.0 layers 1, 2 and 3 ("mp3" files).  For
full CD quality playback (44 kHz, 16 bit, stereo) a fast CPU
is required. Mono and/or reduced quality playback (22 kHz or
11 kHz) is possible on slow CPUs (like Intel 486).

For information on the MP3 License, please visit:
http://www.mpeg.org

%package -n	%{libname}
Group:		System/Libraries
Summary:	MPEG audio decoding library

%description -n	%{libname}
libmpg123 is a fast, free and portable MPEG audio decoding library for Unix.
It supports MPEG 1.0/2.0 layers 1, 2 and 3 ("mp3" files).  For full CD
quality playback (44 kHz, 16 bit, stereo) a fast CPU is required. Mono
and/or reduced quality playback (22 kHz or 11 kHz) is possible on slow
CPUs (like Intel 486).

For information on the MP3 License, please visit:
http://www.mpeg.org

%package -n	%{devname}
Group:		Development/C
Summary:	MPEG audio decoding library - development files
Requires:	%{libname} = %{version}
Provides:	libmpg123-devel = %{version}-%{release}

%description -n %devname
libmpg123 is a fast, free and portable MPEG audio decoding library for Unix.
It supports MPEG 1.0/2.0 layers 1, 2 and 3 ("mp3" files).  For full CD
quality playback (44 kHz, 16 bit, stereo) a fast CPU is required. Mono
and/or reduced quality playback (22 kHz or 11 kHz) is possible on slow
CPUs (like Intel 486).

For information on the MP3 License, please visit:
http://www.mpeg.org

%prep
%setup -q -a 1
rm -f doc/README.WIN32
rm -f configure
libtoolize --force --copy; aclocal; autoheader; automake --add-missing --copy; autoconf

%build
#gw this must be disabled for configure, else it will bail out
%define Werror_cflags %{nil}
%configure2_5x \
    --with-module-suffix=.so \
    --with-default-audio=alsa \
    --enable-ipv6=yes \
    --enable-network=yes

%make CFLAGS="%{optflags} -Wformat -Werror=format-security"

%install
%makeinstall_std

%files 
%doc doc/* NEWS README AUTHORS ChangeLog
%doc mp3license
%defattr (-,root,root)
%{_bindir}/*
%{_mandir}/man1/*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/output_alsa*
%{_libdir}/%{name}/output_dummy*
%{_libdir}/%{name}/output_oss*

%files pulse
%{_libdir}/%{name}/output_pulse*

%files jack
%{_libdir}/%{name}/output_jack*

%files nas
%{_libdir}/%{name}/output_nas*

%files portaudio
%{_libdir}/%{name}/output_portaudio*

%files sdl
%{_libdir}/%{name}/output_sdl*

%files esd
%{_libdir}/%{name}/output_esd*

%files openal
%{_libdir}/%{name}/output_openal*

%files -n %{libname}
%{_libdir}/libmpg123.so.%{major}*

%files -n %{devname}
%{_libdir}/libmpg123.so
%{_libdir}/libmpg123.la
%{_includedir}/mpg123.h
%{_libdir}/pkgconfig/libmpg123.pc
