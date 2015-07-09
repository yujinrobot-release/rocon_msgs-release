Name:           ros-indigo-rocon-service-pair-msgs
Version:        0.7.11
Release:        1%{?dist}
Summary:        ROS rocon_service_pair_msgs package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/rocon_pair_msgs
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-rospy
Requires:       ros-indigo-uuid-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-uuid-msgs

%description
Paired pubsubs generators for non-blocking services.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
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
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Jul 09 2015 Daniel Stonier <d.stonier@gmail.com> - 0.7.11-1
- Autogenerated by Bloom

* Wed May 27 2015 Daniel Stonier <d.stonier@gmail.com> - 0.7.11-0
- Autogenerated by Bloom

* Mon Apr 06 2015 Daniel Stonier <d.stonier@gmail.com> - 0.7.10-0
- Autogenerated by Bloom

* Mon Feb 09 2015 Daniel Stonier <d.stonier@gmail.com> - 0.7.9-0
- Autogenerated by Bloom

* Fri Nov 21 2014 Daniel Stonier <d.stonier@gmail.com> - 0.7.8-0
- Autogenerated by Bloom

* Mon Aug 25 2014 Daniel Stonier <d.stonier@gmail.com> - 0.7.7-1
- Autogenerated by Bloom

* Mon Aug 25 2014 Daniel Stonier <d.stonier@gmail.com> - 0.7.7-0
- Autogenerated by Bloom

* Mon Aug 25 2014 Daniel Stonier <d.stonier@gmail.com> - 0.7.6-1
- Autogenerated by Bloom

* Mon Aug 25 2014 Daniel Stonier <d.stonier@gmail.com> - 0.7.6-0
- Autogenerated by Bloom

