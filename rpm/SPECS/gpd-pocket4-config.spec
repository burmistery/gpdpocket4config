Name:		gpd-pocket4-config
Version:	0.1.0
Release:	1%{?dist}
Summary:	Hardware support configuration for GPD Pocket 4

License:	MIT
URL:		https://github.com/burmistery/gpdpocket4config
Source0:	scripts/niri-autorotate.sh
Source1:	systemd/niri-autorotate.service

BuildArch:	noarch

Requires:	systemd
Requires:	iio-sensor-proxy

%description
Hardware support configuration for GPD Pocket 4.

%prep

%build

%install
install -Dpm0755 %{SOURCE0} \
    %{buildroot}%{_libexecdir}/niri-autorotate.sh
install -Dpm0644 %{SOURCE1} \
    %{buildroot}%{_userunitdir}/niri-autorotate.service

%files
%{_libexecdir}/niri-autorotate.sh
%{_userunitdir}/niri-autorotate.service

%changelog
* Sun Oct 18 2026 burmistery
- Initial package
