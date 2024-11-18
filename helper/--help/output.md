# Options()
## basic()

---
### --help

原始参数名:
```
--help
```
中文参数名:
```

```
原始简介:
```
show this help message and exit
```
中文简介:
```

```

---
### --version

原始参数名:
```
--version
```
中文参数名:
```

```
原始简介:
```
Show version information and important details for bug reports, then exit.
Defaults to off.
```
中文简介:
```

```

---
### --module

原始参数名:
```
--module
```
中文参数名:
```

```
原始简介:
```
Create an importable binary extension module executable instead of a program.
Defaults to off.
```
中文简介:
```

```

---
### --mode=COMPILATION_MODE

原始参数名:
```
--mode=COMPILATION_MODE
```
中文参数名:
```

```
原始简介:
```
Mode in which to compile. Accelerated runs in your Python installation and
depends on it. Standalone creates a folder with an executable contained to run
it. Onefile creates a single executable to deploy. Default is 'accelerated'.
```
中文简介:
```

```

---
### --standalone

原始参数名:
```
--standalone
```
中文参数名:
```

```
原始简介:
```
Enable standalone mode for output. This allows you to transfer the created
binary to other machines without it using an existing Python installation. This
also means it will become big. It implies these option: "-- follow-imports" and
"--python-flag=no_site". Defaults to off.
```
中文简介:
```

```

---
### --onefile

原始参数名:
```
--onefile
```
中文参数名:
```

```
原始简介:
```
On top of standalone mode, enable onefile mode. This means not a folder, but a
compressed executable is created and used. Defaults to off.
```
中文简介:
```

```

---
### --python-flag=FLAG

原始参数名:
```
--python-flag=FLAG
```
中文参数名:
```

```
原始简介:
```
Python flags to use. Default is what you are using to run Nuitka, this enforces
a specific mode. These are options that also exist to standard Python
executable. Currently supported: "-S" (alias "no_site"), "static_hashes" (do not
use hash randomization), "no_warnings" (do not give Python run time warnings),
"-O" (alias "no_asserts"), "no_docstrings" (do not use doc strings), "-u" (alias
"unbuffered"), "isolated" (do not load outside code) and "-m" (package mode,
compile as "package.__main__"). Default empty.
```
中文简介:
```

```

---
### --python-debug

原始参数名:
```
--python-debug
```
中文参数名:
```

```
原始简介:
```
Use debug version or not. Default uses what you are using to run Nuitka, most
likely a non-debug version. Only for debugging and testing purposes.
```
中文简介:
```

```

---
### --python-for-scons=PATH

原始参数名:
```
--python-for-scons=PATH
```
中文参数名:
```

```
原始简介:
```
When compiling with Python 3.4 provide the path of a Python binary to use for
Scons. Otherwise Nuitka can use what you run Nuitka with, or find Python
installation, e.g. from Windows registry. On Windows, a Python 3.5 or higher is
needed. On non-Windows, a Python 2.6 or 2.7 will do as well.
```
中文简介:
```

```

---
### --main=PATH

原始参数名:
```
--main=PATH
```
中文参数名:
```

```
原始简介:
```
If specified once, this takes the place of the positional argument, i.e. the
filename to compile. When given multiple times, it enables "multidist" (see User
Manual) it allows you to create binaries that depending on file name or
invocation name.
```
中文简介:
```

```

---

---
## Control the inclusion of modules and packages in result()

---
### --include-package=PACKAGE

原始参数名:
```
--include-package=PACKAGE
```
中文参数名:
```

```
原始简介:
```
Include a whole package. Give as a Python namespace, e.g.
"some_package.sub_package" and Nuitka will then find it and include it and all
the modules found below that disk location in the binary or extension module it
creates, and make it available for import by the code. To avoid unwanted sub
packages, e.g. tests you can e.g. do this "--nofollow-import-to=*.tests".
Default empty.
```
中文简介:
```

```

---
### --include-module=MODULE

原始参数名:
```
--include-module=MODULE
```
中文参数名:
```

```
原始简介:
```
Include a single module. Give as a Python namespace, e.g.
"some_package.some_module" and Nuitka will then find it and include it in the
binary or extension module it creates, and make it available for import by the
code. Default empty.
```
中文简介:
```

```

---
### --include-plugin-directory=MODULE/PACKAGE

原始参数名:
```
--include-plugin-directory=MODULE/PACKAGE
```
中文参数名:
```

```
原始简介:
```
Include also the code found in that directory, considering as if they are each
given as a main file. Overrides all other inclusion options. You ought to prefer
other inclusion options, that go by names, rather than filenames, those find
things through being in "sys.path". This option is for very special use cases
only. Can be given multiple times. Default empty.
```
中文简介:
```

```

---
### --include-plugin-files=PATTERN

原始参数名:
```
--include-plugin-files=PATTERN
```
中文参数名:
```

```
原始简介:
```
Include into files matching the PATTERN. Overrides all other follow options.
Can be given multiple times. Default empty.
```
中文简介:
```

```

---
### --prefer-source-code

原始参数名:
```
--prefer-source-code
```
中文参数名:
```

```
原始简介:
```
For already compiled extension modules, where there is both a source file and
an extension module, normally the extension module is used, but it should be
better to compile the module from available source code for best performance. If
not desired, there is --no- prefer-source-code to disable warnings about it.
Default off.
```
中文简介:
```

```

---

---
## Control the following into imported modules()

---
### --follow-imports

原始参数名:
```
--follow-imports
```
中文参数名:
```

```
原始简介:
```
Descend into all imported modules. Defaults to on in standalone mode, otherwise
off.
```
中文简介:
```

```

---
### --follow-import-to=MODULE/PACKAGE

原始参数名:
```
--follow-import-to=MODULE/PACKAGE
```
中文参数名:
```

```
原始简介:
```
Follow to that module if used, or if a package, to the whole package. Can be
given multiple times. Default empty.
```
中文简介:
```

```

---
### --nofollow-import-to=MODULE/PACKAGE

