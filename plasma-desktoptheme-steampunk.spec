Summary:	"SteampunK Powered Linux" Plasma theme
Name:		plasma-desktoptheme-steampunk
Version:	3.0
Release:	1
License:	Creative Commons Attribution-ShareAlike
Group:		Graphical desktop/KDE
Url:		http://kde-look.org/content/show.php?content=157926
Source:		http://kde-look.org/CONTENT/content-files/157926-SteampunK.tar.gz
Requires:	kdebase4-workspace >= 2:4.10
BuildRequires:	kde4-macros
BuildArch:	noarch

%description
This package contains the "SteampunK Powered Linux" Plasma theme.

%files
%{_kde_appsdir}/desktoptheme/SteampunK

#----------------------------------------------------------------------------

%prep
%setup -q -c
find . -type f | xargs chmod 0644
find . -type d | xargs chmod 0755

%build
# nothing

%install
mkdir -p %{buildroot}%{_kde_appsdir}/desktoptheme/

cp -r SteampunK %{buildroot}%{_kde_appsdir}/desktoptheme/

