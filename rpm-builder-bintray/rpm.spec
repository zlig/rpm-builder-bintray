Name:		__NAME__
Version:	__SOFTWARE_VERSION__
Release:	__RELEASE_VERSION__
Summary:	__DESC__

License:	__LICENSE__

Requires:	bash, python

%description
__DESC__

%prep


%build


%install
echo "Hello"
ls -l


%files
%defattr(755,root,root)
%doc

/opt/zlig/hello.sh


%changelog
* Thu Jul 26 2018 zlig <email@example.com>
- Initial build