原始参数名:
```
--nofollow-import-to=MODULE/PACKAGE
```
中文参数名:
```

```
原始简介:
```
Do not follow to that module name even if used, or if a package name, to the
whole package in any case, overrides all other options. This can also contain
patterns, e.g. "*.tests". Can be given multiple times. Default empty.
```
中文简介:
```

```

---
### --nofollow-imports

原始参数名:
```
--nofollow-imports
```
中文参数名:
```

```
原始简介:
```
Do not descend into any imported modules at all, overrides all other inclusion
options and not usable for standalone mode. Defaults to off.
```
中文简介:
```

```

---
### --follow-stdlib

原始参数名:
```
--follow-stdlib
```
中文参数名:
```

```
原始简介:
```
Also descend into imported modules from standard library. This will increase
the compilation time by a lot and is also not well tested at this time and
sometimes won't work. Defaults to off.
```
中文简介:
```

```

---

---
## Onefile options()

---
### --onefile-tempdir-spec=ONEFILE_TEMPDIR_SPEC

原始参数名:
```
--onefile-tempdir-spec=ONEFILE_TEMPDIR_SPEC
```
中文参数名:
```

```
原始简介:
```
Use this as a folder to unpack to in onefile mode. Defaults to
'{TEMP}/onefile_{PID}_{TIME}', i.e. user temporary directory and being
non-static it's removed. Use e.g. a string like
'{CACHE_DIR}/{COMPANY}/{PRODUCT}/{VERSION}' which is a good static cache path,
this will then not be removed.
```
中文简介:
```

```

---
### --onefile-child-grace-time=GRACE_TIME_MS

原始参数名:
```
--onefile-child-grace-time=GRACE_TIME_MS
```
中文参数名:
```

```
原始简介:
```
When stopping the child, e.g. due to CTRL-C or shutdown, etc. the Python code
gets a "KeyboardInterrupt", that it may handle e.g. to flush data. This is the
amount of time in ms, before the child it killed in the hard way. Unit is ms,
and default 5000.
```
中文简介:
```

```

---
### --onefile-no-compression

原始参数名:
```
--onefile-no-compression
```
中文参数名:
```

```
原始简介:
```
When creating the onefile, disable compression of the payload. This is mostly
for debug purposes, or to save time. Default is off.
```
中文简介:
```

```

---
### --onefile-as-archive

原始参数名:
```
--onefile-as-archive
```
中文参数名:
```

```
原始简介:
```
When creating the onefile, use an archive format, that can be unpacked with
"nuitka-onefile-unpack" rather than a stream that only the onefile program
itself unpacks. Default is off.
```
中文简介:
```

```

---

---
## Data files()

---
### --include-package-data=PACKAGE

原始参数名:
```
--include-package-data=PACKAGE
```
中文参数名:
```

```
原始简介:
```
Include data files for the given package name. DLLs and extension modules are
not data files and never included like this. Can use patterns the filenames as
indicated below. Data files of packages are not included by default, but package
configuration can do it. This will only include non-DLL, non-extension modules,
i.e. actual data files. After a ":" optionally a filename pattern can be given
as well, selecting only matching files. Examples: "--include-
package-data=package_name" (all files) "--include-
package-data=package_name=*.txt" (only certain type) "
--include-package-data=package_name=some_filename.dat (concrete file) Default
empty.
```
中文简介:
```

```

---
### --include-data-files=DESC

原始参数名:
```
--include-data-files=DESC
```
中文参数名:
```

```
原始简介:
```
Include data files by filenames in the distribution. There are many allowed
forms. With '--include-data- files=/path/to/file/*.txt=folder_name/some.txt' it
will copy a single file and complain if it's multiple. With '--include-data-
files=/path/to/files/*.txt=folder_name/' it will put all matching files into
that folder. For recursive copy there is a form with 3 values that '--include-
data-files=/path/to/scan=folder_name/=**/*.txt' that will preserve directory
structure. Default empty.
```
中文简介:
```

```

---
### --include-data-dir=DIRECTORY

原始参数名:
```
--include-data-dir=DIRECTORY
```
中文参数名:
```

```
原始简介:
```
Include data files from complete directory in the distribution. This is
recursive. Check '--include- data-files' with patterns if you want non-recursive
inclusion. An example would be '--include-data-
dir=/path/some_dir=data/some_dir' for plain copy, of the whole directory. All
non-code files are copied, if you want to use '--noinclude-data-files' option to
remove them. Default empty.
```
中文简介:
```

```

---
### --noinclude-data-files=PATTERN

原始参数名:
```
--noinclude-data-files=PATTERN
```
中文参数名:
```

```
原始简介:
```
Do not include data files matching the filename pattern given. This is against
the target filename, not source paths. So to ignore a file pattern from package
data for 'package_name' should be matched as 'package_name/*.txt'. Or for the
whole directory simply use 'package_name'. Default empty.
```
中文简介:
```

```

---
### --include-onefile-external-data=PATTERN

原始参数名:
```
--include-onefile-external-data=PATTERN
```
中文参数名:
```

```
原始简介:
```
Include the specified data file patterns outside of the onefile binary, rather
than on the inside. Makes only sense in case of '--onefile' compilation. First
files have to be specified as included with other `--include-*data*` options,
and then this refers to target paths inside the distribution. Default empty.
```
中文简介:
```

```

---
### --list-package-data=LIST_PACKAGE_DATA

原始参数名:
```
--list-package-data=LIST_PACKAGE_DATA
```
中文参数名:
```

```
原始简介:
```
Output the data files found for a given package name. Default not done.
```
中文简介:
```

```

---
### --include-raw-dir=DIRECTORY

原始参数名:
```
--include-raw-dir=DIRECTORY
```
中文参数名:
```

```
原始简介:
```
Include raw directories completely in the distribution. This is recursive.
Check '--include- data-dir' to use the sane option. Default empty.
```
中文简介:
```

```

---

---
## Metadata support()

---
### --include-distribution-metadata=DISTRIBUTION

