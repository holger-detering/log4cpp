from conan import ConanFile
from conan.tools.cmake import CMake
from conan.tools.layout import cmake_layout
from conan.tools.build import can_run

import os

class Log4cppTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

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
            cmd = os.path.join(self.cpp.build.bindir, "package_test")
            self.run(cmd, env="conanrun")
