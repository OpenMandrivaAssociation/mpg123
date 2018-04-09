%define	major	0
%define	libname	%mklibname mpg123_ %{major}
%define	libout	%mklibname out123_ %{major}
%define	devname	%mklibname -d mpg123
%define	devout	%mklibname -d out123

Summary:	MPEG audio player
Name:		mpg123
Version:	1.25.10
Release:	1
License:	LGPLv2+
Group:		Sound
Url:		http://www.mpg123.de
Source0:	http://www.mpg123.de/download/mpg123-%{version}.tar.bz2
Source1:	mp3license.tar.bz2
BuildRequires:	libtool-devel
BuildRequires:	nas-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(portaudio-2.0)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(zlib)

%track
prog %{name} = {
	url = http://sourceforge.net/projects/mpg123/files/
	version = %{version}
	regex = %{name}-(__VER__)\.tar\.bz2
}

%description
Mpg123 is a fast, free and portable MPEG audio player for Unix.
It supports MPEG 1.0/2.0 layers 1, 2 and 3 ("mp3" files).  For
full CD quality playback (44 kHz, 16 bit, stereo) a fast CPU
is required. Mono and/or reduced quality playback (22 kHz or
11 kHz) is possible on slow CPUs (like Intel 486).

For information on the MP3 License, please visit:
http://www.mpeg.org

%package	pulse
Summary:	Pulse audio output plugin for mpg123
Group:		Sound
Requires:	%{name} = %{version}-%{release}

%description pulse
This package contains the pulseaudio plugin for %{name}.

%package	jack
Summary:	Jack audio output plugin for mpg123
Group:		Sound
Requires:	%{name} = %{version}-%{release}

%description	jack
This package contains the jack plugin for %{name}.

%package	portaudio
Summary:	Portaudio output plugin for mpg123
Group:		Sound
Requires:	%{name} = %{version}-%{release}

%description	portaudio
This package contains the portaudio plugin for %{name}.

%package	nas
Summary:	NAS audio output plugin for mpg123
Group:		Sound
Requires:	%{name} = %{version}-%{release}

%description	nas
This package contains the nas plugin for %{name}.

%package	sdl
Summary:	SDL audio output plugin for mpg123
Group:		Sound
Requires:	%{name} = %{version}-%{release}

%description	sdl
This package contains the sdl plugin for %{name}.

%package	openal
Summary:	OpenAL audio output plugin for mpg123
Group:		Sound
Requires:	%{name} = %{version}-%{release}

%description	openal
This package contains the openal plugin for %{name}.

%package -n	%{libname}
Summary:	MPEG audio decoding library
Group:		System/Libraries

%description -n	%{libname}
This package contains the share library for %{name}.

%package -n	%{libout}
Summary:	MPEG audio decoding library
Group:		System/Libraries

%description -n	%{libout}
This package contains the share library for %{name}.

%package -n	%{devout}
Summary:	MPEG audio decoding library - development files
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libout} = %{version}-%{release}
Requires:	%{devname} = %{version}-%{release}
Provides:	%{name}-out-devel = %{version}-%{release}

%description -n %{devout}
This package includes the development files for %{name}.

%package -n	%{devname}
Summary:	MPEG audio decoding library - development files
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package includes the development files for %{name}.

%prep
%setup -q -a 1
%apply_patches
rm -f doc/README.WIN32
rm -f configure
libtoolize --force --copy; aclocal; autoheader; automake --add-missing --copy; autoconf

%build
#gw this must be disabled for configure, else it will bail out
%define Werror_cflags %{nil}
%configure \
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

%files openal
%{_libdir}/%{name}/output_openal*

%files -n %{libname}
%{_libdir}/libmpg123.so.%{major}*

%files -n %{libout}
%{_libdir}/libout123.so.%{major}*

%files -n %{devout}
%{_libdir}/pkgconfig/libout123.pc
%{_includedir}/out123.h
%{_libdir}/libout123.so

%files -n %{devname}
%{_libdir}/libmpg123.so
%{_includedir}/mpg123.h
%{_includedir}/fmt123.h
%{_libdir}/pkgconfig/libmpg123.pc
