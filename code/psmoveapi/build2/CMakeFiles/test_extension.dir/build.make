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
include CMakeFiles/test_extension.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/test_extension.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/test_extension.dir/flags.make

CMakeFiles/test_extension.dir/examples/c/test_extension.c.o: CMakeFiles/test_extension.dir/flags.make
CMakeFiles/test_extension.dir/examples/c/test_extension.c.o: ../examples/c/test_extension.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/yugeji/Library/psmoveapi/build2/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/test_extension.dir/examples/c/test_extension.c.o"
	/Library/Developer/CommandLineTools/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/test_extension.dir/examples/c/test_extension.c.o   -c /Users/yugeji/Library/psmoveapi/examples/c/test_extension.c

CMakeFiles/test_extension.dir/examples/c/test_extension.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/test_extension.dir/examples/c/test_extension.c.i"
	/Library/Developer/CommandLineTools/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/yugeji/Library/psmoveapi/examples/c/test_extension.c > CMakeFiles/test_extension.dir/examples/c/test_extension.c.i

CMakeFiles/test_extension.dir/examples/c/test_extension.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/test_extension.dir/examples/c/test_extension.c.s"
	/Library/Developer/CommandLineTools/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/yugeji/Library/psmoveapi/examples/c/test_extension.c -o CMakeFiles/test_extension.dir/examples/c/test_extension.c.s

CMakeFiles/test_extension.dir/examples/c/test_extension.c.o.requires:

.PHONY : CMakeFiles/test_extension.dir/examples/c/test_extension.c.o.requires

CMakeFiles/test_extension.dir/examples/c/test_extension.c.o.provides: CMakeFiles/test_extension.dir/examples/c/test_extension.c.o.requires
	$(MAKE) -f CMakeFiles/test_extension.dir/build.make CMakeFiles/test_extension.dir/examples/c/test_extension.c.o.provides.build
.PHONY : CMakeFiles/test_extension.dir/examples/c/test_extension.c.o.provides

CMakeFiles/test_extension.dir/examples/c/test_extension.c.o.provides.build: CMakeFiles/test_extension.dir/examples/c/test_extension.c.o


# Object files for target test_extension
test_extension_OBJECTS = \
"CMakeFiles/test_extension.dir/examples/c/test_extension.c.o"

# External object files for target test_extension
test_extension_EXTERNAL_OBJECTS =

test_extension: CMakeFiles/test_extension.dir/examples/c/test_extension.c.o
test_extension: CMakeFiles/test_extension.dir/build.make
test_extension: libpsmoveapi.3.1.0.dylib
test_extension: CMakeFiles/test_extension.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/yugeji/Library/psmoveapi/build2/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable test_extension"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/test_extension.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/test_extension.dir/build: test_extension

.PHONY : CMakeFiles/test_extension.dir/build

CMakeFiles/test_extension.dir/requires: CMakeFiles/test_extension.dir/examples/c/test_extension.c.o.requires

.PHONY : CMakeFiles/test_extension.dir/requires

CMakeFiles/test_extension.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/test_extension.dir/cmake_clean.cmake
.PHONY : CMakeFiles/test_extension.dir/clean

CMakeFiles/test_extension.dir/depend:
	cd /Users/yugeji/Library/psmoveapi/build2 && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/yugeji/Library/psmoveapi /Users/yugeji/Library/psmoveapi /Users/yugeji/Library/psmoveapi/build2 /Users/yugeji/Library/psmoveapi/build2 /Users/yugeji/Library/psmoveapi/build2/CMakeFiles/test_extension.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/test_extension.dir/depend

