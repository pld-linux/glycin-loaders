Summary:	Sandboxed image rendering
Summary(pl.UTF-8):	Renderowanie obrazów w piaskownicy
Name:		glycin-loaders
Version:	0.1.2
Release:	1
License:	MPL v2.0 or LGPL v2.1+
Group:		Applications
Source0:	https://download.gnome.org/sources/glycin-loaders/0.1/%{name}-%{version}.tar.xz
# Source0-md5:	eef8925be5537cf2901e9d11feff0df2
URL:		https://gitlab.gnome.org/sophie-h/glycin
BuildRequires:	cairo-devel >= 1.17.0
BuildRequires:	cargo
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	gtk4-devel >= 4.12.0
BuildRequires:	libheif-devel >= 1.14.2
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	meson >= 0.57
BuildRequires:	ninja >= 1.5
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	rust
Requires:	cairo >= 1.17.0
Requires:	gtk4 >= 4.12.0
Requires:	libheif >= 1.14.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Glycin allows to decode images into gdk::Textures and to extract image
metadata. The decoding happens in sandboxed modular image loaders.

%description -l pl.UTF-8
Glycin pozwala dekodować obrazy do obiektów gdk::Texture oraz
wydobywać metadane z obrazów. Dekodowanie dzieje się w modułach
wczytujących działających w piaskownicy.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS LICENSE README.md
%dir %{_libexecdir}/glycin-loaders
%dir %{_libexecdir}/glycin-loaders/0+
%attr(755,root,root) %{_libexecdir}/glycin-loaders/0+/glycin-heif
%attr(755,root,root) %{_libexecdir}/glycin-loaders/0+/glycin-image-rs
%attr(755,root,root) %{_libexecdir}/glycin-loaders/0+/glycin-jxl
%attr(755,root,root) %{_libexecdir}/glycin-loaders/0+/glycin-svg
%dir %{_datadir}/glycin-loaders
%dir %{_datadir}/glycin-loaders/0+
%dir %{_datadir}/glycin-loaders/0+/conf.d
%{_datadir}/glycin-loaders/0+/conf.d/glycin-heif.conf
%{_datadir}/glycin-loaders/0+/conf.d/glycin-image-rs.conf
%{_datadir}/glycin-loaders/0+/conf.d/glycin-jxl.conf
%{_datadir}/glycin-loaders/0+/conf.d/glycin-svg.conf
