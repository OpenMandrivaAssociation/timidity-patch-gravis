%define name	timidity-patch-gravis
%define version	1.0
%define release 39

%define patch_pkg_version 2

Summary:	Instruments for the timidity midi->wave converter/player
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Public Domain
URL:		http://www.timidity.jp/
# Patches at http://www.cs.umbc.edu/pub/midia/instruments.tar.gz
Source0:	midia-instruments.tar.bz2
Source1:	http://www.timidity.jp/dist/cfg/midia.cfg
Source2:	http://www.timidity.jp/dist/cfg/gravis.cfg
Source3:	http://www.stardate.bc.ca/eawpatches/eawpats/britepno.pat
Source4:	http://www.stardate.bc.ca/eawpatches/eawpats/pistol.pat
Source5:	timidity-gravis.cfg
Provides:	timidity-instruments = %{patch_pkg_version}
Obsoletes:	timidity-instruments
Group:		Sound
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This package contains a set of instruments for the timidity midi->wave
converter/player.

%prep
%setup -q -c -T -a 0

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/timidity
cp -r instruments %{buildroot}%{_datadir}/timidity/gravis
install -m644 %{SOURCE1} -D %{buildroot}%{_sysconfdir}/timidity/gravis/midia.cfg
install -m644 %{SOURCE2} -D %{buildroot}%{_sysconfdir}/timidity/gravis/gravis.cfg
install -m644 %{SOURCE5} -D %{buildroot}%{_sysconfdir}/timidity/timidity-gravis.cfg
install -m644 %{SOURCE3} -D %{buildroot}%{_datadir}/timidity/gravis/britepno.pat
install -m644 %{SOURCE4} -D %{buildroot}%{_datadir}/timidity/gravis/pistol.pat

%post
%{_sbindir}/update-alternatives --install %{_sysconfdir}/timidity/timidity.cfg timidity.cfg %{_sysconfdir}/timidity/timidity-gravis.cfg 30

%postun
if [ "$1" = "0" ]; then
  %{_sbindir}/update-alternatives --remove timidity.cfg %{_sysconfdir}/timidity/timidity-gravis.cfg
fi

%triggerpostun -- TiMidity++ <= 2.13.2-1mdk
%{_sbindir}/update-alternatives --install %{_sysconfdir}/timidity/timidity.cfg timidity.cfg %{_sysconfdir}/timidity/timidity-gravis.cfg 30

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/timidity/gravis
%dir %{_sysconfdir}/timidity/gravis
%config(noreplace) %{_sysconfdir}/timidity/gravis/gravis.cfg
%config(noreplace) %{_sysconfdir}/timidity/gravis/midia.cfg
%config(noreplace) %{_sysconfdir}/timidity/timidity-gravis.cfg





%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0-30mdv2011.0
+ Revision: 670706
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-29mdv2011.0
+ Revision: 607998
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-28mdv2010.1
+ Revision: 524230
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0-27mdv2010.0
+ Revision: 427378
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0-26mdv2009.0
+ Revision: 225750
- rebuild

* Fri Jan 04 2008 Götz Waschk <waschk@mandriva.org> 1.0-25mdv2008.1
+ Revision: 144832
- fix alternatives uninstallation

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Mar 20 2007 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.0-24mdv2007.1
+ Revision: 146926
- bump release

  + Pixel <pixel@mandriva.com>
    - fix typo making alternatives break (#29527)

* Wed Feb 28 2007 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.0-23mdv2007.1
+ Revision: 126841
- add #extension in config files to avoid old timidity used by SDL_mixer
  gets syntax errors
- fix other broken path

* Wed Feb 28 2007 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.0-22mdv2007.1
+ Revision: 126837
- bump
- fix paths in config

* Wed Dec 13 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.0-21mdv2007.1
+ Revision: 96508
- release
- fix versioned provides

* Wed Dec 13 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.0-20mdv2007.1
+ Revision: 96504
- import old GUS timidity patterns
- Create timidity-patch-gravis

