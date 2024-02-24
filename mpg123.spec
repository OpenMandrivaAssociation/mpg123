# mpg123 is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%endif

%define	major	0
%define	libname	%mklibname mpg123_ %{major}
%define	libout	%mklibname out123_ %{major}
%define	libsyn	%mklibname syn123_ %{major}
%define	devname	%mklibname -d mpg123
%define	devout	%mklibname -d out123
%define	devsyn	%mklibname -d syn123
%define	lib32name	%mklib32name mpg123_ %{major}
%define	lib32out	%mklib32name out123_ %{major}
%define	lib32syn	%mklib32name syn123_ %{major}
%define	dev32name	%mklib32name -d mpg123
%define	dev32out	%mklib32name -d out123
%define	dev32syn	%mklib32name -d syn123

Summary:	MPEG audio player
Name:		mpg123
Version:	1.32.5
Release:	1
License:	LGPLv2+
Group:		Sound
Url:		http://www.mpg123.de
Source0:	http://www.mpg123.de/download/mpg123-%{version}.tar.bz2
BuildRequires:	libtool-devel
BuildRequires:	nas-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(portaudio-2.0)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(sndio)
BuildRequires:	pkgconfig(zlib)
%if %{with compat32}
BuildRequires:	libc6
BuildRequires:	devel(libasound)
BuildRequires:	devel(libjack)
BuildRequires:	devel(libpulse)
BuildRequires:	devel(libopenal)
BuildRequires:	devel(libz)
%endif

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

%package	sndio
Summary:	SNDIO audio output plugin for mpg123
Group:		Sound
Requires:	%{name} = %{version}-%{release}

%description	sndio
This package contains the SNDIO plugin for %{name}.

%package	openal
Summary:	OpenAL audio output plugin for mpg123
Group:		Sound
Requires:	%{name} = %{version}-%{release}

%description	openal
This package contains the openal plugin for %{name}.

%package -n	%{libname}
Summary:	MPEG audio decoding library
Requires:	%{libout} = %{version}-%{release}
Requires:	%{libsyn} = %{version}-%{release}
Group:		System/Libraries

%description -n	%{libname}
This package contains the share library for %{name}.

%package -n	%{libout}
summary:	mpeg audio decoding library
group:		system/libraries

%description -n	%{libout}
this package contains the share library for %{name}.

%package -n	%{devout}
Summary:	MPEG audio decoding library - development files
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libout} = %{version}-%{release}
Requires:	%{devname} = %{version}-%{release}
Provides:	%{name}-out-devel = %{version}-%{release}

%description -n %{devout}
This package includes the development files for %{name}.

%package -n	%{libsyn}
Summary:	MPEG audio decoding library
Group:		System/Libraries

%description -n	%{libsyn}
This package contains the share library for %{name}.

%package -n %{devsyn}
Summary:	MPEG audio decoding library - development files
Group:		Development/C
Requires:	%{libsyn} = %{version}-%{release}

%description -n %{devsyn}
MPEG audio decoding library - development files

%package -n	%{devname}
Summary:	MPEG audio decoding library - development files
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package includes the development files for %{name}.

%if %{with compat32}
%package -n	%{lib32name}
Summary:	MPEG audio decoding library (32-bit)
Group:		System/Libraries

%description -n	%{lib32name}
This package contains the share library for %{name}.

%package -n	%{lib32out}
Summary:	MPEG audio decoding library (32-bit)
Group:		System/Libraries

%description -n	%{lib32out}
This package contains the share library for %{name}.

%package -n	%{dev32out}
Summary:	MPEG audio decoding library - development files (32-bit)
Group:		Development/C
Requires:	%{devout} = %{version}-%{release}
Requires:	%{lib32name} = %{version}-%{release}
Requires:	%{lib32out} = %{version}-%{release}
Requires:	%{dev32name} = %{version}-%{release}
Provides:	%{name}-out-devel = %{version}-%{release}

%description -n %{dev32out}
This package includes the development files for %{name}.

%package -n	%{dev32name}
Summary:	MPEG audio decoding library - development files (32-bit)
Group:		Development/C
Requires:	%{devname} = %{version}-%{release}
Requires:	%{lib32name} = %{version}-%{release}

%description -n %{dev32name}
This package includes the development files for %{name}.

%package -n	%{lib32syn}
Summary:	MPEG audio decoding library (32-bit)
Group:		System/Libraries

%description -n	%{lib32syn}
This package contains the share library for %{name}.

%package -n %{dev32syn}
Summary:	MPEG audio decoding library - development files
Group:		Development/C
Requires:	%{devsyn} = %{version}-%{release}
Requires:	%{lib32syn} = %{version}-%{release}

%description -n %{dev32syn}
MPEG audio decoding library - development files
%endif

%prep
%autosetup -p1
rm -f doc/README.WIN32
rm -f configure
libtoolize --force --copy; aclocal; autoheader; automake --add-missing --copy; autoconf
#define Werror_cflags %{nil}

export CONFIGURE_TOP="$(pwd)"

%if %{with compat32}
mkdir build32
cd build32
%configure32 \
	--with-cpu=x86 \
	--with-module-suffix=.so \
	--with-default-audio=alsa \
	--enable-ipv6=yes \
	--enable-network=yes
cd ..
%endif

mkdir buildnative
cd buildnative
%configure \
	--with-module-suffix=.so \
	--with-default-audio=alsa \
	--enable-ipv6=yes \
	--enable-network=yes

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C buildnative CFLAGS="%{optflags} -Wformat -Werror=format-security"

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C buildnative

%files
%doc doc/* NEWS README AUTHORS ChangeLog
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

%files sndio
%{_libdir}/%{name}/output_sndio*

%files openal
%{_libdir}/%{name}/output_openal*

%files -n %{libname}
%{_libdir}/libmpg123.so.%{major}*

%files -n %{libout}
%{_libdir}/libout123.so.%{major}*

%files -n %{libsyn}
%{_libdir}/libsyn123.so.%{major}*

%files -n %{devout}
%{_libdir}/pkgconfig/libout123.pc
%{_includedir}/out123.h
%{_libdir}/libout123.so

%files -n %{devsyn}
%{_libdir}/pkgconfig/libsyn123.pc
%{_libdir}/libsyn123.so
%{_includedir}/syn123.h

%files -n %{devname}
%{_libdir}/libmpg123.so
%{_includedir}/mpg123.h
%{_includedir}/fmt123.h
%{_libdir}/pkgconfig/libmpg123.pc

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libmpg123.so.%{major}*
%dir %{_prefix}/lib/mpg123
# FIXME does it make sense to split the various outputs
# into different subpackages?
%{_prefix}/lib/mpg123/output_*.so

%files -n %{lib32out}
%{_prefix}/lib/libout123.so.%{major}*

%files -n %{lib32syn}
%{_prefix}/lib/libsyn123.so.%{major}*

%files -n %{dev32out}
%{_prefix}/lib/pkgconfig/libout123.pc
%{_prefix}/lib/libout123.so

%files -n %{dev32name}
%{_prefix}/lib/libmpg123.so
%{_prefix}/lib/pkgconfig/libmpg123.pc

%files -n %{dev32syn}
%{_prefix}/lib/pkgconfig/libsyn123.pc
%{_prefix}/lib/libsyn123.so
%endif
