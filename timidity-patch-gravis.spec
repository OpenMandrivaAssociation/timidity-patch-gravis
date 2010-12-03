%define name	timidity-patch-gravis
%define version	1.0
%define release %mkrel 29

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



