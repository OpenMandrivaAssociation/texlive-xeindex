# revision 16760
# category Package
# catalog-ctan /macros/xetex/latex/xeindex
# catalog-date 2010-01-17 14:52:57 +0100
# catalog-license lppl
# catalog-version 0.2
Name:		texlive-xeindex
Version:	0.2
Release:	1
Summary:	Automatic index generation for XeLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xetex/latex/xeindex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xeindex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xeindex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package is based on XeSearch, and will automatically index
words or phrases in an XeLaTeX document. Words are declared in
a list, and every occurrence then creates an index entry whose
content can be fully specified beforehand.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/xelatex/xeindex/xeindex.sty
%doc %{_texmfdistdir}/doc/xelatex/xeindex/README
%doc %{_texmfdistdir}/doc/xelatex/xeindex/xeindex.pdf
%doc %{_texmfdistdir}/doc/xelatex/xeindex/xeindex.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
