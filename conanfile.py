from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout
from conan.tools.files import apply_conandata_patches, check_md5, check_sha1, get, unzip

import os

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
  options = {"shared": [True, False]}
  default_options = {"shared": True}
  generators = "CMakeDeps", "CMakeToolchain"
  exports_sources = "patches/*.patch", f"sources/log4cpp-{version}.tar.gz"
  tool_requires = "libtool/[>=2.4.6]"
  # todo: cmake >= 3.23?

  def layout(self):
    cmake_layout(self)

  def _fetch_sources(self):
    tarball_name = f"log4cpp-{self.version}.tar.gz"
    url = "https://downloads.sourceforge.net/project/log4cpp/log4cpp-1.1.x%20%28new%29/log4cpp-1.1/" + tarball_name
    source_path = "sources/" + tarball_name
    checksums = self.conan_data["checksums"][self.version][0]
    if os.path.isfile(source_path):
      check_sha1(self, source_path, checksums["sha1"])
      check_md5(self, source_path, checksums["md5"])
      unzip(self, source_path)
    else:
      get(self, url, sha1=checksums["sha1"], md5=checksums["md5"], verify=False)

  def source(self):
    self._fetch_sources()
    apply_conandata_patches(self)

  def _configure_cmake(self):
    cmake = CMake(self)
    cmake.configure(build_script_folder="log4cpp")
    return cmake

  def build(self):
    self.run("./autogen.sh && ./configure",
             cwd=os.path.join(self.folders.base_source,"log4cpp"))
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
