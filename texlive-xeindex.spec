Name:		texlive-xeindex
Version:	35756
Release:	2
Summary:	Automatic index generation for XeLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/xeindex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xeindex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xeindex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is based on XeSearch, and will automatically index
words or phrases in an XeLaTeX document. Words are declared in
a list, and every occurrence then creates an index entry whose
content can be fully specified beforehand.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/xelatex/xeindex/xeindex.sty
%doc %{_texmfdistdir}/doc/xelatex/xeindex/README
%doc %{_texmfdistdir}/doc/xelatex/xeindex/xeindex.pdf
%doc %{_texmfdistdir}/doc/xelatex/xeindex/xeindex.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
