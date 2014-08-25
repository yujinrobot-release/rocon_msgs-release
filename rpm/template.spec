Name:           ros-indigo-concert-msgs
Version:        0.7.7
Release:        1%{?dist}
Summary:        ROS concert_msgs package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/concert_msgs
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-gateway-msgs
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-rocon-app-manager-msgs
Requires:       ros-indigo-rocon-std-msgs
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-uuid-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-gateway-msgs
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-rocon-app-manager-msgs
BuildRequires:  ros-indigo-rocon-std-msgs
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-uuid-msgs

%description
Shared communication types for the concert framework.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Aug 25 2014 Daniel Stonier <d.stonier@gmail.com> - 0.7.7-1
- Autogenerated by Bloom

* Mon Aug 25 2014 Daniel Stonier <d.stonier@gmail.com> - 0.7.6-1
- Autogenerated by Bloom

* Mon Aug 25 2014 Daniel Stonier <d.stonier@gmail.com> - 0.7.6-0
- Autogenerated by Bloom

* Mon Aug 25 2014 Daniel Stonier <d.stonier@gmail.com> - 0.7.7-0
- Autogenerated by Bloom