原始参数名:
```
--include-distribution-metadata=DISTRIBUTION
```
中文参数名:
```

```
原始简介:
```
Include metadata information for the given distribution name. Some packages
check metadata for presence, version, entry points, etc. and without this option
given, it only works when it's recognized at compile time which is not always
happening. This of course only makes sense for packages that are included in the
compilation. Default empty.
```
中文简介:
```

```

---

---
## DLL files()

---
### --noinclude-dlls=PATTERN

原始参数名:
```
--noinclude-dlls=PATTERN
```
中文参数名:
```

```
原始简介:
```
Do not include DLL files matching the filename pattern given. This is against
the target filename, not source paths. So ignore a DLL 'someDLL' contained in
the package 'package_name' it should be matched as 'package_name/someDLL.*'.
Default empty.
```
中文简介:
```

```

---
### --list-package-dlls=LIST_PACKAGE_DLLS

原始参数名:
```
--list-package-dlls=LIST_PACKAGE_DLLS
```
中文参数名:
```

```
原始简介:
```
Output the DLLs found for a given package name. Default not done.
```
中文简介:
```

```

---

---
## Control the warnings to be given by Nuitka()

---
### --warn-implicit-exceptions

原始参数名:
```
--warn-implicit-exceptions
```
中文参数名:
```

```
原始简介:
```
Enable warnings for implicit exceptions detected at compile time.
```
中文简介:
```

```

---
### --warn-unusual-code

原始参数名:
```
--warn-unusual-code
```
中文参数名:
```

```
原始简介:
```
Enable warnings for unusual code detected at compile time.
```
中文简介:
```

```

---
### --assume-yes-for-downloads

原始参数名:
```
--assume-yes-for-downloads
```
中文参数名:
```

```
原始简介:
```
Allow Nuitka to download external code if necessary, e.g. dependency walker,
ccache, and even gcc on Windows. To disable, redirect input from nul device,
e.g. "</dev/null" or "<NUL:". Default is to prompt.
```
中文简介:
```

```

---
### --nowarn-mnemonic=MNEMONIC

原始参数名:
```
--nowarn-mnemonic=MNEMONIC
```
中文参数名:
```

```
原始简介:
```
Disable warning for a given mnemonic. These are given to make sure you are
aware of certain topics, and typically point to the Nuitka website. The mnemonic
is the part of the URL at the end, without the HTML suffix. Can be given
multiple times and accepts shell pattern. Default empty.
```
中文简介:
```

```

---

---
## Immediate execution after compilation()

---
### --run

原始参数名:
```
--run
```
中文参数名:
```

```
原始简介:
```
Execute immediately the created binary (or import the compiled module).
Defaults to off.
```
中文简介:
```

```

---
### --debugger

原始参数名:
```
--debugger
```
中文参数名:
```

```
原始简介:
```
Execute inside a debugger, e.g. "gdb" or "lldb" to automatically get a stack
trace. Defaults to off.
```
中文简介:
```

```

---

---
## Compilation choices()

---
### --user-package-configuration-file=YAML_FILENAME

原始参数名:
```
--user-package-configuration-file=YAML_FILENAME
```
中文参数名:
```

```
原始简介:
```
User provided Yaml file with package configuration. You can include DLLs,
remove bloat, add hidden dependencies. Check the Nuitka Package Configuration
Manual for a complete description of the format to use. Can be given multiple
times. Defaults to empty.
```
中文简介:
```

```

---
### --full-compat

原始参数名:
```
--full-compat
```
中文参数名:
```

```
原始简介:
```
Enforce absolute compatibility with CPython. Do not even allow minor deviations
from CPython behavior, e.g. not having better tracebacks or exception messages
which are not really incompatible, but only different or worse. This is intended
for tests only and should *not* be used.
```
中文简介:
```

```

---
### --file-reference-choice=MODE

原始参数名:
```
--file-reference-choice=MODE
```
中文参数名:
```

```
原始简介:
```
Select what value "__file__" is going to be. With "runtime" (default for
standalone binary mode and module mode), the created binaries and modules, use
the location of themselves to deduct the value of "__file__". Included packages
pretend to be in directories below that location. This allows you to include
data files in deployments. If you merely seek acceleration, it's better for you
to use the "original" value, where the source files location will be used. With
"frozen" a notation "<frozen module_name>" is used. For compatibility reasons,
the "__file__" value will always have ".py" suffix independent of what it really
is.
```
中文简介:
```

```

---
### --module-name-choice=MODE

原始参数名:
```
--module-name-choice=MODE
```
中文参数名:
```

```
原始简介:
```
Select what value "__name__" and "__package__" are going to be. With "runtime"
(default for module mode), the created module uses the parent package to deduce
the value of "__package__", to be fully compatible. The value "original"
(default for other modes) allows for more static optimization to happen, but is
incompatible for modules that normally can be loaded into any package.
```
中文简介:
```

```

---

---
## Output choices()

---
### --output-filename=FILENAME

原始参数名:
```
--output-filename=FILENAME
```
中文参数名:
```

```
原始简介:
```
Specify how the executable should be named. For extension modules there is no
choice, also not for standalone mode and using it will be an error. This may
include path information that needs to exist though. Defaults to
'<program_name>.exe' on this platform.
```
中文简介:
```

```

---
### --output-dir=DIRECTORY

原始参数名:
```
--output-dir=DIRECTORY
```
中文参数名:
```

```
原始简介:
```
Specify where intermediate and final output files should be put. The DIRECTORY
will be populated with build folder, dist folder, binaries, etc. Defaults to
current directory.
```
中文简介:
```

```

---
### --remove-output

原始参数名:
```
--remove-output
```
中文参数名:
```

```
原始简介:
```
Removes the build directory after producing the module or exe file. Defaults to
off.
```
中文简介:
```

```

---
### --no-pyi-file

原始参数名:
```
--no-pyi-file
```
中文参数名:
```

```
原始简介:
```
Do not create a '.pyi' file for extension modules created by Nuitka. This is
used to detect implicit imports. Defaults to off.
```
中文简介:
```

```

