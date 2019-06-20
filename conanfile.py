import os
from conans import ConanFile, MSBuild, tools


class ConanvsexampleConan(ConanFile):
    scm = {
        "type": "git",
        "subfolder": "conan-vs-example",
        "url": "auto",
        "revision": "auto"
    }
    name = "conan-vs-example"
    version = "1.0"
    license = "MIT"
    author = "Carlos Z."
    url = "https://github.com/czoido/conan-vs-example"
    description = "Just a simple example of using Conan to package a VS lib"
    topics = ("conan", "libs", "vs")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False],
               "fPIC": [True, False]}
    default_options = "shared=False"
    _source_subfolder = scm.get("subfolder")

    def configure(self):
        if self.settings.compiler == "Visual Studio":
            del self.options.fPIC
        else:
            raise ConanInvalidConfiguration(
                "Library is only supported for Visual Studio")

    def source(self):
        git = tools.Git()
        git.clone(self.scm.get("url"), branch="master")
        git.checkout(self.scm.get("revision"))

    def build(self):
        msbuild = MSBuild(self)
        msbuild.build("conan-vs-example.sln")

    def package(self):
        self._lib_path = ""

        if self.settings.arch == "x86_64":
            self._lib_path = os.path.join("x64", str(self.settings.build_type))
        elif self.settings.arch == "x86":
            self._lib_path = os.path.join(str(self.settings.build_type))

        self.copy("*.h", dst="include",
                  src=os.path.join(self._source_subfolder, "include"))
        self.copy("*.lib", dst="lib", src=self._lib_path, keep_path=False)
        if self.options.shared == True:
            self.copy("*.dll", dst="bin", src=self._lib_path, keep_path=False)
        self.copy("LICENSE", dst="licenses",
                  src=self._source_subfolder, keep_path=False)

    def package_info(self):
        if self.options.shared == False:
            self.cpp_info.libs = ["mydemolib"]
            self.cpp_info.defines = ["LINK_STATIC_LIB"]
        else:
            self.cpp_info.libs = ["mydemodynlib"]
            self.cpp_info.defines = ["LINK_DYNAMIC_LIB"]
