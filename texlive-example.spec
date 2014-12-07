# revision 33398
# category Package
# catalog-ctan /macros/latex209/contrib/misc/example.sty
# catalog-date 2014-04-08 11:06:38 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-example
Version:	20140408
Release:	3
Summary:	Typeset examples for TeX courses
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex209/contrib/misc/example.sty
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/example.tar.xz
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
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
