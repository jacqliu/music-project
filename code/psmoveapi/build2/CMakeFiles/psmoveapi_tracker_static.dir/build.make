# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.6

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/Cellar/cmake/3.6.2/bin/cmake

# The command to remove a file.
RM = /usr/local/Cellar/cmake/3.6.2/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/yugeji/Library/psmoveapi

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/yugeji/Library/psmoveapi/build2

# Include any dependencies generated for this target.
include CMakeFiles/psmoveapi_tracker_static.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/psmoveapi_tracker_static.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/psmoveapi_tracker_static.dir/flags.make

CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/camera_control.c.o: CMakeFiles/psmoveapi_tracker_static.dir/flags.make
CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/camera_control.c.o: ../src/tracker/camera_control.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/yugeji/Library/psmoveapi/build2/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/camera_control.c.o"
	/Library/Developer/CommandLineTools/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/camera_control.c.o   -c /Users/yugeji/Library/psmoveapi/src/tracker/camera_control.c

CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/camera_control.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/camera_control.c.i"
	/Library/Developer/CommandLineTools/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/yugeji/Library/psmoveapi/src/tracker/camera_control.c > CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/camera_control.c.i

CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/camera_control.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/camera_control.c.s"
	/Library/Developer/CommandLineTools/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/yugeji/Library/psmoveapi/src/tracker/camera_control.c -o CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/camera_control.c.s

CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/camera_control.c.o.requires:

.PHONY : CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/camera_control.c.o.requires

CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/camera_control.c.o.provides: CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/camera_control.c.o.requires
	$(MAKE) -f CMakeFiles/psmoveapi_tracker_static.dir/build.make CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/camera_control.c.o.provides.build
.PHONY : CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/camera_control.c.o.provides

CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/camera_control.c.o.provides.build: CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/camera_control.c.o


CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_tracker.c.o: CMakeFiles/psmoveapi_tracker_static.dir/flags.make
CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_tracker.c.o: ../src/tracker/psmove_tracker.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/yugeji/Library/psmoveapi/build2/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_tracker.c.o"
	/Library/Developer/CommandLineTools/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_tracker.c.o   -c /Users/yugeji/Library/psmoveapi/src/tracker/psmove_tracker.c

CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_tracker.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_tracker.c.i"
	/Library/Developer/CommandLineTools/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/yugeji/Library/psmoveapi/src/tracker/psmove_tracker.c > CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_tracker.c.i

CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_tracker.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_tracker.c.s"
	/Library/Developer/CommandLineTools/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/yugeji/Library/psmoveapi/src/tracker/psmove_tracker.c -o CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_tracker.c.s

CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_tracker.c.o.requires:

.PHONY : CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_tracker.c.o.requires

CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_tracker.c.o.provides: CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_tracker.c.o.requires
	$(MAKE) -f CMakeFiles/psmoveapi_tracker_static.dir/build.make CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_tracker.c.o.provides.build
.PHONY : CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_tracker.c.o.provides

CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_tracker.c.o.provides.build: CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_tracker.c.o


CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/tracker_helpers.c.o: CMakeFiles/psmoveapi_tracker_static.dir/flags.make
CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/tracker_helpers.c.o: ../src/tracker/tracker_helpers.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/yugeji/Library/psmoveapi/build2/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building C object CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/tracker_helpers.c.o"
	/Library/Developer/CommandLineTools/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/tracker_helpers.c.o   -c /Users/yugeji/Library/psmoveapi/src/tracker/tracker_helpers.c

CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/tracker_helpers.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/tracker_helpers.c.i"
	/Library/Developer/CommandLineTools/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/yugeji/Library/psmoveapi/src/tracker/tracker_helpers.c > CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/tracker_helpers.c.i

CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/tracker_helpers.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/tracker_helpers.c.s"
	/Library/Developer/CommandLineTools/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/yugeji/Library/psmoveapi/src/tracker/tracker_helpers.c -o CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/tracker_helpers.c.s

CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/tracker_helpers.c.o.requires:

.PHONY : CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/tracker_helpers.c.o.requires

CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/tracker_helpers.c.o.provides: CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/tracker_helpers.c.o.requires
	$(MAKE) -f CMakeFiles/psmoveapi_tracker_static.dir/build.make CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/tracker_helpers.c.o.provides.build
.PHONY : CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/tracker_helpers.c.o.provides

CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/tracker_helpers.c.o.provides.build: CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/tracker_helpers.c.o


CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_fusion.cpp.o: CMakeFiles/psmoveapi_tracker_static.dir/flags.make
CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_fusion.cpp.o: ../src/tracker/psmove_fusion.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/yugeji/Library/psmoveapi/build2/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_fusion.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_fusion.cpp.o -c /Users/yugeji/Library/psmoveapi/src/tracker/psmove_fusion.cpp

CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_fusion.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_fusion.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/yugeji/Library/psmoveapi/src/tracker/psmove_fusion.cpp > CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_fusion.cpp.i

CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_fusion.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_fusion.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/yugeji/Library/psmoveapi/src/tracker/psmove_fusion.cpp -o CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_fusion.cpp.s

CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_fusion.cpp.o.requires:

.PHONY : CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_fusion.cpp.o.requires

CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_fusion.cpp.o.provides: CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_fusion.cpp.o.requires
	$(MAKE) -f CMakeFiles/psmoveapi_tracker_static.dir/build.make CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_fusion.cpp.o.provides.build
.PHONY : CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_fusion.cpp.o.provides

CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_fusion.cpp.o.provides.build: CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_fusion.cpp.o


CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/psmove_osxsupport.m.o: CMakeFiles/psmoveapi_tracker_static.dir/flags.make
CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/psmove_osxsupport.m.o: ../src/tracker/platform/psmove_osxsupport.m
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/yugeji/Library/psmoveapi/build2/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building C object CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/psmove_osxsupport.m.o"
	/Library/Developer/CommandLineTools/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/psmove_osxsupport.m.o   -c /Users/yugeji/Library/psmoveapi/src/tracker/platform/psmove_osxsupport.m

CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/psmove_osxsupport.m.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/psmove_osxsupport.m.i"
	/Library/Developer/CommandLineTools/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/yugeji/Library/psmoveapi/src/tracker/platform/psmove_osxsupport.m > CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/psmove_osxsupport.m.i

CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/psmove_osxsupport.m.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/psmove_osxsupport.m.s"
	/Library/Developer/CommandLineTools/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/yugeji/Library/psmoveapi/src/tracker/platform/psmove_osxsupport.m -o CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/psmove_osxsupport.m.s

CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/psmove_osxsupport.m.o.requires:

.PHONY : CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/psmove_osxsupport.m.o.requires

CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/psmove_osxsupport.m.o.provides: CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/psmove_osxsupport.m.o.requires
	$(MAKE) -f CMakeFiles/psmoveapi_tracker_static.dir/build.make CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/psmove_osxsupport.m.o.provides.build
.PHONY : CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/psmove_osxsupport.m.o.provides

CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/psmove_osxsupport.m.o.provides.build: CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/psmove_osxsupport.m.o


CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/camera_control_macosx.c.o: CMakeFiles/psmoveapi_tracker_static.dir/flags.make
CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/camera_control_macosx.c.o: ../src/tracker/platform/camera_control_macosx.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/yugeji/Library/psmoveapi/build2/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Building C object CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/camera_control_macosx.c.o"
	/Library/Developer/CommandLineTools/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/camera_control_macosx.c.o   -c /Users/yugeji/Library/psmoveapi/src/tracker/platform/camera_control_macosx.c

CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/camera_control_macosx.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/camera_control_macosx.c.i"
	/Library/Developer/CommandLineTools/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/yugeji/Library/psmoveapi/src/tracker/platform/camera_control_macosx.c > CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/camera_control_macosx.c.i

CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/camera_control_macosx.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/camera_control_macosx.c.s"
	/Library/Developer/CommandLineTools/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/yugeji/Library/psmoveapi/src/tracker/platform/camera_control_macosx.c -o CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/camera_control_macosx.c.s

CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/camera_control_macosx.c.o.requires:

.PHONY : CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/camera_control_macosx.c.o.requires

CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/camera_control_macosx.c.o.provides: CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/camera_control_macosx.c.o.requires
	$(MAKE) -f CMakeFiles/psmoveapi_tracker_static.dir/build.make CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/camera_control_macosx.c.o.provides.build
.PHONY : CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/camera_control_macosx.c.o.provides

CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/camera_control_macosx.c.o.provides.build: CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/camera_control_macosx.c.o


# Object files for target psmoveapi_tracker_static
psmoveapi_tracker_static_OBJECTS = \
"CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/camera_control.c.o" \
"CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_tracker.c.o" \
"CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/tracker_helpers.c.o" \
"CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_fusion.cpp.o" \
"CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/psmove_osxsupport.m.o" \
"CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/camera_control_macosx.c.o"

# External object files for target psmoveapi_tracker_static
psmoveapi_tracker_static_EXTERNAL_OBJECTS =

libpsmoveapi_tracker_static.a: CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/camera_control.c.o
libpsmoveapi_tracker_static.a: CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_tracker.c.o
libpsmoveapi_tracker_static.a: CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/tracker_helpers.c.o
libpsmoveapi_tracker_static.a: CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_fusion.cpp.o
libpsmoveapi_tracker_static.a: CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/psmove_osxsupport.m.o
libpsmoveapi_tracker_static.a: CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/camera_control_macosx.c.o
libpsmoveapi_tracker_static.a: CMakeFiles/psmoveapi_tracker_static.dir/build.make
libpsmoveapi_tracker_static.a: CMakeFiles/psmoveapi_tracker_static.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/yugeji/Library/psmoveapi/build2/CMakeFiles --progress-num=$(CMAKE_PROGRESS_7) "Linking CXX static library libpsmoveapi_tracker_static.a"
	$(CMAKE_COMMAND) -P CMakeFiles/psmoveapi_tracker_static.dir/cmake_clean_target.cmake
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/psmoveapi_tracker_static.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/psmoveapi_tracker_static.dir/build: libpsmoveapi_tracker_static.a

.PHONY : CMakeFiles/psmoveapi_tracker_static.dir/build

CMakeFiles/psmoveapi_tracker_static.dir/requires: CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/camera_control.c.o.requires
CMakeFiles/psmoveapi_tracker_static.dir/requires: CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_tracker.c.o.requires
CMakeFiles/psmoveapi_tracker_static.dir/requires: CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/tracker_helpers.c.o.requires
CMakeFiles/psmoveapi_tracker_static.dir/requires: CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/psmove_fusion.cpp.o.requires
CMakeFiles/psmoveapi_tracker_static.dir/requires: CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/psmove_osxsupport.m.o.requires
CMakeFiles/psmoveapi_tracker_static.dir/requires: CMakeFiles/psmoveapi_tracker_static.dir/src/tracker/platform/camera_control_macosx.c.o.requires

.PHONY : CMakeFiles/psmoveapi_tracker_static.dir/requires

CMakeFiles/psmoveapi_tracker_static.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/psmoveapi_tracker_static.dir/cmake_clean.cmake
.PHONY : CMakeFiles/psmoveapi_tracker_static.dir/clean

CMakeFiles/psmoveapi_tracker_static.dir/depend:
	cd /Users/yugeji/Library/psmoveapi/build2 && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/yugeji/Library/psmoveapi /Users/yugeji/Library/psmoveapi /Users/yugeji/Library/psmoveapi/build2 /Users/yugeji/Library/psmoveapi/build2 /Users/yugeji/Library/psmoveapi/build2/CMakeFiles/psmoveapi_tracker_static.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/psmoveapi_tracker_static.dir/depend

