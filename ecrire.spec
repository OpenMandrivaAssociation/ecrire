Summary: 	Enlightenment text editor
Name: 		ecrire
Version:	0.2.0
Release:	1
License:	BSD
Group:		Editors/Enlightenment
URL:		http://www.enlightenment.org/
Source0:	https://download.enlightenment.org/rel/apps/ecrire/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(efl)
BuildRequires:  gettext-devel
BuildRequires:	cmake
BuildRequires:  meson

%description
This is a text editor.

Ecrire is a basic text editor written in EFL for the Enlightenment desktop environment. 
It is intended to be a native EFL alternative to gedit (GTK/Gnome), kwrite (KDE/Plasma), and similar basic text editors. 
With the exception that ecrire should be usable on desktop as well as mobile devices.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README NEWS TODO
%{_bindir}/ecrire
%{_datadir}/applications/ecrire.desktop
%{_iconsdir}/hicolor/*x*/apps/ecrire.png
%{_iconsdir}/hicolor/scalable/apps/ecrire.svg
%{_datadir}/icons/ecrire.*
%exclude %{_datadir}/ecrire/AUTHORS
%exclude %{_datadir}/ecrire/COPYING
