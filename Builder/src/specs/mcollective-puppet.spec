# VERSION is subbed  let me out during rake srpm process
%global realversion 1.10.0
%global rpmversion <rpm.version>
%global realname mcollective-puppet-agent
%global packager <ericsson.rstate>

Summary:   Manage the puppet agent with MCollective
Name:      EXTRlitpmcollectivepuppetagent_CXP9031035
Version:   %{rpmversion}
Release:   1
Vendor:    PuppetLabs
License:   ASL 2.0
URL:       https://github.com/puppetlabs/mcollective-puppet-agent
BuildRoot: %{_tmppath}/%{realname}-%{realversion}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
Group:     System Tools
Source0:   mcollective-puppet-agent-%{realversion}.tar.gz
Requires:  mcollective-puppet-common = %{realversion}-%{release}
Provides:  mcollective-puppet-agent = 1.10.0
Packager:  %{packager}

%description
mcollective-puppet-agent 1.10.0 repackaged by Ericsson from Puppet Labs source code.
Manage the puppet agent with MCollective

%prep
%setup -q  -n %{realname}-%{realversion}

%build
patch -p0 -i ../../../src/patchFiles/patch.litpcds11690
patch -p0 -i ../../../src/patchFiles/patch.litpcds13763

%install
rm -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_libexecdir}/mcollective/mcollective
cp -a agent aggregate application data util validator %{buildroot}%{_libexecdir}/mcollective/mcollective

%clean
rm -rf %{buildroot}

%package -n EXTRlitpmcollectivepuppetclient_CXP9031354
Requires: mcollective-puppet-common = %{realversion}-%{release}
Provides: mcollective-puppet-client = 1.10.0
Group: System Tools
Summary:   Manage the puppet agent with MCollective

%package -n EXTRlitpmcollectivepuppetcommon_CXP9031355
Requires: mcollective-common >= 2.2.1
Provides: mcollective-puppet-common = 1.10.0
Group: System Tools
Summary:   Manage the puppet agent with MCollective

%description -n EXTRlitpmcollectivepuppetclient_CXP9031354
mcollective-puppet-client 1.10.0 repackaged by Ericsson from Puppet Labs source code.
Manage the puppet agent with MCollective 

%description -n EXTRlitpmcollectivepuppetcommon_CXP9031355
mcollective-puppet-common 1.10.0 repackaged by Ericsson from Puppet Labs source code.
Manage the puppet agent with MCollective

%files 
%{_libexecdir}/mcollective/mcollective/agent/*.rb

%files -n EXTRlitpmcollectivepuppetclient_CXP9031354
%{_libexecdir}/mcollective/mcollective/aggregate/*
%{_libexecdir}/mcollective/mcollective/application/*

%files -n EXTRlitpmcollectivepuppetcommon_CXP9031355
%{_libexecdir}/mcollective/mcollective/agent/*.ddl
%{_libexecdir}/mcollective/mcollective/data/*
%{_libexecdir}/mcollective/mcollective/util/*
%{_libexecdir}/mcollective/mcollective/validator/*

