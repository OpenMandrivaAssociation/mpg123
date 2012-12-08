%define	major	0
%define	libname	%mklibname mpg123_ %{major}
%define	devname	%mklibname -d mpg123

Summary:	MPEG audio player
Name:		mpg123
Version:	1.14.4
Release:	1
License:	LGPLv2+
Group:		Sound
URL:		http://www.mpg123.de
Source0:	http://prdownloads.sourceforge.net/mpg123/%{name}-%{version}.tar.bz2
Source1:	mp3license.tar.bz2
BuildRequires:	pkgconfig(alsa)
BuildRequires:	libtool-devel
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
%{_includedir}/mpg123.h
%{_libdir}/pkgconfig/libmpg123.pc


%changelog
* Sun Jul 01 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.14.3-1
+ Revision: 807720
- version update 1.14.3

* Sat May 12 2012 Götz Waschk <waschk@mandriva.org> 1.14.2-1
+ Revision: 798503
- update to new version 1.14.2

* Tue May 08 2012 Götz Waschk <waschk@mandriva.org> 1.14.1-1
+ Revision: 797375
- update to new version 1.14.1

* Wed May 02 2012 Götz Waschk <waschk@mandriva.org> 1.14.0-1
+ Revision: 794982
- update to new version 1.14.0

* Thu Apr 12 2012 Götz Waschk <waschk@mandriva.org> 1.13.8-1
+ Revision: 790443
- update to new version 1.13.8

* Mon Mar 26 2012 Götz Waschk <waschk@mandriva.org> 1.13.7-1
+ Revision: 786864
- new version

* Mon Mar 12 2012 Götz Waschk <waschk@mandriva.org> 1.13.6-1
+ Revision: 784319
- update build deps
- new version

* Fri Mar 09 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.13.5-1
+ Revision: 783645
- drop libtool file
- do autoconf etc. in %%prep
- cleanups
- use pkgconfig() dependencies

  + Götz Waschk <waschk@mandriva.org>
    - update to new version 1.13.5

* Wed Dec 07 2011 Funda Wang <fwang@mandriva.org> 1.13.4-2
+ Revision: 738469
- use so to detect plugin

* Thu Sep 08 2011 Götz Waschk <waschk@mandriva.org> 1.13.4-1
+ Revision: 698926
- update to new version 1.13.4

* Fri Apr 22 2011 Götz Waschk <waschk@mandriva.org> 1.13.3-1
+ Revision: 656670
- update to new version 1.13.3

* Sun Feb 20 2011 Götz Waschk <waschk@mandriva.org> 1.13.2-1
+ Revision: 639017
- update to new version 1.13.2

* Thu Jan 06 2011 Götz Waschk <waschk@mandriva.org> 1.13.1-1mdv2011.0
+ Revision: 629053
- update to new version 1.13.1

* Tue Dec 14 2010 Götz Waschk <waschk@mandriva.org> 1.13.0-1mdv2011.0
+ Revision: 621691
- update to new version 1.13.0

* Thu Oct 07 2010 Götz Waschk <waschk@mandriva.org> 1.12.5-1mdv2011.0
+ Revision: 584012
- update to new version 1.12.5

* Sat Sep 18 2010 Götz Waschk <waschk@mandriva.org> 1.12.4-1mdv2011.0
+ Revision: 579619
- update to new version 1.12.4

* Sun Jul 11 2010 Götz Waschk <waschk@mandriva.org> 1.12.3-1mdv2011.0
+ Revision: 551162
- update to new version 1.12.3

* Sat Jul 10 2010 Götz Waschk <waschk@mandriva.org> 1.12.2-1mdv2011.0
+ Revision: 550273
- new version

* Wed Apr 14 2010 Götz Waschk <waschk@mandriva.org> 1.12.1-1mdv2010.1
+ Revision: 534704
- new version

* Wed Mar 31 2010 Götz Waschk <waschk@mandriva.org> 1.12.0-1mdv2010.1
+ Revision: 530454
- update to new version 1.12.0

* Sun Mar 21 2010 Götz Waschk <waschk@mandriva.org> 1.11.0-1mdv2010.1
+ Revision: 526133
- update to new version 1.11.0

* Sat Feb 27 2010 Götz Waschk <waschk@mandriva.org> 1.10.1-1mdv2010.1
+ Revision: 512490
- new version

* Sun Dec 06 2009 Funda Wang <fwang@mandriva.org> 1.10.0-1mdv2010.1
+ Revision: 474122
- new version 1.10.0

* Sat Nov 21 2009 Funda Wang <fwang@mandriva.org> 1.9.2-1mdv2010.1
+ Revision: 468071
- New version 1.9.2

* Fri Nov 06 2009 Götz Waschk <waschk@mandriva.org> 1.9.1-1mdv2010.1
+ Revision: 460841
- update to new version 1.9.1

* Fri Aug 14 2009 Götz Waschk <waschk@mandriva.org> 1.9.0-1mdv2010.0
+ Revision: 416308
- new version
- add openal plugin

* Mon Jun 15 2009 Funda Wang <fwang@mandriva.org> 1.8.1-1mdv2010.0
+ Revision: 385956
- New version 1.8.1

