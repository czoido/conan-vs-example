import os
from conans import ConanFile, MSBuild, tools


class TestVSConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "conan-vs-example/1.0@czoido/testing"
    generators = "visual_studio"

    def build(self):
        msbuild = MSBuild(self)
        msbuild.build(os.path.join(self.source_folder, "test_package.sln"),
                      property_file_name="conan_build.props")

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.lib", dst="lib", src="lib")

    def test(self):
        if not tools.cross_building(self.settings):
            self._bin_path = ""

            if self.settings.arch == "x86_64":
                self._bin_path = os.path.join(
                    self.source_folder, "x64", str(self.settings.build_type))
            elif self.settings.arch == "x86":
                self._bin_path = os.path.join(
                    self.source_folder, str(self.settings.build_type))

            self.run(os.path.join(self.source_folder, self._bin_path,
                                  "test_package"), run_environment=True)
