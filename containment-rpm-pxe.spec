# Copyright (c) 2018 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# norootforbuild

Name:           containment-rpm-pxe
Version:        0.1
Release:        0
License:        MIT
Summary:        Wraps OBS/kiwi-built PXE images in rpms.
Url:            https://github.com/openSUSE/%{name}
Group:          System/Management
Source:         %{name}-%{version}.tar.gz
BuildRequires:  filesystem
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires:       libxml2-tools

%description
OBS kiwi_post_run hook to wrap a kiwi-produced PXE image in an rpm package.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/usr/lib/build/
install -m 644 image.spec.in %{buildroot}/usr/lib/build/
install -m 755 kiwi_post_run %{buildroot}/usr/lib/build/

%files
%defattr(-,root,root)
/usr/lib/build/kiwi_post_run
/usr/lib/build/image.spec.in

%changelog
