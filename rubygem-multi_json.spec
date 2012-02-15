%define oname multi_json

Name:       rubygem-%{oname}
Version:    1.0.4
Release:	2
Summary:    A gem to provide swappable JSON backends
Group:      Development/Ruby
License:    GPLv2+
URL:        http://github.com/intridea/multi_json
Source0:    http://rubygems.org/downloads/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
Suggests:   rubygem(rspec)
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
A gem to provide swappable JSON backends utilizing Yajl::Ruby, the JSON gem,
ActiveSupport, or JSON pure.


%prep

%build

%install
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}

rm -f %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/.gitignore
rm -f %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/.rspec
rm -f %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/.travis.yml
rm -f %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/.gemtest

%files
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/.document
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/spec/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Gemfile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/LICENSE.md
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.md
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/%{oname}.gemspec
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
