Summary:	MPEG audio player
Name:		mpg123
Version:	0.66
Release: 	%mkrel 1
Group:		Sound
BuildRequires:	libalsa-devel
Url:		http://www.mpg123.de/

Source0:	http://prdownloads.sourceforge.net/mpg123/mpg123-%version.tar.bz2
Source1:	mp3license.tar.bz2

License:	LGPL
Buildroot:	%_tmppath/%name-%version-root

%description
Mpg123 is a fast, free and portable MPEG audio player for Unix.
It supports MPEG 1.0/2.0 layers 1, 2 and 3 ("mp3" files).  For
full CD quality playback (44 kHz, 16 bit, stereo) a fast CPU
is required. Mono and/or reduced quality playback (22 kHz or
11 kHz) is possible on slow CPUs (like Intel 486).

For information on the MP3 License, please visit:
http://www.mpeg.org/

%prep

%setup -q -a 1
rm -f doc//README.WIN32

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT/ 
%makeinstall_std

%clean
rm -r $RPM_BUILD_ROOT

%files 
%defattr(0644,root,root,755)
%doc doc/* NEWS README AUTHORS ChangeLog
%doc mp3license
%defattr (-,root,root)
%{_bindir}/*
%{_mandir}/man1/*