---

---
## Deployment control()

---
### --deployment

原始参数名:
```
--deployment
```
中文参数名:
```

```
原始简介:
```
Disable code aimed at making finding compatibility issues easier. This will
e.g. prevent execution with "-c" argument, which is often used by code that
attempts run a module, and causes a program to start itself over and over
potentially. Disable once you deploy to end users, for finding typical issues,
this is very helpful during development. Default off.
```
中文简介:
```

```

---
### --no-deployment-flag=FLAG

原始参数名:
```
--no-deployment-flag=FLAG
```
中文参数名:
```

```
原始简介:
```
Keep deployment mode, but disable selectively parts of it. Errors from
deployment mode will output these identifiers. Default empty.
```
中文简介:
```

```

---

---
## Environment control()

---
### --force-runtime-environment-variable=VARIABLE_SPEC

原始参数名:
```
--force-runtime-environment-variable=VARIABLE_SPEC
```
中文参数名:
```

```
原始简介:
```
Force an environment variables to a given value. Default empty.
```
中文简介:
```

```

---

---
## Debug features()

---
### --debug

原始参数名:
```
--debug
```
中文参数名:
```

```
原始简介:
```
Executing all self checks possible to find errors in Nuitka, do not use for
production. Defaults to off.
```
中文简介:
```

```

---
### --no-debug-immortal-assumptions

原始参数名:
```
--no-debug-immortal-assumptions
```
中文参数名:
```

```
原始简介:
```
Disable check normally done with "--debug". With Python3.12+ do not check known
immortal object assumptions. Some C libraries corrupt them. Defaults to check
being made if "--debug" is on.
```
中文简介:
```

```

---
### --unstripped

原始参数名:
```
--unstripped
```
中文参数名:
```

```
原始简介:
```
Keep debug info in the resulting object file for better debugger interaction.
Defaults to off.
```
中文简介:
```

```

---
### --profile

原始参数名:
```
--profile
```
中文参数名:
```

```
原始简介:
```
Enable vmprof based profiling of time spent. Not working currently. Defaults to
off.
```
中文简介:
```

```

---
### --trace-execution

原始参数名:
```
--trace-execution
```
中文参数名:
```

```
原始简介:
```
Traced execution output, output the line of code before executing it. Defaults
to off.
```
中文简介:
```

```

---
### --xml=XML_FILENAME

原始参数名:
```
--xml=XML_FILENAME
```
中文参数名:
```

```
原始简介:
```
Write the internal program structure, result of optimization in XML form to
given filename.
```
中文简介:
```

```

---
### --experimental=FLAG

原始参数名:
```
--experimental=FLAG
```
中文参数名:
```

```
原始简介:
```
Use features declared as 'experimental'. May have no effect if no experimental
features are present in the code. Uses secret tags (check source) per
experimented feature.
```
中文简介:
```

```

---
### --low-memory

原始参数名:
```
--low-memory
```
中文参数名:
```

```
原始简介:
```
Attempt to use less memory, by forking less C compilation jobs and using
options that use less memory. For use on embedded machines. Use this in case of
out of memory problems. Defaults to off.
```
中文简介:
```

```

---
### --create-environment-from-report=CREATE_ENVIRONMENT_FROM_REPORT

原始参数名:
```
--create-environment-from-report=CREATE_ENVIRONMENT_FROM_REPORT
```
中文参数名:
```

```
原始简介:
```
Create a new virtualenv in that non-existing path from the report file given
with e.g. '--report=compilation- report.xml'. Default not done.
```
中文简介:
```

```

---
### --generate-c-only

原始参数名:
```
--generate-c-only
```
中文参数名:
```

```
原始简介:
```
Generate only C source code, and do not compile it to binary or module. This is
for debugging and code coverage analysis that doesn't waste CPU. Defaults to
off. Do not think you can use this directly.
```
中文简介:
```

```

---

---
## Nuitka Development features()

---
### --devel-missing-code-helpers

原始参数名:
```
--devel-missing-code-helpers
```
中文参数名:
```

```
原始简介:
```
Report warnings for code helpers for types that were attempted, but don't
exist. This helps to identify opportunities for improving optimization of
generated code from type knowledge not used. Default False.
```
中文简介:
```

```

---
### --devel-missing-trust

原始参数名:
```
--devel-missing-trust
```
中文参数名:
```

```
原始简介:
```
Report warnings for imports that could be trusted, but currently are not. This
is to identify opportunities for improving handling of hard modules, where this
sometimes could allow more static optimization. Default False.
```
中文简介:
```

```

---
### --devel-recompile-c-only

原始参数名:
```
--devel-recompile-c-only
```
中文参数名:
```

```
原始简介:
```
This is not incremental compilation, but for Nuitka development only. Takes
existing files and simply compiles them as C again after doing the Python steps.
Allows compiling edited C files for manual debugging changes to the generated
source. Allows us to add printing, check and print values, but it is now what
users would want. Depends on compiling Python source to determine which files it
should look at.
```
中文简介:
```

```

---
### --devel-internal-graph

原始参数名:
```
--devel-internal-graph
```
中文参数名:
```

```
原始简介:
```
Create graph of optimization process internals, do not use for whole programs,
but only for small test cases. Defaults to off.
```
中文简介:
```

```

---

---
## Backend C compiler choice()

---
### --clang

原始参数名:
```
--clang
```
中文参数名:
```

```
原始简介:
```
Enforce the use of clang. On Windows this requires a working Visual Studio
version to piggy back on. Defaults to off.
```
中文简介:
```

```

---
### --mingw64

原始参数名:
```
--mingw64
```
中文参数名:
```

```
原始简介:
```
Enforce the use of MinGW64 on Windows. Defaults to off unless MSYS2 with MinGW
Python is used.
```
中文简介:
```

```

---
### --msvc=MSVC_VERSION

