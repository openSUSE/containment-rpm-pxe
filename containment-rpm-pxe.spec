#
# spec file for package containment-rpm-pxe
#
# Copyright (c) 2021 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           containment-rpm-pxe
Version:        0.2.6
Release:        0
Summary:        Wraps OBS/kiwi-built PXE images in rpms.
License:        MIT
Group:          System/Management
URL:            https://github.com/openSUSE/%{name}
Source:         https://github.com/openSUSE/containment-rpm-pxe/archive/%{version}.tar.gz
BuildRequires:  filesystem
Requires:       fdupes
Requires:       libxml2-tools
Requires:       perl-TimeDate
%if 0%{?sle_version} >= 150100
Requires:       kiwi-systemdeps-disk-images
Requires:       kiwi-systemdeps-image-validation
Requires:       kiwi-boot-descriptions
%endif
BuildArch:      noarch

%description
OBS kiwi_post_run hook to wrap a kiwi-produced PXE image in an rpm package.

%prep
%setup -q -n %{name}-%{version}

%build

%install
mkdir -p %{buildroot}%{_prefix}/lib/build/
install -m 644 image.spec.in %{buildroot}%{_prefix}/lib/build/
install -m 755 kiwi_post_run %{buildroot}%{_prefix}/lib/build/

%files
%{_prefix}/lib/build/kiwi_post_run
%{_prefix}/lib/build/image.spec.in

%changelog
