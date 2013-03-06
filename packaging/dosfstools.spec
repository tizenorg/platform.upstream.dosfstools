Name:           dosfstools
Version:        3.0.16
Release:        0
License:        GPL-3.0+
Group:          Base/File Systems
Summary:        Utilities for Making and Checking MS-DOS FAT File Systems on Linux
URL:            http://www.daniel-baumann.ch/software/dosfstools/
Source:         %{name}-%{version}.orig.tar.xz
Source1001:     dosfstools.manifest

%description
The dosfstools package includes the mkdosfs and dosfsck utilities,
which respectively make and check MS-DOS FAT file systems on hard
drives or on floppies.

%prep
%setup -q

%build
cp %{SOURCE1001} .
make

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}

rm -rf %{buildroot}%{_datadir}/doc/dosfstools


%docs_package

%files
%manifest dosfstools.manifest
%{_sbindir}/dosfsck
%{_sbindir}/dosfslabel
%{_sbindir}/fsck.msdos
%{_sbindir}/fsck.vfat
%{_sbindir}/mkdosfs
%{_sbindir}/mkfs.msdos
%{_sbindir}/mkfs.vfat
