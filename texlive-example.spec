Name:		texlive-example
Version:	33398
Release:	1
Summary:	Typeset examples for TeX courses
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex209/contrib/misc/example.sty
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/example.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package makes it easier to produce examples for TeX course.
It provides an example environment, which typesets its contents
on the left of the page, and prints it verbatim on the right.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/example/example.sty

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