原始参数名:
```
--msvc=MSVC_VERSION
```
中文参数名:
```

```
原始简介:
```
Enforce the use of specific MSVC version on Windows. Allowed values are e.g.
"14.3" (MSVC 2022) and other MSVC version numbers, specify "list" for a list of
installed compilers, or use "latest".  Defaults to latest MSVC being used if
installed, otherwise MinGW64 is used.
```
中文简介:
```

```

---
### --jobs=N

原始参数名:
```
--jobs=N
```
中文参数名:
```

```
原始简介:
```
Specify the allowed number of parallel C compiler jobs. Negative values are
system CPU minus the given value. Defaults to the full system CPU count unless
low memory mode is activated, then it defaults to 1.
```
中文简介:
```

```

---
### --lto=choice

原始参数名:
```
--lto=choice
```
中文参数名:
```

```
原始简介:
```
Use link time optimizations (MSVC, gcc, clang). Allowed values are "yes", "no",
and "auto" (when it's known to work). Defaults to "auto".
```
中文简介:
```

```

---
### --static-libpython=choice

原始参数名:
```
--static-libpython=choice
```
中文参数名:
```

```
原始简介:
```
Use static link library of Python. Allowed values are "yes", "no", and "auto"
(when it's known to work). Defaults to "auto".
```
中文简介:
```

```

---
### --cf-protection=PROTECTION_MODE

原始参数名:
```
--cf-protection=PROTECTION_MODE
```
中文参数名:
```

```
原始简介:
```
This option is gcc specific. For the gcc compiler, select the "cf-protection"
mode. Default "auto" is to use the gcc default value, but you can override it,
e.g. to disable it with "none" value. Refer to gcc documentation for
"-fcf-protection" for the details.
```
中文简介:
```

```

---

---
## Cache Control()

---
### --disable-cache=DISABLED_CACHES

原始参数名:
```
--disable-cache=DISABLED_CACHES
```
中文参数名:
```

```
原始简介:
```
Disable selected caches, specify "all" for all cached. Currently allowed values
are: "all","ccache","bytecode","compression","dll- dependencies". can be given
multiple times or with comma separated values. Default none.
```
中文简介:
```

```

---
### --clean-cache=CLEAN_CACHES

原始参数名:
```
--clean-cache=CLEAN_CACHES
```
中文参数名:
```

```
原始简介:
```
Clean the given caches before executing, specify "all" for all cached.
Currently allowed values are: "all","ccache","bytecode","compression","dll-
dependencies". can be given multiple times or with comma separated values.
Default none.
```
中文简介:
```

```

---
### --force-dll-dependency-cache-update

原始参数名:
```
--force-dll-dependency-cache-update
```
中文参数名:
```

```
原始简介:
```
For an update of the dependency walker cache. Will result in much longer times
to create the distribution folder, but might be used in case the cache is
suspect to cause errors or known to need an update.
```
中文简介:
```

```

---

---
## PGO compilation choices()

---
### --pgo-c

原始参数名:
```
--pgo-c
```
中文参数名:
```

```
原始简介:
```
Enables C level profile guided optimization (PGO), by executing a dedicated
build first for a profiling run, and then using the result to feedback into the
C compilation. Note: This is experimental and not working with standalone modes
of Nuitka yet. Defaults to off.
```
中文简介:
```

```

---
### --pgo-args=PGO_ARGS

原始参数名:
```
--pgo-args=PGO_ARGS
```
中文参数名:
```

```
原始简介:
```
Arguments to be passed in case of profile guided optimization. These are passed
to the special built executable during the PGO profiling run. Default empty.
```
中文简介:
```

```

---
### --pgo-executable=PGO_EXECUTABLE

原始参数名:
```
--pgo-executable=PGO_EXECUTABLE
```
中文参数名:
```

```
原始简介:
```
Command to execute when collecting profile information. Use this only, if you
need to launch it through a script that prepares it to run. Default use created
program.
```
中文简介:
```

```

---

---
## Tracing features()

---
### --report=REPORT_FILENAME

原始参数名:
```
--report=REPORT_FILENAME
```
中文参数名:
```

```
原始简介:
```
Report module, data files, compilation, plugin, etc. details in an XML output
file. This is also super useful for issue reporting. These reports can e.g. be
used to re-create the environment easily using it with
'--create-environment-from-report', but contain a lot of information. Default is
off.
```
中文简介:
```

```

---
### --report-diffable

原始参数名:
```
--report-diffable
```
中文参数名:
```

```
原始简介:
```
Report data in diffable form, i.e. no timing or memory usage values that vary
from run to run. Default is off.
```
中文简介:
```

```

---
### --report-user-provided=KEY_VALUE

原始参数名:
```
--report-user-provided=KEY_VALUE
```
中文参数名:
```

```
原始简介:
```
Report data from you. This can be given multiple times and be anything in
'key=value' form, where key should be an identifier, e.g. use '--report-user-
provided=pipenv-lock-hash=64a5e4' to track some input values. Default is empty.
```
中文简介:
```

```

---
### --report-template=REPORT_DESC

原始参数名:
```
--report-template=REPORT_DESC
```
中文参数名:
```

```
原始简介:
```
Report via template. Provide template and output filename
'template.rst.j2:output.rst'. For built-in templates, check the User Manual for
what these are. Can be given multiple times. Default is empty.
```
中文简介:
```

```

---
### --quiet

原始参数名:
```
--quiet
```
中文参数名:
```

```
原始简介:
```
Disable all information outputs, but show warnings. Defaults to off.
```
中文简介:
```

```

---
### --show-scons

原始参数名:
```
--show-scons
```
中文参数名:
```

```
原始简介:
```
Run the C building backend Scons with verbose information, showing the executed
commands, detected compilers. Defaults to off.
```
中文简介:
```

```

---
### --no-progressbar

原始参数名:
```
--no-progressbar
```
中文参数名:
```

```
原始简介:
```
Disable progress bars. Defaults to off.
```
中文简介:
```

```

---
### --show-progress

