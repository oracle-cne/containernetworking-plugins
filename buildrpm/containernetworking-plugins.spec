
%if 0%{?with_debug}
# https://bugzilla.redhat.com/show_bug.cgi?id=995136#c12
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global _buildhost	build-ol%{?oraclelinux}-%{?_arch}.oracle.com

Name:           containernetworking-plugins 
Version:        1.9.0
Release:        1%{dist}
Summary:        Container Network Interface Plugins - networking plugins for Linux containers
Vendor:         Oracle America
License:        Apache-2.0
Group:          System/Management
Url:            https://github.com/containernetworking/plugins
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  golang
#%{?systemd_requires}
Requires:       flannel-cni-plugin >= 1.2.0
Patch0:         build_linux.sh.patch

Provides: kubernetes-cni-plugins =  %{version}-%{release}
Obsoletes: kubernetes-cni-plugins < 1.8.0

%description
The CNI (Container Network Interface) project consists of a
specification and libraries for writing plugins to configure
network interfaces in Linux containers, along with a number of
supported plugins. CNI concerns itself only with network
connectivity of containers and removing allocated resources when
the container is deleted. Because of this focus, CNI has a wide
range of support and the specification is simple to implement.

This is the minimal CNI configuration for Kubernetes.

%prep
%setup -q -n %{name}-%{version}
%patch0

%build
export VERSION="v%{version}"
chmod +x build_linux.sh
./build_linux.sh

%install
install -m 755 -d %{buildroot}/opt/cni
mv bin/ %{buildroot}/opt/cni/

%files
%license LICENSE THIRD_PARTY_LICENSES.txt
/opt/cni

%changelog
* Tue Dec 09 2025 Oracle Cloud Native Environment Authors <noreply@oracle.com> - 1.9.0-1
- Added Oracle specific build files for Kubernetes CNI Plugins
