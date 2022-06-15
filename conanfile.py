from conans import ConanFile, CMake, tools

class Log4cppConan(ConanFile):
    name = "log4cpp"
    version = "1.1.3"
    license = "LGPL-2.1-or-later"
    author = "Bastiaan Bakker <bastiaan.bakker@lifeline.nl>"
    url = "https://sourceforge.net/projects/log4cpp/"
    description = """\
A library of C++ classes for flexible logging to files (rolling), syslog, IDSA
and other destinations. It is modeled after the Log for Java library
(http://www.log4j.org), staying as close to their API as is reasonable."""
    topics = ("c++", "logging")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": True}
    generators = "cmake"

    def source(self):
        self.run("git clone https://git.code.sf.net/p/log4cpp/codegit log4cpp")

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(source_folder="log4cpp")
        return cmake

    def build_requirements(self):
        if self.settings.os == "Linux":
            self.tool_requires("libtool/[>=2.4.6]@")

    def build(self):
        self.run("cd log4cpp && ./autogen.sh && ./configure");
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["log4cpp"]
#        if self.settings.os == "Linux":
#            self.cpp_info.libs.append("pthread")

