Summary:	Controls the robotic mechanism in DDS Tape drive autoloaders
Name:		mtx
Version:	1.3.12
Release:	4
Group:		Archiving/Backup
License:	GPLv2
URL:		https://sourceforge.net/projects/mtx
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


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.12-3mdv2011.0
+ Revision: 620415
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.3.12-2mdv2010.0
+ Revision: 430115
- rebuild

* Mon Sep 01 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.12-1mdv2009.0
+ Revision: 278251
- 1.3.12
- install the bash_completion file

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.3.11-2mdv2009.0
+ Revision: 268173
- rebuild early 2009.0 package (before pixel changes)

* Fri May 09 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.11-1mdv2009.0
+ Revision: 204930
- 1.3.11
- drop redundant patches

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 1.2.18-5mdv2008.1
+ Revision: 140966
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Sep 03 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2.18-5mdv2008.0
+ Revision: 78553
- rebuild


* Tue Aug 22 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.18-4mdv2007.0
- sync with fedora (1.2.18-8.2.1)

* Fri Sep 09 2005 Buchan Milne <bgmilne@linux-mandrake.com> 1.2.18-3mdk
- annual rebuild

* Mon May 17 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.2.18-2mdk
- added P0 from fedora (makes it compile...)
- misc spec file fixes

