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
include CMakeFiles/battery_check.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/battery_check.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/battery_check.dir/flags.make

CMakeFiles/battery_check.dir/examples/c/battery_check.c.o: CMakeFiles/battery_check.dir/flags.make
CMakeFiles/battery_check.dir/examples/c/battery_check.c.o: ../examples/c/battery_check.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/yugeji/Library/psmoveapi/build2/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/battery_check.dir/examples/c/battery_check.c.o"
	/Library/Developer/CommandLineTools/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/battery_check.dir/examples/c/battery_check.c.o   -c /Users/yugeji/Library/psmoveapi/examples/c/battery_check.c

CMakeFiles/battery_check.dir/examples/c/battery_check.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/battery_check.dir/examples/c/battery_check.c.i"
	/Library/Developer/CommandLineTools/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/yugeji/Library/psmoveapi/examples/c/battery_check.c > CMakeFiles/battery_check.dir/examples/c/battery_check.c.i

CMakeFiles/battery_check.dir/examples/c/battery_check.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/battery_check.dir/examples/c/battery_check.c.s"
	/Library/Developer/CommandLineTools/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/yugeji/Library/psmoveapi/examples/c/battery_check.c -o CMakeFiles/battery_check.dir/examples/c/battery_check.c.s

CMakeFiles/battery_check.dir/examples/c/battery_check.c.o.requires:

.PHONY : CMakeFiles/battery_check.dir/examples/c/battery_check.c.o.requires

CMakeFiles/battery_check.dir/examples/c/battery_check.c.o.provides: CMakeFiles/battery_check.dir/examples/c/battery_check.c.o.requires
	$(MAKE) -f CMakeFiles/battery_check.dir/build.make CMakeFiles/battery_check.dir/examples/c/battery_check.c.o.provides.build
.PHONY : CMakeFiles/battery_check.dir/examples/c/battery_check.c.o.provides

CMakeFiles/battery_check.dir/examples/c/battery_check.c.o.provides.build: CMakeFiles/battery_check.dir/examples/c/battery_check.c.o


# Object files for target battery_check
battery_check_OBJECTS = \
"CMakeFiles/battery_check.dir/examples/c/battery_check.c.o"

# External object files for target battery_check
battery_check_EXTERNAL_OBJECTS =

battery_check: CMakeFiles/battery_check.dir/examples/c/battery_check.c.o
battery_check: CMakeFiles/battery_check.dir/build.make
battery_check: libpsmoveapi.3.1.0.dylib
battery_check: CMakeFiles/battery_check.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/yugeji/Library/psmoveapi/build2/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable battery_check"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/battery_check.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/battery_check.dir/build: battery_check

.PHONY : CMakeFiles/battery_check.dir/build

CMakeFiles/battery_check.dir/requires: CMakeFiles/battery_check.dir/examples/c/battery_check.c.o.requires

.PHONY : CMakeFiles/battery_check.dir/requires

CMakeFiles/battery_check.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/battery_check.dir/cmake_clean.cmake
.PHONY : CMakeFiles/battery_check.dir/clean

CMakeFiles/battery_check.dir/depend:
	cd /Users/yugeji/Library/psmoveapi/build2 && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/yugeji/Library/psmoveapi /Users/yugeji/Library/psmoveapi /Users/yugeji/Library/psmoveapi/build2 /Users/yugeji/Library/psmoveapi/build2 /Users/yugeji/Library/psmoveapi/build2/CMakeFiles/battery_check.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/battery_check.dir/depend
