import os

from conans import ConanFile, CMake, tools

class Log4cppTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    requires = "log4cpp/1.1.3@"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if not tools.cross_building(self):
            os.chdir("bin")
            self.run(".%spackage_test" % os.sep)