* Thu Jun 11 2009 Götz Waschk <waschk@mandriva.org> 1.8.0-1mdv2010.0
+ Revision: 385061
- new version
- drop patch

* Mon Jun 08 2009 Götz Waschk <waschk@mandriva.org> 1.7.3-1mdv2010.0
+ Revision: 383898
- update to new version 1.7.3

* Fri Apr 17 2009 Oden Eriksson <oeriksson@mandriva.com> 1.7.2-1mdv2009.1
+ Revision: 367902
- fix deps (zlib-devel)
- 1.7.2
- fix autopoo

* Mon Feb 09 2009 Helio Chissini de Castro <helio@mandriva.com> 1.6.4-3mdv2009.1
+ Revision: 338926
- No arts anymore...

* Wed Jan 28 2009 Götz Waschk <waschk@mandriva.org> 1.6.4-2mdv2009.1
+ Revision: 334734
- rebuild for new libltdl

* Sun Jan 11 2009 Funda Wang <fwang@mandriva.org> 1.6.4-1mdv2009.1
+ Revision: 328266
- 1.6.4

* Sun Dec 21 2008 Götz Waschk <waschk@mandriva.org> 1.6.3-1mdv2009.1
+ Revision: 317118
- new version
- fix build

* Thu Nov 13 2008 Götz Waschk <waschk@mandriva.org> 1.6.2-1mdv2009.1
+ Revision: 302637
- update to new version 1.6.2

* Mon Nov 10 2008 Götz Waschk <waschk@mandriva.org> 1.6.1-1mdv2009.1
+ Revision: 301677
- update to new version 1.6.1

* Wed Nov 05 2008 Götz Waschk <waschk@mandriva.org> 1.6.0-1mdv2009.1
+ Revision: 300003
- update to new version 1.6.0

* Fri Aug 29 2008 Oden Eriksson <oeriksson@mandriva.com> 1.5.1-1mdv2009.0
+ Revision: 277348
- 1.5.1

* Sun Aug 03 2008 Oden Eriksson <oeriksson@mandriva.com> 1.5.0-1mdv2009.0
+ Revision: 262019
- 1.5.0

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri May 23 2008 Götz Waschk <waschk@mandriva.org> 1.4.3-2mdv2009.0
+ Revision: 210361
- disable no undefined workaround

* Fri May 23 2008 Götz Waschk <waschk@mandriva.org> 1.4.3-1mdv2009.0
+ Revision: 210270
- fix buildrequires for stupid KDE
- new version
- disable no undefined option to make it build

* Mon Apr 21 2008 Götz Waschk <waschk@mandriva.org> 1.4.2-1mdv2009.0
+ Revision: 196116
- new version

* Tue Apr 08 2008 Götz Waschk <waschk@mandriva.org> 1.4.1-1mdv2009.0
+ Revision: 192392
- new version

* Thu Mar 06 2008 Götz Waschk <waschk@mandriva.org> 1.3.0-2mdv2008.1
+ Revision: 180900
- use alsa by default
- split pulseaudio plugin

* Mon Mar 03 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-1mdv2008.1
+ Revision: 177857
- 1.3.0 (Major bugfixes)

* Wed Feb 20 2008 Götz Waschk <waschk@mandriva.org> 1.2.1-1mdv2008.1
+ Revision: 173165
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Fri Feb 01 2008 Funda Wang <fwang@mandriva.org> 1.2.0-1mdv2008.1
+ Revision: 161062
- New version 1.2.0

* Tue Jan 15 2008 Götz Waschk <waschk@mandriva.org> 1.1.0-1mdv2008.1
+ Revision: 152836
- new version
- add arts plugin

* Sat Dec 29 2007 Funda Wang <fwang@mandriva.org> 1.0.1-1mdv2008.1
+ Revision: 139179
- New version 1.0.1

* Thu Dec 27 2007 Götz Waschk <waschk@mandriva.org> 1.0.0-1mdv2008.1
+ Revision: 138436
- add esd plugin
- new version
- drop patch

* Thu Dec 20 2007 Götz Waschk <waschk@mandriva.org> 1.0-0.rc3.2mdv2008.1
+ Revision: 136006
- fix pulse plugin

* Tue Dec 18 2007 Götz Waschk <waschk@mandriva.org> 1.0-0.rc3.1mdv2008.1
+ Revision: 132240
- add additional audio output plugins
- make pulseaudio the default output plugin
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Dec 10 2007 Götz Waschk <waschk@mandriva.org> 1.0-0.rc2.1mdv2008.1
+ Revision: 116874
- new version

* Wed Dec 05 2007 Götz Waschk <waschk@mandriva.org> 1.0-0.rc1.1mdv2008.1
+ Revision: 115656
- fix buildrequires
- new version
- add library package

* Sat Nov 17 2007 Funda Wang <fwang@mandriva.org> 0.68-2mdv2008.1
+ Revision: 109207
- rebuild for new lzma

* Sun Nov 04 2007 Götz Waschk <waschk@mandriva.org> 0.68-1mdv2008.1
+ Revision: 105947
- new version

* Fri Oct 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.67-1mdv2008.1
+ Revision: 100093
- new version
- spec file clean

* Mon Jun 04 2007 Götz Waschk <waschk@mandriva.org> 0.66-2mdv2008.0
+ Revision: 35061
- new version

