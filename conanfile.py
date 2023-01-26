from conans import ConanFile, CMake, tools

class Log4cppConan(ConanFile):
  name = "log4cpp"
  version = "1.1.3"
  license = "LGPL-2.1-or-later"
  author = "Holger Detering <freelance@detering-springhoe.de>"
  url = "https://github.com/holger-detering/log4cpp"
  homepage = "https://sourceforge.net/projects/log4cpp"
  description = """\
A library of C++ classes for flexible logging to files (rolling), syslog, IDSA
and other destinations. It is modeled after the Log for Java library
(http://www.log4j.org), staying as close to their API as is reasonable."""
  topics = ("c++", "logging")
  settings = "os", "compiler", "build_type", "arch"
  generators = "cmake"
  exports_sources = "patches/*.patch"
  tool_requires = "libtool/[>=2.4.6]"

  def source(self):
    url = f"https://downloads.sourceforge.net/project/log4cpp/log4cpp-1.1.x%20%28new%29/log4cpp-1.1/log4cpp-{self.version}.tar.gz"
    checksums = self.conan_data["checksums"][self.version][0]
    tools.get(url, sha1=checksums["sha1"], md5=checksums["md5"], verify=False)
    for patch in self.conan_data["patches"][self.version]:
      tools.patch(**patch)

  def _configure_cmake(self):
    cmake = CMake(self)
    cmake.configure(source_folder="log4cpp")
    return cmake

  def build(self):
    self.run("./autogen.sh && ./configure", cwd="log4cpp");
    cmake = self._configure_cmake()
    cmake.build()

  def package(self):
    cmake = self._configure_cmake()
    cmake.install()

  def package_info(self):
    if self.settings.build_type == "Debug":
      self.cpp_info.libs = ["log4cppD"]
    else:
      self.cpp_info.libs = ["log4cpp"]
    if self.settings.os == "Linux":
      self.cpp_info.libs.append("pthread")
