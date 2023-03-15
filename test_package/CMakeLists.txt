cmake_minimum_required(VERSION 3.18)
project(PackageTest CXX)

find_package(log4cpp CONFIG REQUIRED)

add_executable(package_test)
target_sources(package_test PRIVATE test_log4cpp.cpp)
target_link_libraries(package_test PRIVATE log4cpp::log4cpp)
