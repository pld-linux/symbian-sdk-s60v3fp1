Summary:	Symbian s60v3 FP1 SDK
Summary(pl.UTF-8):	SDK Symbiana s60v3 FP1
Name:		symbian-sdk-s60v3fp1
Version:	1.07
Release:	2
License:	Nokia EULA
Group:		Developement
Source0:	http://www.martin.st/symbian/gnupoc-package-%{version}.tar.gz
# Source0-md5:	4d3f903c3952b028b54e3ff5c657e527
Source1:	S60-SDK-200634-3.1-Cpp-f.1090b.zip
Source2:	%{name}-gcc4.patch
URL:		http://www.martin.st/symbian/
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1
%define		_noautoreq	/c/Perl/bin/perl

%description
Symbian s60v3 FP1 SDK.

%description -l pl.UTF-8
SDK Symbiana s60v3 FP1.

%prep
%setup -n gnupoc-package-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

cd sdks
./install_gnupoc_s60_31 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/symbian/s60v3fp1

rm -rf $RPM_BUILD_ROOT%{_datadir}/symbian/s60v3fp1/epoc32/tools_orig

install makelinkdir $RPM_BUILD_ROOT%{_bindir}

cd $RPM_BUILD_ROOT
patch -p1 < %{SOURCE2}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc sdks/README
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/symbian
%dir %{_datadir}/symbian/s60v3fp1
%{_datadir}/symbian/s60v3fp1/examples
%{_datadir}/symbian/s60v3fp1/s60ex
%{_datadir}/symbian/s60v3fp1/s60.ico
%{_datadir}/symbian/s60v3fp1/series60doc
%{_datadir}/symbian/s60v3fp1/series60tools

%dir %{_datadir}/symbian/s60v3fp1/epoc32
%{_datadir}/symbian/s60v3fp1/epoc32/cshlpcmp_template
%{_datadir}/symbian/s60v3fp1/epoc32/data
%{_datadir}/symbian/s60v3fp1/epoc32/gcc
%{_datadir}/symbian/s60v3fp1/epoc32/include
%{_datadir}/symbian/s60v3fp1/epoc32/kit
%{_datadir}/symbian/s60v3fp1/epoc32/release
%{_datadir}/symbian/s60v3fp1/epoc32/winscw

%dir %{_datadir}/symbian/s60v3fp1/epoc32/tools
%{_datadir}/symbian/s60v3fp1/epoc32/tools/alp2csh
%{_datadir}/symbian/s60v3fp1/epoc32/tools/build
%{_datadir}/symbian/s60v3fp1/epoc32/tools/captools
%{_datadir}/symbian/s60v3fp1/epoc32/tools/cdb
%{_datadir}/symbian/s60v3fp1/epoc32/tools/charconv
%{_datadir}/symbian/s60v3fp1/epoc32/tools/commdb-schema
%{_datadir}/symbian/s60v3fp1/epoc32/tools/compilation_config
%{_datadir}/symbian/s60v3fp1/epoc32/tools/cshlpcmp
%{_datadir}/symbian/s60v3fp1/epoc32/tools/depcheck
%{_datadir}/symbian/s60v3fp1/epoc32/tools/depmodel
%{_datadir}/symbian/s60v3fp1/epoc32/tools/distrib
%{_datadir}/symbian/s60v3fp1/epoc32/tools/ecmt
%{_datadir}/symbian/s60v3fp1/epoc32/tools/j2me
%{_datadir}/symbian/s60v3fp1/epoc32/tools/perl
%{_datadir}/symbian/s60v3fp1/epoc32/tools/perllib
%{_datadir}/symbian/s60v3fp1/epoc32/tools/productinstaller
%{_datadir}/symbian/s60v3fp1/epoc32/tools/shell
%{_datadir}/symbian/s60v3fp1/epoc32/tools/sipserver
%{_datadir}/symbian/s60v3fp1/epoc32/tools/tz
%{_datadir}/symbian/s60v3fp1/epoc32/tools/variant

%{_datadir}/symbian/s60v3fp1/epoc32/tools/aiftool
%{_datadir}/symbian/s60v3fp1/epoc32/tools/*.bat
%{_datadir}/symbian/s60v3fp1/epoc32/tools/*.bsf
%{_datadir}/symbian/s60v3fp1/epoc32/tools/*.cmd
%{_datadir}/symbian/s60v3fp1/epoc32/tools/*.cwlink
%{_datadir}/symbian/s60v3fp1/epoc32/tools/*.dll
%{_datadir}/symbian/s60v3fp1/epoc32/tools/*.dtd
%{_datadir}/symbian/s60v3fp1/epoc32/tools/emulatorbuild
%{_datadir}/symbian/s60v3fp1/epoc32/tools/*.exe
%{_datadir}/symbian/s60v3fp1/epoc32/tools/*.jar
%{_datadir}/symbian/s60v3fp1/epoc32/tools/*.pm
%{_datadir}/symbian/s60v3fp1/epoc32/tools/*.rsg
%{_datadir}/symbian/s60v3fp1/epoc32/tools/*.txt
%{_datadir}/symbian/s60v3fp1/epoc32/tools/*.xml
%attr(755,root,root) %{_datadir}/symbian/s60v3fp1/epoc32/tools/abld
%attr(755,root,root) %{_datadir}/symbian/s60v3fp1/epoc32/tools/bldmake
%attr(755,root,root) %{_datadir}/symbian/s60v3fp1/epoc32/tools/bmconv
%attr(755,root,root) %{_datadir}/symbian/s60v3fp1/epoc32/tools/elf2e32
%attr(755,root,root) %{_datadir}/symbian/s60v3fp1/epoc32/tools/epoc
%attr(755,root,root) %{_datadir}/symbian/s60v3fp1/epoc32/tools/eshell
%attr(755,root,root) %{_datadir}/symbian/s60v3fp1/epoc32/tools/extmake
%attr(755,root,root) %{_datadir}/symbian/s60v3fp1/epoc32/tools/makekeys
%attr(755,root,root) %{_datadir}/symbian/s60v3fp1/epoc32/tools/makesis
%attr(755,root,root) %{_datadir}/symbian/s60v3fp1/epoc32/tools/makmake
%attr(755,root,root) %{_datadir}/symbian/s60v3fp1/epoc32/tools/mifconv
%attr(755,root,root) %{_datadir}/symbian/s60v3fp1/epoc32/tools/petran
%attr(755,root,root) %{_datadir}/symbian/s60v3fp1/epoc32/tools/pfsdump
%attr(755,root,root) %{_datadir}/symbian/s60v3fp1/epoc32/tools/*.pl
%attr(755,root,root) %{_datadir}/symbian/s60v3fp1/epoc32/tools/rcomp
%attr(755,root,root) %{_datadir}/symbian/s60v3fp1/epoc32/tools/setupcomms
%attr(755,root,root) %{_datadir}/symbian/s60v3fp1/epoc32/tools/signsis
