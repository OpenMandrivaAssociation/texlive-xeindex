%global tl_name xeindex
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3
Release:	%{tl_revision}.1
Summary:	Automatic index generation for XeLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/xeindex
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xeindex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xeindex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is based on XeSearch, and will automatically index words or
phrases in an XeLaTeX document. Words are declared in a list, and every
occurrence then creates an index entry whose content can be fully
specified beforehand.

