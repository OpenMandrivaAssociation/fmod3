%define		oname fmod
%define		major 3
%define		libname %mklibname %{oname} %{major}
%define		develname %mklibname %{oname} -d
%define		oversion 375

Summary:	Fast, powerful, easy to use sound system
Name:		fmod3
Version:	3.75
Release:	2
License:	FMOD Licence (free for non-commercial use)
Group:		System/Libraries
URL:		http://www.fmod.org/
Source:		http://www.fmod.org/files/fmodapi%{oversion}linux.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
ExclusiveArch:	%{ix86}

%description
FMOD is a fast, powerful, and easy to use sound system. It runs on
Windows, Linux, Windows CE, and now also on Macintosh, GameCube, PS2,
and XBox. FMOD supports 3D sound, midi, mods, mp3, ogg vorbis, wma, aiff,
recording, obstruction/occlusion, cd playback (analog or digital), cd ripping,
mmx, internet streaming, dsp effects, spectrum analysis, user created samples
and streams, synchronization support, ASIO, EAX 2&3, C/C++/VB/Delphi and more.

%package -n %{libname}
Summary:	Fast, powerful, easy to use sound system
Group:		System/Libraries

%description -n %{libname}
FMOD is a fast, powerful, and easy to use sound system. It runs on
Windows, Linux, Windows CE, and now also on Macintosh, GameCube, PS2,
and XBox. FMOD supports 3D sound, midi, mods, mp3, ogg vorbis, wma, aiff,
recording, obstruction/occlusion, cd playback (analog or digital), cd ripping,
mmx, internet streaming, dsp effects, spectrum analysis, user created samples
and streams, synchronization support, ASIO, EAX 2&3, C/C++/VB/Delphi and more.

%package -n %{develname}
Summary:	Header files and documentation for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains the header files and development documentation
for %{name}. If you like to develop programs using %{name}, you will
need to install %{name}-devel.

%prep
%setup -qn fmodapi%{oversion}linux

%install
%__rm -rf %{buildroot}
%__install -Dp -m0755 api/libfmod-%{version}.so %{buildroot}%{_libdir}/libfmod-%{version}.so.%{major}
%__ln_s %{_libdir}/libfmod-%{version}.so.%{major} %{buildroot}%{_libdir}/libfmod.so

%__install -d %{buildroot}%{_includedir}/fmod3/
%__cp api/inc/*.h %{buildroot}%{_includedir}/fmod3/

%clean
%__rm -rf %{buildroot}

%files -n %{libname}
%defattr(-, root, root, 0755)
%doc README.TXT
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(644, root, root, 0755)
%doc documentation/* media/ samples/
%{_includedir}/fmod3/
%{_libdir}/*.so

