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
include CMakeFiles/moved.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/moved.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/moved.dir/flags.make

CMakeFiles/moved.dir/src/utils/moved.c.o: CMakeFiles/moved.dir/flags.make
CMakeFiles/moved.dir/src/utils/moved.c.o: ../src/utils/moved.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/yugeji/Library/psmoveapi/build2/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/moved.dir/src/utils/moved.c.o"
	/Library/Developer/CommandLineTools/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/moved.dir/src/utils/moved.c.o   -c /Users/yugeji/Library/psmoveapi/src/utils/moved.c

CMakeFiles/moved.dir/src/utils/moved.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/moved.dir/src/utils/moved.c.i"
	/Library/Developer/CommandLineTools/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/yugeji/Library/psmoveapi/src/utils/moved.c > CMakeFiles/moved.dir/src/utils/moved.c.i

CMakeFiles/moved.dir/src/utils/moved.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/moved.dir/src/utils/moved.c.s"
	/Library/Developer/CommandLineTools/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/yugeji/Library/psmoveapi/src/utils/moved.c -o CMakeFiles/moved.dir/src/utils/moved.c.s

CMakeFiles/moved.dir/src/utils/moved.c.o.requires:

.PHONY : CMakeFiles/moved.dir/src/utils/moved.c.o.requires

CMakeFiles/moved.dir/src/utils/moved.c.o.provides: CMakeFiles/moved.dir/src/utils/moved.c.o.requires
	$(MAKE) -f CMakeFiles/moved.dir/build.make CMakeFiles/moved.dir/src/utils/moved.c.o.provides.build
.PHONY : CMakeFiles/moved.dir/src/utils/moved.c.o.provides

CMakeFiles/moved.dir/src/utils/moved.c.o.provides.build: CMakeFiles/moved.dir/src/utils/moved.c.o


# Object files for target moved
moved_OBJECTS = \
"CMakeFiles/moved.dir/src/utils/moved.c.o"

# External object files for target moved
moved_EXTERNAL_OBJECTS =

moved: CMakeFiles/moved.dir/src/utils/moved.c.o
moved: CMakeFiles/moved.dir/build.make
moved: libpsmoveapi_static.a
moved: CMakeFiles/moved.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/yugeji/Library/psmoveapi/build2/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable moved"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/moved.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/moved.dir/build: moved

.PHONY : CMakeFiles/moved.dir/build

CMakeFiles/moved.dir/requires: CMakeFiles/moved.dir/src/utils/moved.c.o.requires

.PHONY : CMakeFiles/moved.dir/requires

CMakeFiles/moved.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/moved.dir/cmake_clean.cmake
.PHONY : CMakeFiles/moved.dir/clean

CMakeFiles/moved.dir/depend:
	cd /Users/yugeji/Library/psmoveapi/build2 && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/yugeji/Library/psmoveapi /Users/yugeji/Library/psmoveapi /Users/yugeji/Library/psmoveapi/build2 /Users/yugeji/Library/psmoveapi/build2 /Users/yugeji/Library/psmoveapi/build2/CMakeFiles/moved.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/moved.dir/depend