原始参数名:
```
--show-progress
```
中文参数名:
```

```
原始简介:
```
Obsolete: Provide progress information and statistics. Disables normal progress
bar. Defaults to off.
```
中文简介:
```

```

---
### --show-memory

原始参数名:
```
--show-memory
```
中文参数名:
```

```
原始简介:
```
Provide memory information and statistics. Defaults to off.
```
中文简介:
```

```

---
### --show-modules

原始参数名:
```
--show-modules
```
中文参数名:
```

```
原始简介:
```
Provide information for included modules and DLLs Obsolete: You should use
'--report' file instead. Defaults to off.
```
中文简介:
```

```

---
### --show-modules-output=PATH

原始参数名:
```
--show-modules-output=PATH
```
中文参数名:
```

```
原始简介:
```
Where to output '--show-modules', should be a filename. Default is standard
output.
```
中文简介:
```

```

---
### --verbose

原始参数名:
```
--verbose
```
中文参数名:
```

```
原始简介:
```
Output details of actions taken, esp. in optimizations. Can become a lot.
Defaults to off.
```
中文简介:
```

```

---
### --verbose-output=PATH

原始参数名:
```
--verbose-output=PATH
```
中文参数名:
```

```
原始简介:
```
Where to output from '--verbose', should be a filename. Default is standard
output.
```
中文简介:
```

```

---

---
## General OS controls()

---
### --force-stdout-spec=FORCE_STDOUT_SPEC

原始参数名:
```
--force-stdout-spec=FORCE_STDOUT_SPEC
```
中文参数名:
```

```
原始简介:
```
Force standard output of the program to go to this location. Useful for
programs with disabled console and programs using the Windows Services Plugin of
Nuitka commercial. Defaults to not active, use e.g. '{PROGRAM_BASE}.out.txt',
i.e. file near your program, check User Manual for full list of available
values.
```
中文简介:
```

```

---
### --force-stderr-spec=FORCE_STDERR_SPEC

原始参数名:
```
--force-stderr-spec=FORCE_STDERR_SPEC
```
中文参数名:
```

```
原始简介:
```
Force standard error of the program to go to this location. Useful for programs
with disabled console and programs using the Windows Services Plugin of Nuitka
commercial. Defaults to not active, use e.g. '{PROGRAM_BASE}.err.txt', i.e. file
near your program, check User Manual for full list of available values.
```
中文简介:
```

```

---

---
## Windows specific controls()

---
### --windows-console-mode=CONSOLE_MODE

原始参数名:
```
--windows-console-mode=CONSOLE_MODE
```
中文参数名:
```

```
原始简介:
```
Select console mode to use. Default mode is 'force' and creates a console
window unless the program was started from one. With 'disable' it doesn't create
or use a console at all. With 'attach' an existing console will be used for
outputs. With 'hide' a newly spawned console will be hidden and an already
existing console will behave like 'force'. Default is 'force'.
```
中文简介:
```

```

---
### --windows-icon-from-ico=ICON_PATH

原始参数名:
```
--windows-icon-from-ico=ICON_PATH
```
中文参数名:
```

```
原始简介:
```
Add executable icon. Can be given multiple times for different resolutions or
files with multiple icons inside. In the later case, you may also suffix with
#<n> where n is an integer index starting from 1, specifying a specific icon to
be included, and all others to be ignored.
```
中文简介:
```

```

---
### --windows-icon-from-exe=ICON_EXE_PATH

原始参数名:
```
--windows-icon-from-exe=ICON_EXE_PATH
```
中文参数名:
```

```
原始简介:
```
Copy executable icons from this existing executable (Windows only).
```
中文简介:
```

```

---
### --onefile-windows-splash-screen-image=SPLASH_SCREEN_IMAGE

原始参数名:
```
--onefile-windows-splash-screen-image=SPLASH_SCREEN_IMAGE
```
中文参数名:
```

```
原始简介:
```
When compiling for Windows and onefile, show this while loading the
application. Defaults to off.
```
中文简介:
```

```

---
### --windows-uac-admin

原始参数名:
```
--windows-uac-admin
```
中文参数名:
```

```
原始简介:
```
Request Windows User Control, to grant admin rights on execution. (Windows
only). Defaults to off.
```
中文简介:
```

```

---
### --windows-uac-uiaccess

原始参数名:
```
--windows-uac-uiaccess
```
中文参数名:
```

```
原始简介:
```
Request Windows User Control, to enforce running from a few folders only,
remote desktop access. (Windows only). Defaults to off.
```
中文简介:
```

```

---

---
## macOS specific controls()

---
### --macos-create-app-bundle

原始参数名:
```
--macos-create-app-bundle
```
中文参数名:
```

```
原始简介:
```
When compiling for macOS, create a bundle rather than a plain binary
application. This is the only way to unlock the disabling of console, get high
DPI graphics, etc. and implies standalone mode. Defaults to off.
```
中文简介:
```

```

---
### --macos-target-arch=MACOS_TARGET_ARCH

原始参数名:
```
--macos-target-arch=MACOS_TARGET_ARCH
```
中文参数名:
```

```
原始简介:
```
What architectures is this to supposed to run on. Default and limit is what the
running Python allows for. Default is "native" which is the architecture the
Python is run with.
```
中文简介:
```

```

---
### --macos-app-icon=ICON_PATH

原始参数名:
```
--macos-app-icon=ICON_PATH
```
中文参数名:
```

```
原始简介:
```
Add icon for the application bundle to use. Can be given only one time.
Defaults to Python icon if available.
```
中文简介:
```

```

---
### --macos-signed-app-name=MACOS_SIGNED_APP_NAME

原始参数名:
```
--macos-signed-app-name=MACOS_SIGNED_APP_NAME
```
中文参数名:
```

```
原始简介:
```
Name of the application to use for macOS signing. Follow
"com.YourCompany.AppName" naming results for best results, as these have to be
globally unique, and will potentially grant protected API accesses.
```
中文简介:
```

```

---
### --macos-app-name=MACOS_APP_NAME

