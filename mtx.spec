Summary:	Controls the robotic mechanism in DDS Tape drive autoloaders
Name:		mtx
Version:	1.2.18
Release:	%mkrel 4
Group:		Archiving/Backup
License:	GPL
URL:		http://sourceforge.net/projects/mtx
Source0:	ftp://ftp.badtux.net/pub/storage/mtx/%{name}-%{version}rel.tar.bz2
Patch0:		mtx-1.2.18-portable.patch
Patch1:		mtx-1.2.18rel-dce.patch
Patch2:		mtx-1.2.18rel-gcc4.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description 
The MTX program controls the robotic mechanism in autoloaders and tape
libraries such as the HP SureStore DAT 40x6, Exabyte EZ-17, and
Exabyte 220. This program is also reported to work with a variety of
other tape libraries and autochangers from ADIC, Tandberg/Overland,
Breece Hill, HP, and Seagate.

If you have a backup tape device capable of handling more than one
tape at a time, you should install MTX.

%prep

%setup -q -n %{name}-%{version}rel
%patch0 -p1 -b .portable
%patch1 -p1 -b .dce
%patch2 -p1 -b .gcc4

%build

%configure2_5x

%make

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

install -d %{buildroot}/sbin
install -d %{buildroot}%{_mandir}/man1

install mtx %{buildroot}/sbin/mtx
install tapeinfo %{buildroot}/sbin/tapeinfo
install mtx.1 %{buildroot}%{_mandir}/man1/mtx.1
install tapeinfo.1 %{buildroot}%{_mandir}/man1/tapeinfo.1

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc CHANGES COMPATABILITY contrib FAQ LICENSE LICENSE.html
%doc mtx.doc mtxl.README.html README TODO
%{_mandir}/man1/*
/sbin/*

