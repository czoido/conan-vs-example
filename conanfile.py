from conans import ConanFile, CMake, tools


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
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
	_source_subfolder = scm.subfolder;

    def source(self):
        git = tools.Git()
        git.clone(self.scm.url, branch="master")
        git.checkout(self.scm.revision)

    def build(self):
        msbuild = MSBuild(self)
        msbuild.build("conan-vs-example.sln")

    def package(self):
        self.copy("*.h", dst="include", src="hello")
        self.copy("*hello.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["mydemolib"]