原始参数名:
```
--macos-app-name=MACOS_APP_NAME
```
中文参数名:
```

```
原始简介:
```
Name of the product to use in macOS bundle information. Defaults to base
filename of the binary.
```
中文简介:
```

```

---
### --macos-app-mode=MODE

原始参数名:
```
--macos-app-mode=MODE
```
中文参数名:
```

```
原始简介:
```
Mode of application for the application bundle. When launching a Window, and
appearing in Docker is desired, default value "gui" is a good fit. Without a
Window ever, the application is a "background" application. For UI elements that
get to display later, "ui-element" is in-between. The application will not
appear in dock, but get full access to desktop when it does open a Window later.
```
中文简介:
```

```

---
### --macos-sign-identity=MACOS_APP_VERSION

原始参数名:
```
--macos-sign-identity=MACOS_APP_VERSION
```
中文参数名:
```

```
原始简介:
```
When signing on macOS, by default an ad-hoc identify will be used, but with
this option your get to specify another identity to use. The signing of code is
now mandatory on macOS and cannot be disabled. Use "auto" to detect your only
identity installed. Default "ad- hoc" if not given.
```
中文简介:
```

```

---
### --macos-sign-notarization

原始参数名:
```
--macos-sign-notarization
```
中文参数名:
```

```
原始简介:
```
When signing for notarization, using a proper TeamID identity from Apple, use
the required runtime signing option, such that it can be accepted.
```
中文简介:
```

```

---
### --macos-app-version=MACOS_APP_VERSION

原始参数名:
```
--macos-app-version=MACOS_APP_VERSION
```
中文参数名:
```

```
原始简介:
```
Product version to use in macOS bundle information. Defaults to "1.0" if not
given.
```
中文简介:
```

```

---
### --macos-app-protected-resource=RESOURCE_DESC

原始参数名:
```
--macos-app-protected-resource=RESOURCE_DESC
```
中文参数名:
```

```
原始简介:
```
Request an entitlement for access to a macOS protected resources, e.g.
"NSMicrophoneUsageDescription:Microphone access for recording audio." requests
access to the microphone and provides an informative text for the user, why that
is needed. Before the colon, is an OS identifier for an access right, then the
informative text. Legal values can be found on https://developer.apple.com/doc
umentation/bundleresources/information_property_list/p rotected_resources and
the option can be specified multiple times. Default empty.
```
中文简介:
```

```

---

---
## Linux specific controls()

---
### --linux-icon=ICON_PATH

原始参数名:
```
--linux-icon=ICON_PATH
```
中文参数名:
```

```
原始简介:
```
Add executable icon for onefile binary to use. Can be given only one time.
Defaults to Python icon if available.
```
中文简介:
```

```

---

---
## Binary Version Information()

---
### --company-name=COMPANY_NAME

原始参数名:
```
--company-name=COMPANY_NAME
```
中文参数名:
```

```
原始简介:
```
Name of the company to use in version information. Defaults to unused.
```
中文简介:
```

```

---
### --product-name=PRODUCT_NAME

原始参数名:
```
--product-name=PRODUCT_NAME
```
中文参数名:
```

```
原始简介:
```
Name of the product to use in version information. Defaults to base filename of
the binary.
```
中文简介:
```

```

---
### --file-version=FILE_VERSION

原始参数名:
```
--file-version=FILE_VERSION
```
中文参数名:
```

```
原始简介:
```
File version to use in version information. Must be a sequence of up to 4
numbers, e.g. 1.0 or 1.0.0.0, no more digits are allowed, no strings are
allowed. Defaults to unused.
```
中文简介:
```

```

---
### --product-version=PRODUCT_VERSION

原始参数名:
```
--product-version=PRODUCT_VERSION
```
中文参数名:
```

```
原始简介:
```
Product version to use in version information. Same rules as for file version.
Defaults to unused.
```
中文简介:
```

```

---
### --file-description=FILE_DESCRIPTION

原始参数名:
```
--file-description=FILE_DESCRIPTION
```
中文参数名:
```

```
原始简介:
```
Description of the file used in version information. Windows only at this time.
Defaults to binary filename.
```
中文简介:
```

```

---
### --copyright=COPYRIGHT_TEXT

原始参数名:
```
--copyright=COPYRIGHT_TEXT
```
中文参数名:
```

```
原始简介:
```
Copyright used in version information. Windows/macOS only at this time.
Defaults to not present.
```
中文简介:
```

```

---
### --trademarks=TRADEMARK_TEXT

原始参数名:
```
--trademarks=TRADEMARK_TEXT
```
中文参数名:
```

```
原始简介:
```
Trademark used in version information. Windows/macOS only at this time.
Defaults to not present.
```
中文简介:
```

```

---

---
## Plugin control()

---
### --enable-plugins=PLUGIN_NAME

原始参数名:
```
--enable-plugins=PLUGIN_NAME
```
中文参数名:
```

```
原始简介:
```
Enabled plugins. Must be plug-in names. Use '--plugin- list' to query the full
list and exit. Default empty.
```
中文简介:
```

```

---
### --disable-plugins=PLUGIN_NAME

原始参数名:
```
--disable-plugins=PLUGIN_NAME
```
中文参数名:
```

```
原始简介:
```
Disabled plugins. Must be plug-in names. Use '-- plugin-list' to query the full
list and exit. Most standard plugins are not a good idea to disable. Default
empty.
```
中文简介:
```

```

---
### --user-plugin=PATH

原始参数名:
```
--user-plugin=PATH
```
中文参数名:
```

```
原始简介:
```
The file name of user plugin. Can be given multiple times. Default empty.
```
中文简介:
```

```

---
### --plugin-list

原始参数名:
```
--plugin-list
```
中文参数名:
```

```
原始简介:
```
Show list of all available plugins and exit. Defaults to off.
```
中文简介:
```

```

---
### --plugin-no-detection

