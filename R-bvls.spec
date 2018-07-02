#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-bvls
Version  : 1.4
Release  : 1
URL      : https://cran.r-project.org/src/contrib/bvls_1.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/bvls_1.4.tar.gz
Summary  : The Stark-Parker algorithm for bounded-variable least squares
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-bvls-lib
Requires: R-nnls
Requires: R-quadprog
BuildRequires : R-nnls
BuildRequires : R-quadprog
BuildRequires : clr-R-helpers

%description
algorithm for bounded-variable least squares

%package lib
Summary: lib components for the R-bvls package.
Group: Libraries

%description lib
lib components for the R-bvls package.


%prep
%setup -q -c -n bvls

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530509562

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1530509562
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bvls
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bvls
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bvls
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library bvls|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/bvls/COPYRIGHTS
/usr/lib64/R/library/bvls/DESCRIPTION
/usr/lib64/R/library/bvls/INDEX
/usr/lib64/R/library/bvls/Meta/Rd.rds
/usr/lib64/R/library/bvls/Meta/features.rds
/usr/lib64/R/library/bvls/Meta/hsearch.rds
/usr/lib64/R/library/bvls/Meta/links.rds
/usr/lib64/R/library/bvls/Meta/nsInfo.rds
/usr/lib64/R/library/bvls/Meta/package.rds
/usr/lib64/R/library/bvls/NAMESPACE
/usr/lib64/R/library/bvls/R/bvls
/usr/lib64/R/library/bvls/R/bvls.rdb
/usr/lib64/R/library/bvls/R/bvls.rdx
/usr/lib64/R/library/bvls/help/AnIndex
/usr/lib64/R/library/bvls/help/aliases.rds
/usr/lib64/R/library/bvls/help/bvls.rdb
/usr/lib64/R/library/bvls/help/bvls.rdx
/usr/lib64/R/library/bvls/help/paths.rds
/usr/lib64/R/library/bvls/html/00Index.html
/usr/lib64/R/library/bvls/html/R.css
/usr/lib64/R/library/bvls/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/bvls/libs/bvls.so
/usr/lib64/R/library/bvls/libs/bvls.so.avx2
/usr/lib64/R/library/bvls/libs/bvls.so.avx512
