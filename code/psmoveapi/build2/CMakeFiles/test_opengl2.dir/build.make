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
include CMakeFiles/test_opengl2.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/test_opengl2.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/test_opengl2.dir/flags.make

CMakeFiles/test_opengl2.dir/examples/c/test_opengl2.cpp.o: CMakeFiles/test_opengl2.dir/flags.make
CMakeFiles/test_opengl2.dir/examples/c/test_opengl2.cpp.o: ../examples/c/test_opengl2.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/yugeji/Library/psmoveapi/build2/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/test_opengl2.dir/examples/c/test_opengl2.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/test_opengl2.dir/examples/c/test_opengl2.cpp.o -c /Users/yugeji/Library/psmoveapi/examples/c/test_opengl2.cpp

CMakeFiles/test_opengl2.dir/examples/c/test_opengl2.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test_opengl2.dir/examples/c/test_opengl2.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/yugeji/Library/psmoveapi/examples/c/test_opengl2.cpp > CMakeFiles/test_opengl2.dir/examples/c/test_opengl2.cpp.i

CMakeFiles/test_opengl2.dir/examples/c/test_opengl2.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test_opengl2.dir/examples/c/test_opengl2.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/yugeji/Library/psmoveapi/examples/c/test_opengl2.cpp -o CMakeFiles/test_opengl2.dir/examples/c/test_opengl2.cpp.s

CMakeFiles/test_opengl2.dir/examples/c/test_opengl2.cpp.o.requires:

.PHONY : CMakeFiles/test_opengl2.dir/examples/c/test_opengl2.cpp.o.requires

CMakeFiles/test_opengl2.dir/examples/c/test_opengl2.cpp.o.provides: CMakeFiles/test_opengl2.dir/examples/c/test_opengl2.cpp.o.requires
	$(MAKE) -f CMakeFiles/test_opengl2.dir/build.make CMakeFiles/test_opengl2.dir/examples/c/test_opengl2.cpp.o.provides.build
.PHONY : CMakeFiles/test_opengl2.dir/examples/c/test_opengl2.cpp.o.provides

CMakeFiles/test_opengl2.dir/examples/c/test_opengl2.cpp.o.provides.build: CMakeFiles/test_opengl2.dir/examples/c/test_opengl2.cpp.o


# Object files for target test_opengl2
test_opengl2_OBJECTS = \
"CMakeFiles/test_opengl2.dir/examples/c/test_opengl2.cpp.o"

# External object files for target test_opengl2
test_opengl2_EXTERNAL_OBJECTS =

test_opengl2: CMakeFiles/test_opengl2.dir/examples/c/test_opengl2.cpp.o
test_opengl2: CMakeFiles/test_opengl2.dir/build.make
test_opengl2: libpsmoveapi_tracker.3.1.0.dylib
test_opengl2: /usr/local/lib/libSDL2main.a
test_opengl2: /usr/local/lib/libSDL2.dylib
test_opengl2: libpsmoveapi.3.1.0.dylib
test_opengl2: /usr/local/lib/libopencv_videostab.2.4.13.dylib
test_opengl2: /usr/local/lib/libopencv_ts.a
test_opengl2: /usr/local/lib/libopencv_superres.2.4.13.dylib
test_opengl2: /usr/local/lib/libopencv_stitching.2.4.13.dylib
test_opengl2: /usr/local/lib/libopencv_contrib.2.4.13.dylib
test_opengl2: /usr/local/lib/libopencv_nonfree.2.4.13.dylib
test_opengl2: /usr/local/lib/libopencv_ocl.2.4.13.dylib
test_opengl2: /usr/local/lib/libopencv_gpu.2.4.13.dylib
test_opengl2: /usr/local/lib/libopencv_photo.2.4.13.dylib
test_opengl2: /usr/local/lib/libopencv_objdetect.2.4.13.dylib
test_opengl2: /usr/local/lib/libopencv_legacy.2.4.13.dylib
test_opengl2: /usr/local/lib/libopencv_video.2.4.13.dylib
test_opengl2: /usr/local/lib/libopencv_ml.2.4.13.dylib
test_opengl2: /usr/local/lib/libopencv_calib3d.2.4.13.dylib
test_opengl2: /usr/local/lib/libopencv_features2d.2.4.13.dylib
test_opengl2: /usr/local/lib/libopencv_highgui.2.4.13.dylib
test_opengl2: /usr/local/lib/libopencv_imgproc.2.4.13.dylib
test_opengl2: /usr/local/lib/libopencv_flann.2.4.13.dylib
test_opengl2: /usr/local/lib/libopencv_core.2.4.13.dylib
test_opengl2: CMakeFiles/test_opengl2.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/yugeji/Library/psmoveapi/build2/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable test_opengl2"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/test_opengl2.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/test_opengl2.dir/build: test_opengl2

.PHONY : CMakeFiles/test_opengl2.dir/build

CMakeFiles/test_opengl2.dir/requires: CMakeFiles/test_opengl2.dir/examples/c/test_opengl2.cpp.o.requires

.PHONY : CMakeFiles/test_opengl2.dir/requires

CMakeFiles/test_opengl2.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/test_opengl2.dir/cmake_clean.cmake
.PHONY : CMakeFiles/test_opengl2.dir/clean

CMakeFiles/test_opengl2.dir/depend:
	cd /Users/yugeji/Library/psmoveapi/build2 && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/yugeji/Library/psmoveapi /Users/yugeji/Library/psmoveapi /Users/yugeji/Library/psmoveapi/build2 /Users/yugeji/Library/psmoveapi/build2 /Users/yugeji/Library/psmoveapi/build2/CMakeFiles/test_opengl2.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/test_opengl2.dir/depend