原始参数名:
```
--plugin-no-detection
```
中文参数名:
```

```
原始简介:
```
Plugins can detect if they might be used, and the you can disable the warning
via "--disable-plugin=plugin- that-warned", or you can use this option to
disable the mechanism entirely, which also speeds up compilation slightly of
course as this detection code is run in vain once you are certain of which
plugins to use. Defaults to off.
```
中文简介:
```

```

---
### --module-parameter=MODULE_PARAMETERS

原始参数名:
```
--module-parameter=MODULE_PARAMETERS
```
中文参数名:
```

```
原始简介:
```
Provide a module parameter. You are asked by some packages to provide extra
decisions. Format is currently --module-parameter=module.name-option- name=value
Default empty.
```
中文简介:
```

```

---
### --show-source-changes=SHOW_SOURCE_CHANGES

原始参数名:
```
--show-source-changes=SHOW_SOURCE_CHANGES
```
中文参数名:
```

```
原始简介:
```
Show source changes to original Python file content before compilation. Mostly
intended for developing plugins and Nuitka package configuration. Use e.g. '--
show-source-changes=numpy.**' to see all changes below a given namespace or use
'*' to see everything which can get a lot. Default empty.
```
中文简介:
```

```

---

---
## Cross compilation()

---
### --target=TARGET_DESC

原始参数名:
```
--target=TARGET_DESC
```
中文参数名:
```

```
原始简介:
```
Cross compilation target. Highly experimental and in development, not supposed
to work yet. We are working on '--target=wasi' and nothing else yet.
```
中文简介:
```

```

---

---
## Plugin options of 'anti-bloat'()

---
### --show-anti-bloat-changes

原始参数名:
```
--show-anti-bloat-changes
```
中文参数名:
```

```
原始简介:
```
Annotate what changes are done by the plugin.
```
中文简介:
```

```

---
### --noinclude-setuptools-mode=NOINCLUDE_SETUPTOOLS_MODE

原始参数名:
```
--noinclude-setuptools-mode=NOINCLUDE_SETUPTOOLS_MODE
```
中文参数名:
```

```
原始简介:
```
What to do if a 'setuptools' or import is encountered. This package can be big
with dependencies, and should definitely be avoided. Also handles
'setuptools_scm'.
```
中文简介:
```

```

---
### --noinclude-pytest-mode=NOINCLUDE_PYTEST_MODE

原始参数名:
```
--noinclude-pytest-mode=NOINCLUDE_PYTEST_MODE
```
中文参数名:
```

```
原始简介:
```
What to do if a 'pytest' import is encountered. This package can be big with
dependencies, and should definitely be avoided. Also handles 'nose' imports.
```
中文简介:
```

```

---
### --noinclude-unittest-mode=NOINCLUDE_UNITTEST_MODE

原始参数名:
```
--noinclude-unittest-mode=NOINCLUDE_UNITTEST_MODE
```
中文参数名:
```

```
原始简介:
```
What to do if a unittest import is encountered. This package can be big with
dependencies, and should definitely be avoided.
```
中文简介:
```

```

---
### --noinclude-pydoc-mode=NOINCLUDE_PYDOC_MODE

原始参数名:
```
--noinclude-pydoc-mode=NOINCLUDE_PYDOC_MODE
```
中文参数名:
```

```
原始简介:
```
What to do if a pydoc import is encountered. This package use is mark of
useless code for deployments and should be avoided.
```
中文简介:
```

```

---
### --noinclude-IPython-mode=NOINCLUDE_IPYTHON_MODE

原始参数名:
```
--noinclude-IPython-mode=NOINCLUDE_IPYTHON_MODE
```
中文参数名:
```

```
原始简介:
```
What to do if a IPython import is encountered. This package can be big with
dependencies, and should definitely be avoided.
```
中文简介:
```

```

---
### --noinclude-dask-mode=NOINCLUDE_DASK_MODE

原始参数名:
```
--noinclude-dask-mode=NOINCLUDE_DASK_MODE
```
中文参数名:
```

```
原始简介:
```
What to do if a 'dask' import is encountered. This package can be big with
dependencies, and should definitely be avoided.
```
中文简介:
```

```

---
### --noinclude-numba-mode=NOINCLUDE_NUMBA_MODE

原始参数名:
```
--noinclude-numba-mode=NOINCLUDE_NUMBA_MODE
```
中文参数名:
```

```
原始简介:
```
What to do if a 'numba' import is encountered. This package can be big with
dependencies, and is currently not working for standalone. This package is big
with dependencies, and should definitely be avoided.
```
中文简介:
```

```

---
### --noinclude-default-mode=NOINCLUDE_DEFAULT_MODE

原始参数名:
```
--noinclude-default-mode=NOINCLUDE_DEFAULT_MODE
```
中文参数名:
```

```
原始简介:
```
This actually provides the default "warning" value for above options, and can
be used to turn all of these on.
```
中文简介:
```

```

---
### --noinclude-custom-mode=CUSTOM_CHOICES

原始参数名:
```
--noinclude-custom-mode=CUSTOM_CHOICES
```
中文参数名:
```

```
原始简介:
```
What to do if a specific import is encountered. Format is module name, which
can and should be a top level package and then one choice, "error", "warning",
"nofollow", e.g. PyQt5:error.
```
中文简介:
```

```

---

---
## Plugin options of 'playwright'()

---
### --playwright-include-browser=INCLUDE_BROWSERS

原始参数名:
```
--playwright-include-browser=INCLUDE_BROWSERS
```
中文参数名:
```

```
原始简介:
```
Playwright browser to include. Can be specified multiple times. use "all" to
include all installed browsers.
```
中文简介:
```

```

---

---
## Plugin options of 'spacy'()

---
### --spacy-language-model=INCLUDE_LANGUAGE_MODELS

原始参数名:
```
--spacy-language-model=INCLUDE_LANGUAGE_MODELS
```
中文参数名:
```

```
原始简介:
```
Spacy language models to use. Can be specified multiple times. Use 'all' to
include all downloaded models.
```
中文简介:
```

```

---

---
