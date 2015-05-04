%define git	20150504

Epoch:	1
Summary: 	Enlightened text editor
Name: 		ecrire
Version:	0.1.0
Release:	1.%{git}.2
License:	BSD
Group:		Video
URL:		http://www.enlightenment.org/
Source0:	%{name}-%{git}.tar.gz

BuildRequires:	pkgconfig(eet)
BuildRequires:	pkgconfig(eina)
BuildRequires:	pkgconfig(ecore)
BuildRequires:	pkgconfig(edje)
BuildRequires:	pkgconfig(efreet)
BuildRequires:	pkgconfig(evas)
BuildRequires:	pkgconfig(elementary)
BuildRequires:	cmake

%description
This is a text editor.

This is a WORK IN PROGRESS - it is NOT COMPLETE. do not expect everything to
work and do what you want.

%prep
%setup -qn %{name}-%{git}

%build
%cmake
%make

%install
%makeinstall_std -C build

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README ChangeLog NEWS TODO
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_iconsdir}/%name.png
