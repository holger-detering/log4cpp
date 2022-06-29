cmake_minimum_required(VERSION 3.18)
project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_executable(package_test)
target_sources(package_test PRIVATE test_log4cpp.cpp)
target_link_libraries(package_test PRIVATE CONAN_PKG::log4cpp)
