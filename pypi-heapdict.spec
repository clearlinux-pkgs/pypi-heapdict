#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-heapdict
Version  : 1.0.1
Release  : 31
URL      : https://files.pythonhosted.org/packages/5a/9b/d8963ae7e388270b695f3b556b6dc9adb70ae9618fba09aa1e7b1886652d/HeapDict-1.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/5a/9b/d8963ae7e388270b695f3b556b6dc9adb70ae9618fba09aa1e7b1886652d/HeapDict-1.0.1.tar.gz
Summary  : a heap with decrease-key and increase-key operations
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-heapdict-license = %{version}-%{release}
Requires: pypi-heapdict-python = %{version}-%{release}
Requires: pypi-heapdict-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
===============================================================
        
        heapdict implements the MutableMapping ABC, meaning it works pretty
        much like a regular Python dict.  It's designed to be used as a

%package license
Summary: license components for the pypi-heapdict package.
Group: Default

%description license
license components for the pypi-heapdict package.


%package python
Summary: python components for the pypi-heapdict package.
Group: Default
Requires: pypi-heapdict-python3 = %{version}-%{release}

%description python
python components for the pypi-heapdict package.


%package python3
Summary: python3 components for the pypi-heapdict package.
Group: Default
Requires: python3-core
Provides: pypi(heapdict)

%description python3
python3 components for the pypi-heapdict package.


%prep
%setup -q -n HeapDict-1.0.1
cd %{_builddir}/HeapDict-1.0.1
pushd ..
cp -a HeapDict-1.0.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656401653
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-heapdict
cp %{_builddir}/HeapDict-1.0.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-heapdict/31a389d465048a3fadc191a3c2ffc9f74a79c3b1
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-heapdict/31a389d465048a3fadc191a3c2ffc9f74a79c3b1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
