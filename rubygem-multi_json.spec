%define rbname multi_json

Name:       rubygem-%{rbname}
Version:    1.10.1
Release:    2
Summary:    A gem to provide swappable JSON backends
Group:      Development/Ruby
License:    GPLv2+
URL:        https://github.com/intridea/multi_json
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
%dir %{gem_dir}/gems/%{rbname}-%{version}
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib
%{gem_dir}/gems/%{rbname}-%{version}/lib/*.rb
%{gem_dir}/specifications/%{rbname}-%{version}.gemspec
%{gem_dir}/gems/%{rbname}-%{version}/lib/multi_json

%files doc
%doc LICENSE.md
%{gem_dir}/doc/%{rbname}-%{version}



