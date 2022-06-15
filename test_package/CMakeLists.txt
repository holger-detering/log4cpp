cmake_minimum_required(VERSION 3.22)
project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(package_test)
target_sources(package_test PRIVATE test_log4cpp.cpp)
target_include_directories(package_test PRIVATE ${CONAN_INCLUDE_DIRS_LOG4CPP})
target_link_libraries(package_test PRIVATE ${CONAN_LIBS_LOG4CPP})
