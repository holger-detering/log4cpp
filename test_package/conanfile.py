from conan import ConanFile
from conan.tools.cmake import CMake,cmake_layout
from conan.tools.build import can_run

import os

class Log4cppTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"
    #requires = "log4cpp/1.1.3@"

    def requirements(self):
        self.requires(self.tested_reference_str)

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if not can_run(self):
            os.chdir("bin")
            cmd = os.path.join(self.cpp.build.bindir, "package_test")
            self.run(cmd, env="conanrun")
