Name:		__NAME__
Version:	__SOFTWARE_VERSION__
Release:	__RELEASE_VERSION__
Summary:	__DESC__

License:	__LICENSE__

Requires:	python

%description
__DESC__

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc



%changelog
* Thu Jul 26 2018 zlig <email@example.com>
- Initial build
