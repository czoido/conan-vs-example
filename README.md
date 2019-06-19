# conan-vs-example
Just a simple example of using Conan to package a VS lib

## How to Use

1. Install conan: https://docs.conan.io/en/latest/installation.html
2. Clone this repo: `git clone https://github.com/czoido/conan-vs-example.git`
3. Create package: `conan create . user/channel`
That will create the package with the default profile.
If you want to check the test_package links dynamic or static library depending on the input configuration change to something like this:

`conan create . user/channel -s build_type=Release -o *:shared=True`

At the end the test should output: `HELLO! (Release Static)`
