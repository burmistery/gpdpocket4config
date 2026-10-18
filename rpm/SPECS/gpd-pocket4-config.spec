Name:		gpd-pocket4-config
Version:	0.1.0
Release:	1%{?dist}
Summary:	Hardware support configuration for GPD Pocket 4

License:	MIT
URL:		https://github.com/burmistery/gpdpocket4config
Source0:	%{name}-%{version}.tar.gz

BuildArch:	noarch

Requires:	systemd
Requires:	iio-sensor-proxy

%description
Hardware support configuration for GPD Pocket 4.

%prep
%setup -q

%build

%install
install -Dpm0755 scripts/niri-autorotate.sh \
    %{buildroot}%{_libexecdir}/niri-autorotate.sh

install -Dpm0644 systemd/niri-autorotate.service \
    %{buildroot}/usr/lib/systemd/user/niri-autorotate.service

%files
%{_libexecdir}/niri-autorotate.sh
/usr/lib/systemd/user/niri-autorotate.service

%changelog
* Sun Oct 18 2026 burmistery
- Initial package
