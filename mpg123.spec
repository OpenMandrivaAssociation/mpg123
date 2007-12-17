%define prerel rc2
%define major 0
%define libname %mklibname mpg123_ %major
%define develname %mklibname -d mpg123
Summary:	MPEG audio player
Name:		mpg123
Version:	1.0
Release:	%mkrel 0.%prerel.1
License:	LGPLv2+
Group:		Sound
Url:		http://www.mpg123.de
Source0:	http://prdownloads.sourceforge.net/mpg123/mpg123-%version%prerel.tar.bz2
Source1:	mp3license.tar.bz2
BuildRequires:	libalsa-devel
BuildRequires:	libltdl-devel

%description
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

%setup -q -n %name-%version%prerel -a 1
rm -f doc//README.WIN32

%build
%configure2_5x \
	--with-audio=alsa

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -r %{buildroot}

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files 
%defattr(-,root,root)
%doc doc/* NEWS README AUTHORS ChangeLog
%doc mp3license
%defattr (-,root,root)
%{_bindir}/*
%{_mandir}/man1/*
%_libdir/%name

%files -n %libname
%defattr(-,root,root)
%_libdir/libmpg123.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%_libdir/libmpg123.so
%_libdir/libmpg123.la
%_includedir/mpg123.h
%_libdir/pkgconfig/libmpg123.pc
