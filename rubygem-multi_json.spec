%define rbname multi_json

Name:       rubygem-%{rbname}
Version:    1.10.1
Release:    1
Summary:    A gem to provide swappable JSON backends
Group:      Development/Ruby
License:    GPLv2+
URL:        http://github.com/intridea/multi_json
Source0:    http://rubygems.org/downloads/%{rbname}-%{version}.gem
BuildRequires: rubygems

Requires:   rubygems
Suggests:   rubygem(rspec)

BuildArch:  noarch


%description
A gem to provide swappable JSON backends utilizing Yajl::Ruby, the JSON gem,
ActiveSupport, or JSON pure.

#-------------------------------------------------------------------------------
%package        doc
Summary:    Documentation for %{name}
Group:      Development/Ruby
Requires:   %{name} = %{version}-%{release}

%description    doc
Documents, Rdoc & RI documentation for %{name}.
#-------------------------------------------------------------------------------
%prep
%setup -q
sed -i /spec.signing_key/d %{rbname}.gemspec

%build
%gem_build

%install
%gem_install


%files
%doc README.md
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/multi_json

%files doc
%doc LICENSE.md
%{ruby_gemdir}/doc/%{rbname}-%{version}



