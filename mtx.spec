Summary:	Controls the robotic mechanism in DDS Tape drive autoloaders
Name:		mtx
Version:	1.3.12
Release:	%mkrel 3
Group:		Archiving/Backup
License:	GPLv2
URL:		http://sourceforge.net/projects/mtx
Source0:	ftp://ftp.opensource-sw.net/pub/mtx/development/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description 
The MTX program controls the robotic mechanism in autoloaders and tape
libraries such as the HP SureStore DAT 40x6, Exabyte EZ-17, and
Exabyte 220. This program is also reported to work with a variety of
other tape libraries and autochangers from ADIC, Tandberg/Overland,
Breece Hill, HP, and Seagate.

If you have a backup tape device capable of handling more than one
tape at a time, you should install MTX.

%prep

%setup -q -n %{name}-%{version}

%build

%configure2_5x \
    --sbindir=/sbin

%make

%install
rm -rf %{buildroot}

%makeinstall sbindir=%{buildroot}/sbin

install -d %{buildroot}%{_sysconfdir}/bash_completion.d
install -m0644 debian/bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/%{name}

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc CHANGES COMPATABILITY contrib FAQ LICENSE LICENSE.html
%doc mtx.doc mtxl.README.html README TODO
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}
/sbin/*
%{_mandir}/man1/*
