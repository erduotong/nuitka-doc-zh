# Nuitka --help文档翻译

> 返回[导航](../README.md#导航)

## 信息

该文档目前Nuitka版本: `Nuitka 1.8.1`
<details>
<summary>模板</summary>

````markdown
### --help

原始参数名: `--help`    
中文参数名: `帮助`   
原始简介:

```
show this help message and exit
```

中文简介:

```
显示此帮助消息并退出
```

---

````

</details>


<details>
<summary>源文本</summary>

```
Options:
  --help                show this help message and exit
  --version             Show version information and important details for bug
                        reports, then exit. Defaults to off.
  --module              Create an extension module executable instead of a
                        program. Defaults to off.
  --standalone          Enable standalone mode for output. This allows you to
                        transfer the created binary to other machines without
                        it using an existing Python installation. This also
                        means it will become big. It implies these option: "--
                        follow-imports" and "--python-flag=no_site". Defaults
                        to off.
  --onefile             On top of standalone mode, enable onefile mode. This
                        means not a folder, but a compressed executable is
                        created and used. Defaults to off.
  --python-debug        Use debug version or not. Default uses what you are
                        using to run Nuitka, most likely a non-debug version.
  --python-flag=FLAG    Python flags to use. Default is what you are using to
                        run Nuitka, this enforces a specific mode. These are
                        options that also exist to standard Python executable.
                        Currently supported: "-S" (alias "no_site"),
                        "static_hashes" (do not use hash randomization),
                        "no_warnings" (do not give Python run time warnings),
                        "-O" (alias "no_asserts"), "no_docstrings" (do not use
                        doc strings), "-u" (alias "unbuffered"), "isolated"
                        (do not load outside code) and "-m" (package mode,
                        compile as "package.__main__"). Default empty.
  --python-for-scons=PATH
                        If using Python3.3 or Python3.4, provide the path of a
                        Python binary to use for Scons. Otherwise Nuitka can
                        use what you run Nuitka with or a Python installation
                        from Windows registry. On Windows Python 3.5 or higher
                        is needed. On non-Windows, Python 2.6 or 2.7 will do
                        as well.
  --main=PATH           If specified once, this takes the place of the
                        positional argument, i.e. the filename to compile.
                        When given multiple times, it enables "multidist" (see
                        User Manual) it allows you to create binaries that
                        depending on file name or invocation name.

  Control the inclusion of modules and packages in result:
    --include-package=PACKAGE
                        Include a whole package. Give as a Python namespace,
                        e.g. "some_package.sub_package" and Nuitka will then
                        find it and include it and all the modules found below
                        that disk location in the binary or extension module
                        it creates, and make it available for import by the
                        code. To avoid unwanted sub packages, e.g. tests you
                        can e.g. do this "--nofollow-import-to=*.tests".
                        Default empty.
    --include-module=MODULE
                        Include a single module. Give as a Python namespace,
                        e.g. "some_package.some_module" and Nuitka will then
                        find it and include it in the binary or extension
                        module it creates, and make it available for import by
                        the code. Default empty.
    --include-plugin-directory=MODULE/PACKAGE
                        Include also the code found in that directory,
                        considering as if they are each given as a main file.
                        Overrides all other inclusion options. You ought to
                        prefer other inclusion options, that go by names,
                        rather than filenames, those find things through being
                        in "sys.path". This option is for very special use
                        cases only. Can be given multiple times. Default
                        empty.
    --include-plugin-files=PATTERN
                        Include into files matching the PATTERN. Overrides all
                        other follow options. Can be given multiple times.
                        Default empty.
    --prefer-source-code
                        For already compiled extension modules, where there is
                        both a source file and an extension module, normally
                        the extension module is used, but it should be better
                        to compile the module from available source code for
                        best performance. If not desired, there is --no-
                        prefer-source-code to disable warnings about it.
                        Default off.

  Control the following into imported modules:
    --follow-imports    Descend into all imported modules. Defaults to on in
                        standalone mode, otherwise off.
    --follow-import-to=MODULE/PACKAGE
                        Follow to that module if used, or if a package, to the
                        whole package. Can be given multiple times. Default
                        empty.
    --nofollow-import-to=MODULE/PACKAGE
                        Do not follow to that module name even if used, or if
                        a package name, to the whole package in any case,
                        overrides all other options. Can be given multiple
                        times. Default empty.
    --nofollow-imports  Do not descend into any imported modules at all,
                        overrides all other inclusion options and not usable
                        for standalone mode. Defaults to off.
    --follow-stdlib     Also descend into imported modules from standard
                        library. This will increase the compilation time by a
                        lot and is also not well tested at this time and
                        sometimes won't work. Defaults to off.

  Onefile options:
    --onefile-tempdir-spec=ONEFILE_TEMPDIR_SPEC
                        Use this as a folder to unpack to in onefile mode.
                        Defaults to '%TEMP%/onefile_%PID%_%TIME%', i.e. user
                        temporary directory and being non-static it's removed.
                        Use e.g. a string like
                        '%CACHE_DIR%/%COMPANY%/%PRODUCT%/%VERSION%' which is a
                        good static cache path, this will then not be removed.
    --onefile-child-grace-time=GRACE_TIME_MS
                        When stopping the child, e.g. due to CTRL-C or
                        shutdown, etc. the Python code gets a
                        "KeyboardInterrupt", that it may handle e.g. to flush
                        data. This is the amount of time in ms, before the
                        child it killed in the hard way. Unit is ms, and
                        default 5000.
    --onefile-no-compression
                        When creating the onefile, disable compression of the
                        payload. This is mostly for debug purposes, or to save
                        time. Default is off.

  Data files:
    --include-package-data=PACKAGE
                        Include data files for the given package name. DLLs
                        and extension modules are not data files and never
                        included like this. Can use patterns the filenames as
                        indicated below. Data files of packages are not
                        included by default, but package configuration can do
                        it. This will only include non-DLL, non-extension
                        modules, i.e. actual data files. After a ":"
                        optionally a filename pattern can be given as well,
                        selecting only matching files. Examples: "--include-
                        package-data=package_name" (all files) "--include-
                        package-data=package_name=*.txt" (only certain type) "
                        --include-package-data=package_name=some_filename.dat
                        (concrete file) Default empty.
    --include-data-files=DESC
                        Include data files by filenames in the distribution.
                        There are many allowed forms. With '--include-data-
                        files=/path/to/file/*.txt=folder_name/some.txt' it
                        will copy a single file and complain if it's multiple.
                        With '--include-data-
                        files=/path/to/files/*.txt=folder_name/' it will put
                        all matching files into that folder. For recursive
                        copy there is a form with 3 values that '--include-
                        data-files=/path/to/scan=folder_name=**/*.txt' that
                        will preserve directory structure. Default empty.
    --include-data-dir=DIRECTORY
                        Include data files from complete directory in the
                        distribution. This is recursive. Check '--include-
                        data-files' with patterns if you want non-recursive
                        inclusion. An example would be '--include-data-
                        dir=/path/some_dir=data/some_dir' for plain copy, of
                        the whole directory. All files are copied, if you want
                        to exclude files you need to remove them beforehand,
                        or use '--noinclude-data-files' option to remove them.
                        Default empty.
    --noinclude-data-files=PATTERN
                        Do not include data files matching the filename
                        pattern given. This is against the target filename,
                        not source paths. So to ignore a file pattern from
                        package data for "package_name" should be matched as
                        "package_name/*.txt". Or for the whole directory
                        simply use "package_name". Default empty.
    --list-package-data=LIST_PACKAGE_DATA
                        Output the data files found for a given package name.
                        Default not done.

  Metadata support:
    --include-distribution-metadata=DISTRIBUTION
                        Include metadata information for the given
                        distribution name. Some packages check metadata for
                        presence, version, entry points, etc. and without this
                        option given, it only works when it's recognized at
                        compile time which is not always happening. This of
                        course only makes sense for packages that are included
                        in the compilation. Default empty.

  DLL files:
    --noinclude-dlls=PATTERN
                        Do not include DLL files matching the filename pattern
                        given. This is against the target filename, not source
                        paths. So ignore a DLL "someDLL" contained in the
                        package "package_name" it should be matched as
                        "package_name/someDLL.*". Default empty.
    --list-package-dlls=LIST_PACKAGE_DLLS
                        Output the DLLs found for a given package name.
                        Default not done.

  Control the warnings to be given by Nuitka:
    --warn-implicit-exceptions
                        Enable warnings for implicit exceptions detected at
                        compile time.
    --warn-unusual-code
                        Enable warnings for unusual code detected at compile
                        time.
    --assume-yes-for-downloads
                        Allow Nuitka to download external code if necessary,
                        e.g. dependency walker, ccache, and even gcc on
                        Windows. To disable, redirect input from nul device,
                        e.g. "</dev/null" or "<NUL:". Default is to prompt.
    --nowarn-mnemonic=MNEMONIC
                        Disable warning for a given mnemonic. These are given
                        to make sure you are aware of certain topics, and
                        typically point to the Nuitka website. The mnemonic is
                        the part of the URL at the end, without the HTML
                        suffix. Can be given multiple times and accepts shell
                        pattern. Default empty.

  Immediate execution after compilation:
    --run               Execute immediately the created binary (or import the
                        compiled module). Defaults to off.
    --debugger          Execute inside a debugger, e.g. "gdb" or "lldb" to
                        automatically get a stack trace. Defaults to off.
    --execute-with-pythonpath
                        When immediately executing the created binary or
                        module using '--run', don't reset 'PYTHONPATH'
                        environment. When all modules are successfully
                        included, you ought to not need PYTHONPATH anymore,
                        and definitely not for standalone mode.

  Compilation choices:
    --user-package-configuration-file=YAML_FILENAME
                        User provided Yaml file with package configuration.
                        You can include DLLs, remove bloat, add hidden
                        dependencies. Check User Manual for a complete
                        description of the format to use. Can be given
                        multiple times. Defaults to empty.
    --full-compat       Enforce absolute compatibility with CPython. Do not
                        even allow minor deviations from CPython behavior,
                        e.g. not having better tracebacks or exception
                        messages which are not really incompatible, but only
                        different or worse. This is intended for tests only
                        and should *not* be used.
    --file-reference-choice=MODE
                        Select what value "__file__" is going to be. With
                        "runtime" (default for standalone binary mode and
                        module mode), the created binaries and modules, use
                        the location of themselves to deduct the value of
                        "__file__". Included packages pretend to be in
                        directories below that location. This allows you to
                        include data files in deployments. If you merely seek
                        acceleration, it's better for you to use the
                        "original" value, where the source files location will
                        be used. With "frozen" a notation "<frozen
                        module_name>" is used. For compatibility reasons, the
                        "__file__" value will always have ".py" suffix
                        independent of what it really is.
    --module-name-choice=MODE
                        Select what value "__name__" and "__package__" are
                        going to be. With "runtime" (default for module mode),
                        the created module uses the parent package to deduce
                        the value of "__package__", to be fully compatible.
                        The value "original" (default for other modes) allows
                        for more static optimization to happen, but is
                        incompatible for modules that normally can be loaded
                        into any package.

  Output choices:
    --output-filename=FILENAME
                        Specify how the executable should be named. For
                        extension modules there is no choice, also not for
                        standalone mode and using it will be an error. This
                        may include path information that needs to exist
                        though. Defaults to '<program_name>' on this platform.
                        .exe
    --output-dir=DIRECTORY
                        Specify where intermediate and final output files
                        should be put. The DIRECTORY will be populated with
                        build folder, dist folder, binaries, etc. Defaults to
                        current directory.
    --remove-output     Removes the build directory after producing the module
                        or exe file. Defaults to off.
    --no-pyi-file       Do not create a ".pyi" file for extension modules
                        created by Nuitka. This is used to detect implicit
                        imports. Defaults to off.

  Debug features:
    --debug             Executing all self checks possible to find errors in
                        Nuitka, do not use for production. Defaults to off.
    --unstripped        Keep debug info in the resulting object file for
                        better debugger interaction. Defaults to off.
    --profile           Enable vmprof based profiling of time spent. Not
                        working currently. Defaults to off.
    --internal-graph    Create graph of optimization process internals, do not
                        use for whole programs, but only for small test cases.
                        Defaults to off.
    --trace-execution   Traced execution output, output the line of code
                        before executing it. Defaults to off.
    --recompile-c-only  This is not incremental compilation, but for Nuitka
                        development only. Takes existing files and simply
                        compile them as C again. Allows compiling edited C
                        files for quick debugging changes to the generated
                        source, e.g. to see if code is passed by, values
                        output, etc, Defaults to off. Depends on compiling
                        Python source to determine which files it should look
                        at.
    --xml=XML_FILENAME  Write the internal program structure, result of
                        optimization in XML form to given filename.
    --deployment        Disable code aimed at making finding compatibility
                        issues easier. This will e.g. prevent execution with
                        "-c" argument, which is often used by code that
                        attempts run a module, and causes a program to start
                        itself over and over potentially. Default off.
    --no-deployment-flag=FLAG
                        Keep deployment mode, but disable selectively parts of
                        it. Errors from deployment mode will output these
                        identifiers. Default empty.
    --experimental=FLAG
                        Use features declared as 'experimental'. May have no
                        effect if no experimental features are present in the
                        code. Uses secret tags (check source) per experimented
                        feature.
    --low-memory        Attempt to use less memory, by forking less C
                        compilation jobs and using options that use less
                        memory. For use on embedded machines. Use this in case
                        of out of memory problems. Defaults to off.
    --create-environment-from-report=CREATE_ENVIRONMENT_FROM_REPORT
                        Create a new virtualenv in that non-existing path from
                        the report file given with e.g. '--report=compilation-
                        report.xml'. Default not done.
    --generate-c-only   Generate only C source code, and do not compile it to
                        binary or module. This is for debugging and code
                        coverage analysis that doesn't waste CPU. Defaults to
                        off. Do not think you can use this directly.

  Backend C compiler choice:
    --clang             Enforce the use of clang. On Windows this requires a
                        working Visual Studio version to piggy back on.
                        Defaults to off.
    --mingw64           Enforce the use of MinGW64 on Windows. Defaults to off
                        unless MSYS2 with MinGW Python is used.
    --msvc=MSVC_VERSION
                        Enforce the use of specific MSVC version on Windows.
                        Allowed values are e.g. "14.3" (MSVC 2022) and other
                        MSVC version numbers, specify "list" for a list of
                        installed compilers, or use "latest".  Defaults to
                        latest MSVC being used if installed, otherwise MinGW64
                        is used.
    --jobs=N            Specify the allowed number of parallel C compiler
                        jobs. Defaults to the system CPU count.
    --lto=choice        Use link time optimizations (MSVC, gcc, clang).
                        Allowed values are "yes", "no", and "auto" (when it's
                        known to work). Defaults to "auto".
    --static-libpython=choice
                        Use static link library of Python. Allowed values are
                        "yes", "no", and "auto" (when it's known to work).
                        Defaults to "auto".

  Cache Control:
    --disable-cache=DISABLED_CACHES
                        Disable selected caches, specify "all" for all cached.
                        Currently allowed values are:
                        "all","ccache","bytecode","dll-dependencies". can be
                        given multiple times or with comma separated values.
                        Default none.
    --clean-cache=CLEAN_CACHES
                        Clean the given caches before executing, specify "all"
                        for all cached. Currently allowed values are:
                        "all","ccache","bytecode","dll-dependencies". can be
                        given multiple times or with comma separated values.
                        Default none.
    --disable-bytecode-cache
                        Do not reuse dependency analysis results for modules,
                        esp. from standard library, that are included as
                        bytecode. Same as --disable-cache=bytecode.
    --disable-ccache    Do not attempt to use ccache (gcc, clang, etc.) or
                        clcache (MSVC, clangcl). Same as --disable-
                        cache=ccache.
    --disable-dll-dependency-cache
                        Disable the dependency walker cache. Will result in
                        much longer times to create the distribution folder,
                        but might be used in case the cache is suspect to
                        cause errors. Same as --disable-cache=dll-
                        dependencies.
    --force-dll-dependency-cache-update
                        For an update of the dependency walker cache. Will
                        result in much longer times to create the distribution
                        folder, but might be used in case the cache is suspect
                        to cause errors or known to need an update.

  PGO compilation choices:
    --pgo               Enables C level profile guided optimization (PGO), by
                        executing a dedicated build first for a profiling run,
                        and then using the result to feedback into the C
                        compilation. Note: This is experimental and not
                        working with standalone modes of Nuitka yet. Defaults
                        to off.
    --pgo-args=PGO_ARGS
                        Arguments to be passed in case of profile guided
                        optimization. These are passed to the special built
                        executable during the PGO profiling run. Default
                        empty.
    --pgo-executable=PGO_EXECUTABLE
                        Command to execute when collecting profile
                        information. Use this only, if you need to launch it
                        through a script that prepares it to run. Default use
                        created program.

  Tracing features:
    --report=REPORT_FILENAME
                        Report module, data files, compilation, plugin, etc.
                        details in an XML output file. This is also super
                        useful for issue reporting. These reports can e.g. be
                        used to re-create the environment easily using it with
                        '--create-environment-from-report', but contain a lot
                        of information. Default is off.
    --report-diffable   Report data in diffable form, i.e. no timing or memory
                        usage values that vary from run to run. Default is
                        off.
    --report-user-provided=KEY_VALUE
                        Report data from you. This can be given multiple times
                        and be anything in 'key=value' form, where key should
                        be an identifier, e.g. use '--report-user-
                        provided=pipenv-lock-hash=64a5e4' to track some input
                        values. Default is empty.
    --report-template=REPORT_DESC
                        Report via template. Provide template and output
                        filename "template.rst.j2:output.rst". For built-in
                        templates, check the User Manual for what these are.
                        Can be given multiple times. Default is empty.
    --quiet             Disable all information outputs, but show warnings.
                        Defaults to off.
    --show-scons        Run the C building backend Scons with verbose
                        information, showing the executed commands, detected
                        compilers. Defaults to off.
    --no-progressbar    Disable progress bars. Defaults to off.
    --show-progress     Obsolete: Provide progress information and statistics.
                        Disables normal progress bar. Defaults to off.
    --show-memory       Provide memory information and statistics. Defaults to
                        off.
    --show-modules      Provide information for included modules and DLLs
                        Obsolete: You should use '--report' file instead.
                        Defaults to off.
    --show-modules-output=PATH
                        Where to output '--show-modules', should be a
                        filename. Default is standard output.
    --verbose           Output details of actions taken, esp. in
                        optimizations. Can become a lot. Defaults to off.
    --verbose-output=PATH
                        Where to output from '--verbose', should be a
                        filename. Default is standard output.

  General OS controls:
    --disable-console   When compiling for Windows or macOS, disable the
                        console window and create a GUI application. Defaults
                        to off.
    --enable-console    When compiling for Windows or macOS, enable the
                        console window and create a console application. This
                        disables hints from certain modules, e.g. "PySide"
                        that suggest to disable it. Defaults to true.
    --force-stdout-spec=FORCE_STDOUT_SPEC
                        Force standard output of the program to go to this
                        location. Useful for programs with disabled console
                        and programs using the Windows Services Plugin of
                        Nuitka commercial. Defaults to not active, use e.g.
                        '%PROGRAM_BASE%.out.txt', i.e. file near your program,
                        check User Manual for full list of available values.
    --force-stderr-spec=FORCE_STDERR_SPEC
                        Force standard error of the program to go to this
                        location. Useful for programs with disabled console
                        and programs using the Windows Services Plugin of
                        Nuitka commercial. Defaults to not active, use e.g.
                        '%PROGRAM_BASE%.err.txt', i.e. file near your program,
                        check User Manual for full list of available values.

  Windows specific controls:
    --windows-icon-from-ico=ICON_PATH
                        Add executable icon. Can be given multiple times for
                        different resolutions or files with multiple icons
                        inside. In the later case, you may also suffix with
                        #<n> where n is an integer index starting from 1,
                        specifying a specific icon to be included, and all
                        others to be ignored.
    --windows-icon-from-exe=ICON_EXE_PATH
                        Copy executable icons from this existing executable
                        (Windows only).
    --onefile-windows-splash-screen-image=SPLASH_SCREEN_IMAGE
                        When compiling for Windows and onefile, show this
                        while loading the application. Defaults to off.
    --windows-uac-admin
                        Request Windows User Control, to grant admin rights on
                        execution. (Windows only). Defaults to off.
    --windows-uac-uiaccess
                        Request Windows User Control, to enforce running from
                        a few folders only, remote desktop access. (Windows
                        only). Defaults to off.

  macOS specific controls:
    --macos-target-arch=MACOS_TARGET_ARCH
                        What architectures is this to supposed to run on.
                        Default and limit is what the running Python allows
                        for. Default is "native" which is the architecture the
                        Python is run with.
    --macos-create-app-bundle
                        When compiling for macOS, create a bundle rather than
                        a plain binary application. Currently experimental and
                        incomplete. Currently this is the only way to unlock
                        disabling of console.Defaults to off.
    --macos-app-icon=ICON_PATH
                        Add icon for the application bundle to use. Can be
                        given only one time. Defaults to Python icon if
                        available.
    --macos-signed-app-name=MACOS_SIGNED_APP_NAME
                        Name of the application to use for macOS signing.
                        Follow "com.YourCompany.AppName" naming results for
                        best results, as these have to be globally unique, and
                        will potentially grant protected API accesses.
    --macos-app-name=MACOS_APP_NAME
                        Name of the product to use in macOS bundle
                        information. Defaults to base filename of the binary.
    --macos-app-mode=MODE
                        Mode of application for the application bundle. When
                        launching a Window, and appearing in Docker is
                        desired, default value "gui" is a good fit. Without a
                        Window ever, the application is a "background"
                        application. For UI elements that get to display
                        later, "ui-element" is in-between. The application
                        will not appear in dock, but get full access to
                        desktop when it does open a Window later.
    --macos-sign-identity=MACOS_APP_VERSION
                        When signing on macOS, by default an ad-hoc identify
                        will be used, but with this option your get to specify
                        another identity to use. The signing of code is now
                        mandatory on macOS and cannot be disabled. Default
                        "ad-hoc" if not given.
    --macos-sign-notarization
                        When signing for notarization, using a proper TeamID
                        identity from Apple, use the required runtime signing
                        option, such that it can be accepted.
    --macos-app-version=MACOS_APP_VERSION
                        Product version to use in macOS bundle information.
                        Defaults to "1.0" if not given.
    --macos-app-protected-resource=RESOURCE_DESC
                        Request an entitlement for access to a macOS protected
                        resources, e.g.
                        "NSMicrophoneUsageDescription:Microphone access for
                        recording audio." requests access to the microphone
                        and provides an informative text for the user, why
                        that is needed. Before the colon, is an OS identifier
                        for an access right, then the informative text. Legal
                        values can be found on https://developer.apple.com/doc
                        umentation/bundleresources/information_property_list/p
                        rotected_resources and the option can be specified
                        multiple times. Default empty.

  Linux specific controls:
    --linux-icon=ICON_PATH
                        Add executable icon for onefile binary to use. Can be
                        given only one time. Defaults to Python icon if
                        available.

  Binary Version Information:
    --company-name=COMPANY_NAME
                        Name of the company to use in version information.
                        Defaults to unused.
    --product-name=PRODUCT_NAME
                        Name of the product to use in version information.
                        Defaults to base filename of the binary.
    --file-version=FILE_VERSION
                        File version to use in version information. Must be a
                        sequence of up to 4 numbers, e.g. 1.0 or 1.0.0.0, no
                        more digits are allowed, no strings are allowed.
                        Defaults to unused.
    --product-version=PRODUCT_VERSION
                        Product version to use in version information. Same
                        rules as for file version. Defaults to unused.
    --file-description=FILE_DESCRIPTION
                        Description of the file used in version information.
                        Windows only at this time. Defaults to binary
                        filename.
    --copyright=COPYRIGHT_TEXT
                        Copyright used in version information. Windows only at
                        this time. Defaults to not present.
    --trademarks=TRADEMARK_TEXT
                        Trademark used in version information. Windows only at
                        this time. Defaults to not present.

  Plugin control:
    --enable-plugins=PLUGIN_NAME
                        Enabled plugins. Must be plug-in names. Use '--plugin-
                        list' to query the full list and exit. Default empty.
    --disable-plugins=PLUGIN_NAME
                        Disabled plugins. Must be plug-in names. Use '--
                        plugin-list' to query the full list and exit. Most
                        standard plugins are not a good idea to disable.
                        Default empty.
    --plugin-no-detection
                        Plugins can detect if they might be used, and the you
                        can disable the warning via "--disable-plugin=plugin-
                        that-warned", or you can use this option to disable
                        the mechanism entirely, which also speeds up
                        compilation slightly of course as this detection code
                        is run in vain once you are certain of which plugins
                        to use. Defaults to off.
    --plugin-list       Show list of all available plugins and exit. Defaults
                        to off.
    --user-plugin=PATH  The file name of user plugin. Can be given multiple
                        times. Default empty.
    --show-source-changes
                        Show source changes to original Python file content
                        before compilation. Mostly intended for developing
                        plugins. Default False.

  Plugin options of 'anti-bloat':
    --show-anti-bloat-changes
                        Annotate what changes are by the plugin done.
    --noinclude-setuptools-mode=NOINCLUDE_SETUPTOOLS_MODE
                        What to do if a 'setuptools' or import is encountered.
                        This package can be big with dependencies, and should
                        definitely be avoided. Also handles 'setuptools_scm'.
    --noinclude-pytest-mode=NOINCLUDE_PYTEST_MODE
                        What to do if a 'pytest' import is encountered. This
                        package can be big with dependencies, and should
                        definitely be avoided. Also handles 'nose' imports.
    --noinclude-unittest-mode=NOINCLUDE_UNITTEST_MODE
                        What to do if a unittest import is encountered. This
                        package can be big with dependencies, and should
                        definitely be avoided.
    --noinclude-IPython-mode=NOINCLUDE_IPYTHON_MODE
                        What to do if a IPython import is encountered. This
                        package can be big with dependencies, and should
                        definitely be avoided.
    --noinclude-dask-mode=NOINCLUDE_DASK_MODE
                        What to do if a 'dask' import is encountered. This
                        package can be big with dependencies, and should
                        definitely be avoided.
    --noinclude-numba-mode=NOINCLUDE_NUMBA_MODE
                        What to do if a 'numba' import is encountered. This
                        package can be big with dependencies, and is currently
                        not working for standalone. This package is big with
                        dependencies, and should definitely be avoided.
    --noinclude-default-mode=NOINCLUDE_DEFAULT_MODE
                        This actually provides the default "warning" value for
                        above options, and can be used to turn all of these
                        on.
    --noinclude-custom-mode=CUSTOM_CHOICES
                        What to do if a specific import is encountered. Format
                        is module name, which can and should be a top level
                        package and then one choice, "error", "warning",
                        "nofollow", e.g. PyQt5:error.
```

</details>
<details>
<summary>目录</summary>

目录最后更新: 2023/10/14

* [Nuitka --help文档翻译](#nuitka---help文档翻译)
    * [信息](#信息)
* [Options(选项)](#options选项)
    * [basic(基本设置(无分类))](#basic基本设置无分类)
        * [--help](#--help)
        * [--version](#--version)
        * [--module](#--module)
        * [--standalone](#--standalone)
        * [--onefile](#--onefile)
        * [--python-debug](#--python-debug)
        * [--python-flag=FLAG](#--python-flagflag)
        * [--python-for-scons=PATH](#--python-for-sconspath)
        * [--main=PATH](#--mainpath)
    * [Control the inclusion of modules and packages in result(控制结果中包含的模块和包)](#control-the-inclusion-of-modules-and-packages-in-result控制结果中包含的模块和包)
        * [--include-package=PACKAGE](#--include-packagepackage)
        * [--include-module=MODULE](#--include-modulemodule)
        * [--include-plugin-directory=MODULE/PACKAGE](#--include-plugin-directorymodulepackage)
        * [--include-plugin-files=PATTERN](#--include-plugin-filespattern)
        * [--prefer-source-code](#--prefer-source-code)
    * [Control the following into imported modules(控制导入的模块)](#control-the-following-into-imported-modules控制导入的模块)
        * [--follow-imports](#--follow-imports)
        * [--follow-import-to=MODULE/PACKAGE](#--follow-import-tomodulepackage)
        * [--nofollow-import-to=MODULE/PACKAGE](#--nofollow-import-tomodulepackage)
        * [--nofollow-imports](#--nofollow-imports)
        * [--follow-stdlib](#--follow-stdlib)
    * [Onefile options(单文件选项)](#onefile-options单文件选项)
        * [--onefile-tempdir-spec=ONEFILE_TEMPDIR_SPEC](#--onefile-tempdir-speconefiletempdirspec)
        * [--onefile-child-grace-time=GRACE_TIME_MS](#--onefile-child-grace-timegracetimems)
        * [--onefile-no-compression](#--onefile-no-compression)
    * [Data files(数据文件)](#data-files数据文件)
        * [--include-package-data=PACKAGE](#--include-package-datapackage)
        * [--include-data-files=DESC](#--include-data-filesdesc)
        * [--include-data-dir=DIRECTORY](#--include-data-dirdirectory)
        * [--noinclude-data-files=PATTERN](#--noinclude-data-filespattern)
        * [--list-package-data=LIST_PACKAGE_DATA](#--list-package-datalistpackagedata)
    * [Metadata support(元数据支持)](#metadata-support元数据支持)
        * [--include-distribution-metadata=DISTRIBUTION](#--include-distribution-metadatadistribution)
    * [DLL files(DLL(动态链接库)文件)](#dll-filesdll动态链接库文件)
        * [--noinclude-dlls=PATTERN](#--noinclude-dllspattern)
        * [--list-package-dlls=LIST_PACKAGE_DLLS](#--list-package-dllslistpackagedlls)
    * [Control the warnings to be given by Nuitka(控制Nuitka发出的警告)](#control-the-warnings-to-be-given-by-nuitka控制nuitka发出的警告)
        * [--warn-implicit-exceptions](#--warn-implicit-exceptions)
        * [--warn-unusual-code](#--warn-unusual-code)
        * [--assume-yes-for-downloads](#--assume-yes-for-downloads)
        * [--nowarn-mnemonic=MNEMONIC](#--nowarn-mnemonicmnemonic)
    * [Immediate execution after compilation(编译后立刻执行)](#immediate-execution-after-compilation编译后立刻执行)
        * [--run](#--run)
        * [--debugger](#--debugger)
        * [--execute-with-pythonpath](#--execute-with-pythonpath)
    * [Compilation choices(编译选项)](#compilation-choices编译选项)
        * [--user-package-configuration-file=YAML_FILENAME](#--user-package-configuration-fileyamlfilename)
        * [--full-compat](#--full-compat)
        * [--file-reference-choice=MODE](#--file-reference-choicemode)
        * [--module-name-choice=MODE](#--module-name-choicemode)
    * [Output choices(输出选择)](#output-choices输出选择)
        * [--output-filename=FILENAME](#--output-filenamefilename)
        * [--output-dir=DIRECTORY](#--output-dirdirectory)
        * [--remove-output](#--remove-output)
        * [--no-pyi-file](#--no-pyi-file)
    * [Debug features(调试功能)](#debug-features调试功能)
        * [--debug](#--debug)
        * [--unstripped](#--unstripped)
        * [--profile](#--profile)
        * [--internal-graph](#--internal-graph)
        * [--trace-execution](#--trace-execution)
        * [--recompile-c-only](#--recompile-c-only)
        * [--xml=XML_FILENAME](#--xmlxmlfilename)
        * [--deployment](#--deployment)
        * [--no-deployment-flag=FLAG](#--no-deployment-flagflag)
        * [--experimental=FLAG](#--experimentalflag)
        * [--low-memory](#--low-memory)
        * [--create-environment-from-report=CREATE_ENVIRONMENT_FROM_REPORT](#--create-environment-from-reportcreateenvironmentfromreport)
        * [--generate-c-only](#--generate-c-only)
    * [Backend C compiler choice(后端 C 编译器选择)](#backend-c-compiler-choice后端-c-编译器选择)
        * [--clang](#--clang)
        * [--mingw64](#--mingw64)
        * [--msvc=MSVC_VERSION](#--msvcmsvcversion)
        * [--jobs=N](#--jobsn)
        * [--lto=choice](#--ltochoice)
        * [--static-libpython=choice](#--static-libpythonchoice)
    * [Cache Control(缓存控制)](#cache-control缓存控制)
        * [--disable-cache=DISABLED_CACHES](#--disable-cachedisabledcaches)
        * [--clean-cache=CLEAN_CACHES](#--clean-cachecleancaches)
        * [--disable-bytecode-cache](#--disable-bytecode-cache)
        * [--disable-ccache](#--disable-ccache)
        * [--disable-dll-dependency-cache](#--disable-dll-dependency-cache)
        * [--force-dll-dependency-cache-update](#--force-dll-dependency-cache-update)
    * [PGO compilation choices(PGO(配置文件引导优化)编译选项)](#pgo-compilation-choicespgo配置文件引导优化编译选项)
        * [--pgo](#--pgo)
        * [--pgo-args=PGO_ARGS](#--pgo-argspgoargs)
        * [--pgo-executable=PGO_EXECUTABLE](#--pgo-executablepgoexecutable)
    * [Tracing features(跟踪功能)](#tracing-features跟踪功能)
        * [--report=REPORT_FILENAME](#--reportreportfilename)
        * [--report-diffable](#--report-diffable)
        * [--report-user-provided=KEY_VALUE](#--report-user-providedkeyvalue)
        * [--report-template=REPORT_DESC](#--report-templatereportdesc)
        * [--quiet](#--quiet)
        * [--show-scons](#--show-scons)
        * [--no-progressbar](#--no-progressbar)
        * [--show-progress](#--show-progress)
        * [--show-memory](#--show-memory)
        * [--show-modules](#--show-modules)
        * [--show-modules-output=PATH](#--show-modules-outputpath)
        * [--verbose](#--verbose)
        * [--verbose-output=PATH](#--verbose-outputpath)
    * [General OS controls(通用操作系统控制)](#general-os-controls通用操作系统控制)
        * [--disable-console](#--disable-console)
        * [--enable-console](#--enable-console)
        * [--force-stdout-spec=FORCE_STDOUT_SPEC](#--force-stdout-specforcestdoutspec)
        * [--force-stderr-spec=FORCE_STDERR_SPEC](#--force-stderr-specforcestderrspec)
    * [Windows specific controls(Windows特定控制)](#windows-specific-controlswindows特定控制)
        * [--windows-icon-from-ico=ICON_PATH](#--windows-icon-from-icoiconpath)
        * [--windows-icon-from-exe=ICON_EXE_PATH](#--windows-icon-from-exeiconexepath)
        * [--onefile-windows-splash-screen-image=SPLASH_SCREEN_IMAGE](#--onefile-windows-splash-screen-imagesplashscreenimage)
        * [--windows-uac-admin](#--windows-uac-admin)
        * [--windows-uac-uiaccess](#--windows-uac-uiaccess)
    * [macOS specific controls(MacOS特定控制)](#macos-specific-controlsmacos特定控制)
        * [--macos-target-arch=MACOS_TARGET_ARCH](#--macos-target-archmacostargetarch)
        * [--macos-create-app-bundle](#--macos-create-app-bundle)
        * [--macos-app-icon=ICON_PATH](#--macos-app-iconiconpath)
        * [--macos-signed-app-name=MACOS_SIGNED_APP_NAME](#--macos-signed-app-namemacossignedappname)
        * [--macos-app-name=MACOS_APP_NAME](#--macos-app-namemacosappname)
        * [--macos-app-mode=MODE](#--macos-app-modemode)
        * [--macos-sign-identity=MACOS_APP_VERSION](#--macos-sign-identitymacosappversion)
        * [--macos-sign-notarization](#--macos-sign-notarization)
        * [--macos-app-version=MACOS_APP_VERSION](#--macos-app-versionmacosappversion)
        * [--macos-app-protected-resource=RESOURCE_DESC](#--macos-app-protected-resourceresourcedesc)
    * [Linux specific controls(Linux特定控制)](#linux-specific-controlslinux特定控制)
        * [--linux-icon=ICON_PATH](#--linux-iconiconpath)
    * [Binary Version Information(二进制版本信息)](#binary-version-information二进制版本信息)
        * [--company-name=COMPANY_NAME](#--company-namecompanyname)
        * [--product-name=PRODUCT_NAME](#--product-nameproductname)
        * [--file-version=FILE_VERSION](#--file-versionfileversion)
        * [--product-version=PRODUCT_VERSION](#--product-versionproductversion)
        * [--file-description=FILE_DESCRIPTION](#--file-descriptionfiledescription)
        * [--copyright=COPYRIGHT_TEXT](#--copyrightcopyrighttext)
        * [--trademarks=TRADEMARK_TEXT](#--trademarkstrademarktext)
    * [Plugin control(插件控制)](#plugin-control插件控制)
        * [--enable-plugins=PLUGIN_NAME](#--enable-pluginspluginname)
        * [--disable-plugins=PLUGIN_NAME](#--disable-pluginspluginname)
        * [--plugin-no-detection](#--plugin-no-detection)
        * [--plugin-list](#--plugin-list)
        * [--user-plugin=PATH](#--user-pluginpath)
        * [--show-source-changes](#--show-source-changes)
    * [Plugin options of 'anti-bloat'('反膨胀'插件选项)](#plugin-options-of-anti-bloat反膨胀插件选项)
        * [--show-anti-bloat-changes](#--show-anti-bloat-changes)
        * [--noinclude-setuptools-mode=NOINCLUDE_SETUPTOOLS_MODE](#--noinclude-setuptools-modenoincludesetuptoolsmode)
        * [--noinclude-pytest-mode=NOINCLUDE_PYTEST_MODE](#--noinclude-pytest-modenoincludepytestmode)
        * [--noinclude-unittest-mode=NOINCLUDE_UNITTEST_MODE](#--noinclude-unittest-modenoincludeunittestmode)
        * [--noinclude-IPython-mode=NOINCLUDE_IPYTHON_MODE](#--noinclude-ipython-modenoincludeipythonmode)
        * [--noinclude-dask-mode=NOINCLUDE_DASK_MODE](#--noinclude-dask-modenoincludedaskmode)
        * [--noinclude-numba-mode=NOINCLUDE_NUMBA_MODE](#--noinclude-numba-modenoincludenumbamode)
        * [--noinclude-default-mode=NOINCLUDE_DEFAULT_MODE](#--noinclude-default-modenoincludedefaultmode)
        * [--noinclude-custom-mode=CUSTOM_CHOICES](#--noinclude-custom-modecustomchoices)

</details>

# Options(选项)

## basic(基本设置(无分类))

---

### --help

原始参数名:

```
--help
```

中文参数名:

```
帮助
```

原始简介:

```
show this help message and exit
```

中文简介:

```
显示帮助信息并退出
```

---

### --version

原始参数名:

```
--version
```

中文参数名:

``` 
版本
```

原始简介:

```
Show version information and important details for bug reports, then exit.
Defaults to off.
```

中文简介:

```
显示版本信息和重要的错误报告细节，然后退出。默认关闭。
```

---

### --module

原始参数名:

```
--module
```

中文参数名:

```
模块
```

原始简介:

```
Create an extension module executable instead of a program. Defaults to off.
```

中文简介:

``` 
创建一个扩展模块可执行文件而不是一个程序。默认关闭。
```

---

### --standalone

原始参数名:

```
--standalone
```

中文参数名:

```
独立
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
启用独立模式进行输出。这允许你将二进制文件传输到其他机器, 而无需使用已有的Python环境。
这也意味着它将变得很大。它将启用这些选项: "-- follow-imports" 和 "--python-flag=no_site"。
默认关闭。
```

---

### --onefile

原始参数名:

```
--onefile
```

中文参数名:

```
单文件
```

原始简介:

```
On top of standalone mode, enable onefile mode. This means not a folder, but a
compressed executable is created and used. Defaults to off.
```

中文简介:

```
在独立模式的基础上, 启用单文件模式。这意味着不是一个文件夹, 而是创建和使用一个压缩的可执行文件。
默认关闭。
```

---

### --python-debug

原始参数名:

```
--python-debug
``` 

中文参数名:

```
Python调试
```

原始简介:

```
Use debug version or not. Default uses what you are using to run Nuitka, most
likely a non-debug version.
```

中文简介:

```
使用调试版本或不使用。默认使用你用来运行Nuitka的(调试)版本, 大多数情况下是非调试版本。
```

---

### --python-flag=FLAG

原始参数名:

```
--python-flag=FLAG
```

中文参数名:

```
Python标志
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
要使用的Python标志.默认是你用来运行Nuitka的内容, 这强制使用特定模式.这些也是标准Python可执行文件中存在的选项.
目前支持的有: "-S" (别名 "no_site")(不应该包含python的site-packages目录,也就是不包含任何python环境的第三方库),
"static_hashes" (不使用哈希随机化), "no_warnings" (不给出Python运行时的警告),
"-O" (别名 "no_asserts")(不包含任何调试/错误检查(assert)语句), "no_docstrings" (不使用文档字符串),
“-u”（别名 “unbuffered”）(不使用缓冲), "isolated" (不加载外部代码) 和 "-m" (包模式, 编译为 "package.__main__").
默认为空。
```

---

### --python-for-scons=PATH

原始参数名:

```
--python-for-scons=PATH
```

中文参数名:

```
Scons的Python路径=路径
```

原始简介:

```
If using Python3.3 or Python3.4, provide the path of a Python binary to use for
Scons. Otherwise Nuitka can use what you run Nuitka with or a Python
installation from Windows registry. On Windows Python 3.5 or higher is needed.
On non-Windows, Python 2.6 or 2.7 will do as well.
```

中文简介:

```
如果使用Python3.3或Python3.4, 提供一个Python二进制文件的路径给Scons使用.
否则，Nuitka可以使用您运行Nuitka的内容(环境), 或者从Windows注册表中获取Python安装。
在Windows上，需要Python 3.5或更高的版本。在非Windows系统上，Python 2.6或2.7也可以
```

---

### --main=PATH

原始参数名:

```
--main=PATH
```

中文参数名:

```
主程序=路径
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
如果只指定一次(如--main="1.py")，这将取代位置参数，也就是要编译的文件名(入口)。 
如果指定多次(如--main="1.py" --main="2.py"), 它将启用"multidist"(参见用户手册),它允许您创建依赖于文件名或调用名的二进制文件。
(允许多个主程序使用同一套编译参数)

Multidist补充:
我们把主路径的基本名称和入口点称为entry point。这些名称当然必须是不同的。然后创建的二进制文件可以执行任何一个入口点，
并会对sys.argv[0]如何显示做出反应。所以如果以正确的方式执行（通过像subprocess或OS API这样的东西你可以控制这个名字），
或者通过重命名或复制二进制文件，或者链接到它，你就可以实现奇迹。
这种模式适用于独立模式、onefile模式和纯加速模式。它不适用于模块模式。
例子:
|-1.py
|-2.py
nuitka --main=./1.py --main=./2.py --standalone 1.py
运行打包后的1.exe: 得到1.py的运行结果
改名为2.exe: 得到2.py的运行结果
```

---

---

## Control the inclusion of modules and packages in result(控制结果中包含的模块和包)

---

### --include-package=PACKAGE

原始参数名:

```
--include-package=PACKAGE
```

中文参数名:

```
包含包=包
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
包含整个包。以Python命名空间的形式给出，例如’some_package.sub_package’，
然后Nuitka会找到它并包含它以及在其创建的二进制或扩展模块的磁盘位置下面找到的所有模块，并使其可以被代码导入。
为了避免不需要的子包，例如测试，你可以这样做’–nofollow-import-to=*.tests’。默认为空。
(注: 这里的包含是指将包含的包或模块编译到二进制文件中并可以被代码导入, 而不是将其作为依赖项)
(示例:nuitka --include-package=numpy --include-package=pandas main.py)
```

---

### --include-module=MODULE

原始参数名:

```
--include-module=MODULE
```

中文参数名:

```
包含模块=模块
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
包含单个模块。以Python命名控件的形式给出，例如'some_package.some_module'，然后Nuitka会找到它并将其包含在其创建的二进制文件或扩展模块中，
并使其可以被代码导入。默认为空
```

---

### --include-plugin-directory=MODULE/PACKAGE

原始参数名:

```
--include-plugin-directory=MODULE/PACKAGE
```

中文参数名:

```
包含插件目录=模块/包                                                                                                                                                                                                                    
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
同时包括该目录中找到的代码，将它们视为各自的主文件。这将覆盖其他包含(include)选项。
你应该更倾向于使用其他包含选项。它们是通过名称而不是文件名来查找的，这些选项可以通过在'sys.path'中找到东西
这个选项只适用于非常特殊的用例。可以多次给出。默认为空。
```

---

### --include-plugin-files=PATTERN

原始参数名:

```
--include-plugin-files=PATTERN
```

中文参数名:

```
包含插件文件=模式
```

原始简介:

```
Include into files matching the PATTERN. Overrides all other follow options.
Can be given multiple times. Default empty.
```

中文简介:

```
包含匹配PATTERN(模式)的文件。覆盖所有其他的跟随选项。可以多次给出。默认为空
```

---

### --prefer-source-code

原始参数名:

```
--prefer-source-code
```

中文参数名:

```
首选源代码
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
对于已经编译的拓展模块，如果存在源代码和拓展模块，通常会使用拓展模块，但为了获得最佳的性能，最好从可用的源代码编译模块。
如果不需要，可以使用--nop-perfer-source-code来禁用有关于此的警告。默认关闭。
```

---

---

## Control the following into imported modules(控制导入的模块)

---

### --follow-imports

原始参数名:

```
--follow-imports
```

中文参数名:

```
跟随导入们
```

原始简介:

```
Descend into all imported modules. Defaults to on in standalone mode, otherwise
off.
```

中文简介:

```
导入所有被导入的模块。在独立模式下默认开启，否则关闭
```

---

### --follow-import-to=MODULE/PACKAGE

原始参数名:

```
--follow-import-to=MODULE/PACKAGE
```

中文参数名:

```
跟随导入到=模块/包
```

原始简介:

```
Follow to that module if used, or if a package, to the whole package. Can be
given multiple times. Default empty.
```

中文简介:

```
如果使用了该模块，则跟随到该模块，或者如果是一个包，则跟随到整个包。可以多次给出。默认为空。
```

---

### --nofollow-import-to=MODULE/PACKAGE

原始参数名:

```
--nofollow-import-to=MODULE/PACKAGE
```

中文参数名:

```
不跟随导入=模块/包
```

原始简介:

```
Do not follow to that module name even if used, or if a package name, to the
whole package in any case, overrides all other options. Can be given multiple
times. Default empty.
```

中文简介:

```
即使使用了该模块名也不导入该模块，或者如果是一个包名，在任何情况下都不要导入整个包，这将覆盖所有其他的选项，可以多次给出，默认为空。
```

---

### --nofollow-imports

原始参数名:

```
--nofollow-imports
```

中文参数名:

```
不进行所有导入
```

原始简介:

```
Do not descend into any imported modules at all, overrides all other inclusion
options and not usable for standalone mode. Defaults to off.
```

中文简介:

```
不递归深入(导入)到任何导入的模块，这将覆盖所有其他包含选项，并且不能用于独立模式。默认关闭。
```

---

### --follow-stdlib

原始参数名:

```
--follow-stdlib
```

中文参数名:

```
跟随导入标准库
```

原始简介:

```
Also descend into imported modules from standard library. This will increase
the compilation time by a lot and is also not well tested at this time and
sometimes won't work. Defaults to off.
```

中文简介:

```
也深入到从标准库导入的模块，这将大大增加编译时间，而且目前也没有很好的测试，有时候也可能不会工作。默认关闭。
```

---

---

## Onefile options(单文件选项)

---

### --onefile-tempdir-spec=ONEFILE_TEMPDIR_SPEC

原始参数名:

```
--onefile-tempdir-spec=ONEFILE_TEMPDIR_SPEC
```

中文参数名:

```
单文件临时目录位置=单文件临时目录位置(规范)
```

原始简介:

```
Use this as a folder to unpack to in onefile mode. Defaults to
'%TEMP%/onefile_%PID%_%TIME%', i.e. user temporary directory and being
non-static it's removed. Use e.g. a string like
'%CACHE_DIR%/%COMPANY%/%PRODUCT%/%VERSION%' which is a good static cache path,
this will then not be removed.
```

中文简介:

```
在单文件模式下，使用此作为解压的文件夹。默认为’%TEMP%/onefile_%PID%_%TIME%‘，即用户临时目录，并且是非静态的，所以它将会被删除。
例如，可以使用像’%CACHE_DIR%/%COMPANY%/%PRODUCT%/%VERSION%'这样的字符串，这是一个很好的静态缓存路径，并且它将不会被删除。”
```

---

### --onefile-child-grace-time=GRACE_TIME_MS

原始参数名:

```
--onefile-child-grace-time=GRACE_TIME_MS
```

中文参数名:

```
单文件紫禁城宽限时间=宽限时间(毫秒)
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
当停止子进程时，例如由于CTRL-C或关闭等，Python代码会得到一个"KeyboardInterrupt"，它可能会处理例如刷新数据等事件。
这是以硬方式杀死子进程之前的时间量。单位是毫秒，默认为5000。
```

---

### --onefile-no-compression

原始参数名:

```
--onefile-no-compression
```

中文参数名:

```
无压缩单文件
```

原始简介:

```
When creating the onefile, disable compression of the payload. This is mostly
for debug purposes, or to save time. Default is off.
```

中文简介:

```
在创建单文件时，禁用有效载荷的压缩。这主要是出于调试目的，或者为了节省时间。默认关闭
```

---

---

## Data files(数据文件)

---

### --include-package-data=PACKAGE

原始参数名:

```
--include-package-data=PACKAGE
```

中文参数名:

```
包括包数据=包名
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
包括给定包的数据文件。DLL和扩展模块不是数据文件，也不会像这样被包含。可以使用下面指示的文件名模式。
默认情况下，不包括包的数据文件，但包配置可以执行此操作。这只会包括非DLL和非拓展模块，即实际存在的数据文件。
在":"后面，还可以给出文件名模式，只选择匹配的文件。例子: "--include-package-data=package_name" (所有文件)
--include-package-data=package_name=*.txt" (只有某种类型) "--include-package-data=package_name=some_filename.dat (具体文件)
默认为空。
```

---

### --include-data-files=DESC

原始参数名:

```
--include-data-files=DESC
```

中文参数名:

```
包含数据文件=路径
```

原始简介:

```
Include data files by filenames in the distribution. There are many allowed
forms. With '--include-data- files=/path/to/file/*.txt=folder_name/some.txt' it
will copy a single file and complain if it's multiple. With '--include-data-
files=/path/to/files/*.txt=folder_name/' it will put all matching files into
that folder. For recursive copy there is a form with 3 values that '--include-
data-files=/path/to/scan=folder_name=**/*.txt' that will preserve directory
structure. Default empty.
```

中文简介:

```
通过分配的文件名包含数据文件。有很多允许的形式。
使用–include-data-files=/path/to/file/.txt=folder_name/some.txt’，它将复制一个文件，如果是十多个文件，将会报错。
使用’–include-data-files=/path/to/files/.txt=folder_name/‘将把所有匹配的文件放入该文件夹。
对于递归复制，有一种带有三个值的形式:’–include-data-files=/path/to/scan=folder_name=**/*.txt’，这将保留目录的文件结构。
默认为空。

```

---

### --include-data-dir=DIRECTORY

原始参数名:

```
--include-data-dir=DIRECTORY
```

中文参数名:

```
包含数据目录=目录
```

原始简介:

```
Include data files from complete directory in the distribution. This is
recursive. Check '--include- data-files' with patterns if you want non-recursive
inclusion. An example would be '--include-data-
dir=/path/some_dir=data/some_dir' for plain copy, of the whole directory. All
files are copied, if you want to exclude files you need to remove them
beforehand, or use '--noinclude-data-files' option to remove them. Default
empty.
```

中文简介:

```
将整个目录的数据文件包含在分发中。这是递归的。
如果你想要非递归包含，请查看'--include-data-files'与模式。
’–include-data-dir=/path/some_dir=data/some_dir’，用于整个目录的普通复制。
所有文件都会被复制，如果你想排除文件，你需要事先删除它们，或者使用’–noinclude-data-files’选项来删除它们。
默认为空。
```

---

### --noinclude-data-files=PATTERN

原始参数名:

```
--noinclude-data-files=PATTERN
```

中文参数名:

```
不包含数据文件=形式
```

原始简介:

```
Do not include data files matching the filename pattern given. This is against
the target filename, not source paths. So to ignore a file pattern from package
data for "package_name" should be matched as "package_name/*.txt". Or for the
whole directory simply use "package_name". Default empty.
```

中文简介:

```
不包含与给定文件名形式匹配的数据文件。这是针对目标文件名而非源路径的。
因此，要从'package_name'的包数据中忽略一个文件模式，应该匹配为"package_name/*.txt",
或者啥对整个目录而简单地使用"package_name"。默认为空
```

---

### --list-package-data=LIST_PACKAGE_DATA

原始参数名:

```
--list-package-data=LIST_PACKAGE_DATA
```

中文参数名:

```
列出包数据
```

原始简介:

```
Output the data files found for a given package name. Default not done.
```

中文简介:

```
输出给定包名称找到的数据文件。默认不执行
```

---

---

## Metadata support(元数据支持)

---

### --include-distribution-metadata=DISTRIBUTION

原始参数名:

```
--include-distribution-metadata=DISTRIBUTION
```

中文参数名:

```
包含元数据分发分发
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
未给定的分发名称包含元数据信息。有些包会检查元数据的存在、版本、入口点灯，而如果没有给出这些选项，它只能在编译时被识别才会工作，这并不总是会发生。
当然，这只对包含在编译中的包有意义。默认为空。
```

---

---

## DLL files(DLL(动态链接库)文件)

---

### --noinclude-dlls=PATTERN

原始参数名:

```
--noinclude-dlls=PATTERN
```

中文参数名:

```
不包含动态链接库们=模式
```

原始简介:

```
Do not include DLL files matching the filename pattern given. This is against
the target filename, not source paths. So ignore a DLL "someDLL" contained in
the package "package_name" it should be matched as "package_name/someDLL.*".
Default empty.
```

中文简介:

```
不要包括与给定文件名模式匹配的DLL文件。这是针对目标文件名，而不是源路径。
因此，要忽略包含在“package_name”包中的DLL“someDLL”，应将其匹配为“package_name/someDLL.*”。
默认为空。
```

---

### --list-package-dlls=LIST_PACKAGE_DLLS

原始参数名:

```
--list-package-dlls=LIST_PACKAGE_DLLS
```

中文参数名:

```
列出包动态链接库们=包名
```

原始简介:

```
Output the DLLs found for a given package name. Default not done.
```

中文简介:

```
为给定的包名找到DLLs并输出。默认不执行。
```

---

---

## Control the warnings to be given by Nuitka(控制Nuitka发出的警告)

---

### --warn-implicit-exceptions

原始参数名:

```
--warn-implicit-exceptions
```

中文参数名:

```
警告隐式异常
```

原始简介:

```
Enable warnings for implicit exceptions detected at compile time.
```

中文简介:

```
启用对在编译时检测到的隐式异常的警告。
```

---

### --warn-unusual-code

原始参数名:

```
--warn-unusual-code
```

中文参数名:

```
警告不寻常的代码
```

原始简介:

```
Enable warnings for unusual code detected at compile time.
```

中文简介:

```
启用对在编译时对检测到的不寻常代码的警告。
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
在需要时允许Nuitka下载外部代码。例如依赖项walker,ccache,甚至Windows上的gcc。要禁用，请从nul设备重定向输入。
例如"</dev/null"或"<NUL:"。默认下载时提示。
```

---

### --nowarn-mnemonic=MNEMONIC

原始参数名:

```
--nowarn-mnemonic=MNEMONIC
```

中文参数名:

```
不警告助记符=助记符
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
禁用给定助记符的警告。这些是为了确保你知道某些主题，并且通常指向Nuitka网站。助记符是URL末尾的部分，没有HTML后缀。可以多次给出并接受shell模式。默认为空。
```

---

---

## Immediate execution after compilation(编译后立刻执行)

---

### --run

原始参数名:

```
--run
```

中文参数名:

```
运行
```

原始简介:

```
Execute immediately the created binary (or import the compiled module).
Defaults to off.
```

中文简介:

```
立即执行创建的二进制文件(或导入已编译的模块)。默认关闭。
```

---

### --debugger

原始参数名:

```
--debugger
```

中文参数名:

```
调试器
```

原始简介:

```
Execute inside a debugger, e.g. "gdb" or "lldb" to automatically get a stack
trace. Defaults to off.
```

中文简介:

```
在调试器中执行，例如“gdb”或“lldb”以自动获取堆栈跟踪。默认关闭。
```

---

### --execute-with-pythonpath

原始参数名:

```
--execute-with-pythonpath
```

中文参数名:

```
使用pythonpath(python路径)执行
```

原始简介:

```
When immediately executing the created binary or module using '--run', don't
reset 'PYTHONPATH' environment. When all modules are successfully included, you
ought to not need PYTHONPATH anymore, and definitely not for standalone mode.
```

中文简介:

```
当使用'--run'立刻执行创建的二进制文件或模块时，不要重置'PYTHONPATH'环境。当所有模块都成功包含时，您应该不再需要PYTHONPATH。
对于独立模式(standalone)来说，绝对不需要PYTHONPATH。
```

---

---

## Compilation choices(编译选项)

---

### --user-package-configuration-file=YAML_FILENAME

原始参数名:

```
--user-package-configuration-file=YAML_FILENAME
```

中文参数名:

```
用户包配置文件=YAML文件名
```

原始简介:

```
User provided Yaml file with package configuration. You can include DLLs,
remove bloat, add hidden dependencies. Check User Manual for a complete
description of the format to use. Can be given multiple times. Defaults to
empty.
```

中文简介:

```
用户提供包含包配置的Yaml文件. 您可以包括DLL文件,删除冗余，添加隐藏的依赖项。查看用户手册以获取使用格式的完整描述。可以多次给出。默认为空。
```

---

### --full-compat

原始参数名:

```
--full-compat
```

中文参数名:

```
完全兼容
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
确保和CPython绝对兼容。甚至不允许与CPython行为的轻微偏差，例如没有更好的跟踪回溯(trackback)或异常消息。
这些行为并不是真正的不兼容，而只是不同或者更糟糕而已。这仅用于测试，不应该使用。
```

---

### --file-reference-choice=MODE

原始参数名:

```
--file-reference-choice=MODE
```

中文参数名:

```
中文参数名:
文件引用选择=模式
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
选择"__file__"的值。创建的二进制文件和模块"执行时"（即独立二进制文件和摸块模式的默认值)使用自己
的位置来扣除"__file__"的值。包含的软件包假装在该位置下方的目录中。这样就可以在部署中包含数据文件。
如果只是为了加速，最好使用"原始(original)"值，其中将使用源文件位置。也就是使用源文件的位置。使用"frozen"的时候，
会使用"<frozen module_name>"符号。出于兼容性的原因，"__file__"值将始终具有".py"后缀，而与它的实际值无关。
```

---

### --module-name-choice=MODE

原始参数名:

```
--module-name-choice=MODE
```

中文参数名:

```
模块名称选择=模式
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
选择"__name__"和"__package__"的值。使用"执行时(runtime)"（模块模式的默认值）创建的模块使用软件包
来推断"__package__"的值，以实现完全兼容。"原始(original)"值（其他模式的默认值）允许进行更多的静态优化，但对那些通常
可以加载到任意软件包的模块来说是不兼容的。
```

---

---

## Output choices(输出选择)

---

### --output-filename=FILENAME

原始参数名:

```
--output-filename=FILENAME
```

中文参数名:

```
输出文件名=文件名
```

原始简介:

```
Specify how the executable should be named. For extension modules there is no
choice, also not for standalone mode and using it will be an error. This may
include path information that needs to exist though. Defaults to
'<program_name>' on this platform. .exe
```

中文简介:

```
指定可执行文件的名称。拓展模块和独立模式没有这个选项，使用时会报错。这可能需要包含存在的路径信息。
默认为该平台上的"<program_name>.exe"
```

---

### --output-dir=DIRECTORY

原始参数名:

```
--output-dir=DIRECTORY
```

中文参数名:

```
输出目录=目录
```

原始简介:

```
Specify where intermediate and final output files should be put. The DIRECTORY
will be populated with build folder, dist folder, binaries, etc. Defaults to
current directory.
```

中文简介:

```
指定存放中间文件和最终输出文件的位置。选定目录将存放构建文件夹，发行文件夹，二进制文件等。默认为当前目录。
```

---

### --remove-output

原始参数名:

```
--remove-output
```

中文参数名:

```
删除构建文件夹
```

原始简介:

```
Removes the build directory after producing the module or exe file. Defaults to
off.
```

中文简介:

```
生成exe或者模块文件后删除构建文件夹。默认关闭。
```

---

### --no-pyi-file

原始参数名:

```
--no-pyi-file
```

中文参数名:

```
不创建pyi文件
```

原始简介:

```
Do not create a ".pyi" file for extension modules created by Nuitka. This is
used to detect implicit imports. Defaults to off.
```

中文简介:

```
不要为Nuitka创建拓展模块而创建".pyi"文件用于检测隐式导入。默认关闭。
```

---

---

## Debug features(调试功能)

---

### --debug

原始参数名:

```
--debug
```

中文参数名:

```
调试
```

原始简介:

```
Executing all self checks possible to find errors in Nuitka, do not use for
production. Defaults to off.
```

中文简介:

```
执行所有可能的自身检查以发现Nuitka中的错误，请不要用与生产中。
默认关闭。
```

---

### --unstripped

原始参数名:

```
--unstripped
```

中文参数名:

```
不去除调试信息
```

原始简介:

```
Keep debug info in the resulting object file for better debugger interaction.
Defaults to off.
```

中文简介:

```
在生成的对象文件中保留调试信息，以便更好的和调试器交互。默认关闭。
```

---

### --profile

原始参数名:

```
--profile
```

中文参数名:

```
耗时分析
```

原始简介:

```
Enable vmprof based profiling of time spent. Not working currently. Defaults to
off.
```

中文简介:

```
启用基于vmprof的耗时分析。目前无法使用。默认关闭。
```

---

### --internal-graph

原始参数名:

```
--internal-graph
```

中文参数名:

```
内部图
```

原始简介:

```
Create graph of optimization process internals, do not use for whole programs,
but only for small test cases. Defaults to off.
```

中文简介:

```
创建优化过程内部的图，不要用于整个程序，请只用于小的测试用例。默认关闭。
```

---

### --trace-execution

原始参数名:

```
--trace-execution
```

中文参数名:

```
跟踪执行
```

原始简介:

```
Traced execution output, output the line of code before executing it. Defaults
to off.
```

中文简介:

```
跟踪执行并输出。在执行代码之前输出代码行。默认关闭。
```

---

### --recompile-c-only

原始参数名:

```
--recompile-c-only
```

中文参数名:

```

```

原始简介:

```
This is not incremental compilation, but for Nuitka development only. Takes
existing files and simply compile them as C again. Allows compiling edited C
files for quick debugging changes to the generated source, e.g. to see if code
is passed by, values output, etc, Defaults to off. Depends on compiling Python
source to determine which files it should look at.
```

中文简介:

```
这不是增量编译，仅用于 Nuitka 开发。将现有文件重新编译为C。允许编译编辑过的C文件，以便对生成源代码的修改进行快速调试。
例如查看代码是否通过，值的输出等。默认关闭。它要查看的文件取决于编译Python源代码。 
```

---

### --xml=XML_FILENAME

原始参数名:

```
--xml=XML_FILENAME
```

中文参数名:

```
xml=xml文件名
```

原始简介:

```
Write the internal program structure, result of optimization in XML form to
given filename.
```

中文简介:

```
将内部程序结构和优化结果以XML形式写入给定的文件名。
```

---

### --deployment

原始参数名:

```
--deployment
```

中文参数名:

```
发布模式
```

原始简介:

```
Disable code aimed at making finding compatibility issues easier. This will
e.g. prevent execution with "-c" argument, which is often used by code that
attempts run a module, and causes a program to start itself over and over
potentially. Default off.
```

中文简介:

```
禁用用于更方便发现兼容性问题的代码。例如，这将阻止使用"-c"参数执行，
该参数通常被试图运行模块的代码所使用，并可能导致程序一次又一次地启动自己。默认关闭
```

---

### --no-deployment-flag=FLAG

原始参数名:

```
--no-deployment-flag=FLAG
```

中文参数名:

```
禁用发布模式标识=标识
```

原始简介:

```
Keep deployment mode, but disable selectively parts of it. Errors from
deployment mode will output these identifiers. Default empty.
```

中文简介:

```
保持发布模式。但是选择性的禁用其中的某些功能。发布模式的错误将输出这些标识符。默认为空。
```

---

### --experimental=FLAG

原始参数名:

```
--experimental=FLAG
```

中文参数名:

```
实验性=标识符
```

原始简介:

```
Use features declared as 'experimental'. May have no effect if no experimental
features are present in the code. Uses secret tags (check source) per
experimented feature.
```

中文简介:

```
使用声明为"实验性"的功能。如果代码中没有实验性功能，则可能不会产生任何影响。
使用每个实验功能的秘密标签(检查源代码)。
```

---

### --low-memory

原始参数名:

```
--low-memory
```

中文参数名:

```
低内存模式
```

原始简介:

```
Attempt to use less memory, by forking less C compilation jobs and using
options that use less memory. For use on embedded machines. Use this in case of
out of memory problems. Defaults to off.
```

中文简介:

```
尝试使用更少的内存，方法是减少C编译任务的分叉并使用更少内存的选项。用于嵌入式机器。在出现内存不足的问题时使用。默认为关闭。
```

---

### --create-environment-from-report=CREATE_ENVIRONMENT_FROM_REPORT

原始参数名:

```
--create-environment-from-report=CREATE_ENVIRONMENT_FROM_REPORT
```

中文参数名:

```
从报告中创建环境=报告
```

原始简介:

```
Create a new virtualenv in that non-existing path from the report file given
with e.g. '--report=compilation-report.xml'. Default not done.
```

中文简介:

```
根据给出的报告文件在不存在的路径中创建一个新的虚拟环境，例如'--report=compilation-report.xml'。默认不执行。
```

---

### --generate-c-only

原始参数名:

```
--generate-c-only
```

中文参数名:

```
只生成C文件
```

原始简介:

```
Generate only C source code, and do not compile it to binary or module. This is
for debugging and code coverage analysis that doesn't waste CPU. Defaults to
off. Do not think you can use this directly.
```

中文简介:

```
只生成C源代码，不编译为二进制文件或者模块。这是用于调试和代码覆盖分析的，不会浪费CPU。默认关闭。
不要认为你可以直接使用这个。
```

---

---

## Backend C compiler choice(后端 C 编译器选择)

---

### --clang

原始参数名:

```
--clang
```

中文参数名:

```
强制使用clang
```

原始简介:

```
Enforce the use of clang. On Windows this requires a working Visual Studio
version to piggy back on. Defaults to off.
```

中文简介:

```
强制使用 clang 编译。在 Windows 系统上，这需要一个正常运行的 Visual Studio 版本来支持。默认关闭。
```

---

### --mingw64

原始参数名:

```
--mingw64
```

中文参数名:

```
强制使用mingw64
```

原始简介:

```
Enforce the use of MinGW64 on Windows. Defaults to off unless MSYS2 with MinGW
Python is used.
```

中文简介:

```
强制在 Windows 上使用 MinGW64。默认为关闭，除非使用 MSYS2 和 MinGW Python。
```

---

### --msvc=MSVC_VERSION

原始参数名:

```
--msvc=MSVC_VERSION
```

中文参数名:

```
使用msvc=msvc版本
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
强制在Windows上使用特定的MSVC版本。允许的值有"14.3" (MSVC 2022)和其他MSVC版本号。
使用 "list "以获得已安装编译器的列表，或使用 "latest"。默认在有的情况下使用最新的MSVC。否则使用MinGW64。
```

---

### --jobs=N

原始参数名:

```
--jobs=N
```

中文参数名:

```
并行编译任务数=N
```

原始简介:

```
Specify the allowed number of parallel C compiler jobs. Defaults to the system
CPU count.
```

中文简介:

```
指定允许使用的并行C编译器任务数。默认为系统CPU数。
```

---

### --lto=choice

原始参数名:

```
--lto=choice
```

中文参数名:

```
链接时间优化=选择
```

原始简介:

```
Use link time optimizations (MSVC, gcc, clang). Allowed values are "yes", "no",
and "auto" (when it's known to work). Defaults to "auto".
```

中文简介:

```
使用链接时间优化（MSVC、gcc、clang）允许的值有 "yes"（是）、"no"（否）和 "auto"（自动）(已知可用)。默认为 "auto"。
```

---

### --static-libpython=choice

原始参数名:

```
--static-libpython=choice
```

中文参数名:

```
使用Python的静态链接库=选择
```

原始简介:

```
Use static link library of Python. Allowed values are "yes", "no", and "auto"
(when it's known to work). Defaults to "auto".
```

中文简介:

```
使用Python的静态链接库。允许的值有 "yes"（是）、"no"（否）和 "auto"（自动）(已知可用)。默认为 "auto"。
```

---

---

## Cache Control(缓存控制)

---

### --disable-cache=DISABLED_CACHES

原始参数名:

```
--disable-cache=DISABLED_CACHES
```

中文参数名:

```
禁用缓存=已禁用缓存
```

原始简介:

```
Disable selected caches, specify "all" for all cached. Currently allowed values
are: "all","ccache","bytecode","dll-dependencies". can be given multiple times
or with comma separated values. Default none.
```

中文简介:

```
禁用选定的缓存，设置"all"则为所有缓存。当前允许的值有："all(全部)","ccache","bytecode(字节码","dll-dependencies(dll依赖项)"。
可以多次给出或使用逗号分隔给定的值。默认为无。
```

---

### --clean-cache=CLEAN_CACHES

原始参数名:

```
--clean-cache=CLEAN_CACHES
```

中文参数名:

```
清理缓存=要清理的缓存
```

原始简介:

```
Clean the given caches before executing, specify "all" for all cached.
Currently allowed values are: "all","ccache","bytecode","dll-dependencies". can
be given multiple times or with comma separated values. Default none.
```

中文简介:

```
在执行前清理给定缓存，设置"all"则为所有缓存。当前允许的值有：
"all(全部)","ccache","bytecode(字节码)","dll-dependencies(dll依赖项)"。
可以多次给出或使用逗号分隔给定的值。默认为无。
```

---

### --disable-bytecode-cache

原始参数名:

```
--disable-bytecode-cache
```

中文参数名:

```
禁用字节码缓存
```

原始简介:

```
Do not reuse dependency analysis results for modules, esp. from standard
library, that are included as bytecode. Same as --disable-cache=bytecode.
```

中文简介:

```
不要重复使用模块的依赖分析结果，尤其是来自标准库的模块，这些模块会被包含为字节码。与--disable-cache=bytecode效果相同。
```

---

### --disable-ccache

原始参数名:

```
--disable-ccache
```

中文参数名:

```
禁用ccache
```

原始简介:

```
Do not attempt to use ccache (gcc, clang, etc.) or clcache (MSVC, clangcl).
Same as --disable-cache=ccache.
```

中文简介:

```
不要尝试使用ccache(gcc,clang等)或clcache(MSVC,clangcl)。与--disable-cache=ccache效果相同。
```

---

### --disable-dll-dependency-cache

原始参数名:

```
--disable-dll-dependency-cache
```

中文参数名:

```
禁用dll依赖项缓存
```

原始简介:

```
Disable the dependency walker cache. Will result in much longer times to create
the distribution folder, but might be used in case the cache is suspect to cause
errors. Same as --disable-cache=dll-dependencies.
```

中文简介:

```
禁用依赖项分析器缓存。这将导致创建分发文件夹的时间大大延长，但如果怀疑缓存会导致错误，则可以使用它。
与--disable-cache=dll-dependencies效果相同。
```

---

### --force-dll-dependency-cache-update

原始参数名:

```
--force-dll-dependency-cache-update
```

中文参数名:

```
强制dll依赖项缓存更新
```

原始简介:

```
For an update of the dependency walker cache. Will result in much longer times
to create the distribution folder, but might be used in case the cache is
suspect to cause errors or known to need an update.
```

中文简介:

```
用于更新依赖分析器缓存。这将导致创建分发文件夹的时间大大延长，但如果怀疑缓存会导致错误或缓存需要更新，则可以使用它。
```

---

---

## PGO compilation choices(PGO(配置文件引导优化)编译选项)

---

### --pgo

原始参数名:

```
--pgo
```

中文参数名:

```
配置文件引导优化
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
通过先进行分析，然后使用结果来反馈到C编译中，启用C级别的配置文件引导优化（PGO）。
注意：这是实验性的，还不能与Nuitka的独立模式一起使用。默认关闭。
```

---

### --pgo-args=PGO_ARGS

原始参数名:

```
--pgo-args=PGO_ARGS
```

中文参数名:

```
配置文件引导优化参数=配置文件引导优化参数
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

## Tracing features(跟踪功能)

---

### --report=REPORT_FILENAME

原始参数名:

```
--report=REPORT_FILENAME
```

中文参数名:

```
报告=报告文件名
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
在XML输出文件中报告模块、数据文件、编译、插件等详细信息。这对于报告问题也非常有用。
例如，这些报告可以用于使用’–create-environment-from-report’轻松重建环境，但报告包含大量信息。默认关闭。


```

---

### --report-diffable

原始参数名:

```
--report-diffable
```

中文参数名:

```
报告差异
```

原始简介:

```
Report data in diffable form, i.e. no timing or memory usage values that vary
from run to run. Default is off.
```

中文简介:

```
以可比较的方式报告数据，即没有随着运行而变化的时间或内存使用值。默认关闭。
```

---

### --report-user-provided=KEY_VALUE

原始参数名:

```
--report-user-provided=KEY_VALUE
```

中文参数名:

```
报告用户所提供值=键值
```

原始简介:

```
Report data from you. This can be given multiple times and be anything in
'key=value' form, where key should be an identifier, e.g. use '--report-user-
provided=pipenv-lock-hash=64a5e4' to track some input values. Default is empty.
```

中文简介:

```
报告来自您的数据。这可以多次给出，并且可以是任何形式的"key=value"，其中key应该是一个标识符，
例如使用"--report-user-provided=pipenv-lock-hash=64a5e4"来跟踪一些输入值。默认为空。
```

---

### --report-template=REPORT_DESC

原始参数名:

```
--report-template=REPORT_DESC
```

中文参数名:

```
报告模板=报告描述
```

原始简介:

```
Report via template. Provide template and output filename
"template.rst.j2:output.rst". For built-in templates, check the User Manual for
what these are. Can be given multiple times. Default is empty.
```

中文简介:

```
通过模板报告。需要提供模板和输出文件名"template.rst.j2:output.rst"。对于内置模板，请查看用户手册。
可以多次给出。默认为空。
```

---

### --quiet

原始参数名:

```
--quiet
```

中文参数名:

```
静默模式 
```

原始简介:

```
Disable all information outputs, but show warnings. Defaults to off.
```

中文简介:

```
禁止所有信息输出，但显示警告。默认关闭。
```

---

### --show-scons

原始参数名:

```
--show-scons
```

中文参数名:

```
显示scons
```

原始简介:

```
Run the C building backend Scons with verbose information, showing the executed
commands, detected compilers. Defaults to off.
```

中文简介:

```
运行C构建后端Scons，显示执行的命令、检测到的编译器的详细信息。默认关闭。
```

---

### --no-progressbar

原始参数名:

```
--no-progressbar
```

中文参数名:

```
无进度条
```

原始简介:

```
Disable progress bars. Defaults to off.
```

中文简介:

```
禁用进度条。默认关闭。
```

---

### --show-progress

原始参数名:

```
--show-progress
```

中文参数名:

```
显示进度
```

原始简介:

```
Obsolete: Provide progress information and statistics. Disables normal progress
bar. Defaults to off.
```

中文简介:

```
过时: 提供进度信息和统计信息。禁用正常的进度条。默认关闭。
```

---

### --show-memory

原始参数名:

```
--show-memory
```

中文参数名:

```
显示内存
```

原始简介:

```
Provide memory information and statistics. Defaults to off.
```

中文简介:

```
提供内存信息和统计信息。默认关闭。
```

---

### --show-modules

原始参数名:

```
--show-modules
```

中文参数名:

```
显示模块
```

原始简介:

```
Provide information for included modules and DLLs Obsolete: You should use
'--report' file instead. Defaults to off.
```

中文简介:

```
过时: 您应该使用'--report'文件替代。提供包含的模块和DLL的信息。默认关闭。
```

---

### --show-modules-output=PATH

原始参数名:

```
--show-modules-output=PATH
```

中文参数名:

```
显示模块输出=路径
```

原始简介:

```
Where to output '--show-modules', should be a filename. Default is standard
output.
```

中文简介:

```
用于设定输出'--show-modules'的位置，应该是一个文件名。默认为标准输出。
```

---

### --verbose

原始参数名:

```
--verbose
```

中文参数名:

```
详细模式
```

原始简介:

```
Output details of actions taken, esp. in optimizations. Can become a lot.
Defaults to off.
```

中文简介:

```
输出采取的操作的详细信息，尤其是在优化过程中可能会大量输出。默认关闭。
```

---

### --verbose-output=PATH

原始参数名:

```
--verbose-output=PATH
```

中文参数名:

```
详细模式输出=路径
```

原始简介:

```
Where to output from '--verbose', should be a filename. Default is standard
output.
```

中文简介:

```
用于设定输出'--verbose'的位置，应该是一个文件名。默认为标准输出。
```

---

---

## General OS controls(通用操作系统控制)

---

### --disable-console

原始参数名:

```
--disable-console
```

中文参数名:

```
禁用控制台
```

原始简介:

```
When compiling for Windows or macOS, disable the console window and create a
GUI application. Defaults to off.
```

中文简介:

```
在为Windows或macOS编译时，禁用控制台窗口并创建为一个GUI应用程序。默认关闭。
```

---

### --enable-console

原始参数名:

```
--enable-console
```

中文参数名:

```
启用控制台
```

原始简介:

```
When compiling for Windows or macOS, enable the console window and create a
console application. This disables hints from certain modules, e.g. "PySide"
that suggest to disable it. Defaults to true.
```

中文简介:

```
在为Windows或macOS编译时，启用控制台窗口并创建一个控制台应用程序。
这将禁用来自某些模块的提示，例如"PySide"会建议禁用它。默认启用。
```

---

### --force-stdout-spec=FORCE_STDOUT_SPEC

原始参数名:

```
--force-stdout-spec=FORCE_STDOUT_SPEC
```

中文参数名:

```
强制标准输出规范=强制标准输出规范
```

原始简介:

```
Force standard output of the program to go to this location. Useful for
programs with disabled console and programs using the Windows Services Plugin of
Nuitka commercial. Defaults to not active, use e.g. '%PROGRAM_BASE%.out.txt',
i.e. file near your program, check User Manual for full list of available
values.
```

中文简介:

```
强制程序的标准输出输出到这个位置。对于禁用控制台的程序和使用Nuitka商业版的Windows服务插件的程序非常有用。默认不激活，
例如使用'%PROGRAM_BASE%.out.txt'，也就是程序目录附近的文件，查看用户手册以获取可用值的完整列表。
```

---

### --force-stderr-spec=FORCE_STDERR_SPEC

原始参数名:

```
--force-stderr-spec=FORCE_STDERR_SPEC
```

中文参数名:

```
强制标准错误规范=强制标准错误规范
```

原始简介:

```
Force standard error of the program to go to this location. Useful for programs
with disabled console and programs using the Windows Services Plugin of Nuitka
commercial. Defaults to not active, use e.g. '%PROGRAM_BASE%.err.txt', i.e. file
near your program, check User Manual for full list of available values.
```

中文简介:

```
强制程序的标准错误输出到这个位置。对于禁用控制台的程序和使用Nuitka商业版的Windows服务插件的程序非常有用。默认不激活，
例如使用'%PROGRAM_BASE%.err.txt'，也就是程序目录附近的文件，查看用户手册以获取可用值的完整列表。
```

---

---

## Windows specific controls(Windows特定控制)

---

### --windows-icon-from-ico=ICON_PATH

原始参数名:

```
--windows-icon-from-ico=ICON_PATH
```

中文参数名:

```
windows图标(ico文件)=图标路径
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
添加可执行文件的图标。可以多次给出不同分辨率或者包含多个图标的文件。在选择包含多个图标的文件时，
您也可以使用#<n>后缀来指定要包含的特定图标并忽略其他所有的图标，其中n是从1开始的整数索引
```

---

### --windows-icon-from-exe=ICON_EXE_PATH

原始参数名:

```
--windows-icon-from-exe=ICON_EXE_PATH
```

中文参数名:

```
windows图标(exe文件)=图标exe路径
```

原始简介:

```
Copy executable icons from this existing executable (Windows only).
```

中文简介:

```
复制来自该可执行文件的图标(仅限Windows)。
```

---

### --onefile-windows-splash-screen-image=SPLASH_SCREEN_IMAGE

原始参数名:

```
--onefile-windows-splash-screen-image=SPLASH_SCREEN_IMAGE
```

中文参数名:

```
单文件Windows启动画面图像=启动画面图像
```

原始简介:

```
When compiling for Windows and onefile, show this while loading the
application. Defaults to off.
```

中文简介:

```
当编译为Windows下的单文件时，在加载应用程序时显示这个图像。默认关闭。
```

---

### --windows-uac-admin

原始参数名:

```
--windows-uac-admin
```

中文参数名:

```
请求Windows用户控制(UAC)管理员权限
```

原始简介:

```
Request Windows User Control, to grant admin rights on execution. (Windows
only). Defaults to off.
```

中文简介:

```
向Windows用户控制(UAC)请求在执行时授予管理员权限。(仅限Windows)。默认关闭。
```

---

### --windows-uac-uiaccess

原始参数名:

```
--windows-uac-uiaccess
```

中文参数名:

```
请求Windows用户控制（UAC）UI访问权限
```

原始简介:

```
Request Windows User Control, to enforce running from a few folders only,
remote desktop access. (Windows only). Defaults to off.
```

中文简介:

```
请求Windows用户控制权限(UAC)，用于强制在特定的几个文件夹中运行和远程桌面访问。(仅限Windows)。默认关闭。
```

---

---

## macOS specific controls(MacOS特定控制)

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
application. Currently experimental and incomplete. Currently this is the only
way to unlock disabling of console.Defaults to off.
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
now mandatory on macOS and cannot be disabled. Default "ad-hoc" if not given.
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

## Linux specific controls(Linux特定控制)

---

### --linux-icon=ICON_PATH

原始参数名:

```
--linux-icon=ICON_PATH
```

中文参数名:

```
Linux图标=图标路径
```

原始简介:

```
Add executable icon for onefile binary to use. Can be given only one time.
Defaults to Python icon if available.
```

中文简介:

```
为单文件二进制可执行文件添加图标。只能给出一次。如果可用，默认为Python图标。
```

---

---

## Binary Version Information(二进制版本信息)

---

### --company-name=COMPANY_NAME

原始参数名:

```
--company-name=COMPANY_NAME
```

中文参数名:

```
公司名称=公司名称
```

原始简介:

```
Name of the company to use in version information. Defaults to unused.
```

中文简介:

```
要在版本信息中使用的公司名称。默认为无。
```

---

### --product-name=PRODUCT_NAME

原始参数名:

```
--product-name=PRODUCT_NAME
```

中文参数名:

```
产品名称=产品名称
```

原始简介:

```
Name of the product to use in version information. Defaults to base filename of
the binary.
```

中文简介:

```
要在版本信息中使用的产品名称。默认为二进制文件的基本文件名。
```

---

### --file-version=FILE_VERSION

原始参数名:

```
--file-version=FILE_VERSION
```

中文参数名:

```
文件版本=文件版本
```

原始简介:

```
File version to use in version information. Must be a sequence of up to 4
numbers, e.g. 1.0 or 1.0.0.0, no more digits are allowed, no strings are
allowed. Defaults to unused.
```

中文简介:

```
要在版本信息中使用的文件版本。必须为一个最多4个数字的序列，例如1.0或1.0.0.0,不允许使用更多的数字或者使用字符串。默认为无。
```

---

### --product-version=PRODUCT_VERSION

原始参数名:

```
--product-version=PRODUCT_VERSION
```

中文参数名:

```
产品版本=产品版本
```

原始简介:

```
Product version to use in version information. Same rules as for file version.
Defaults to unused.
```

中文简介:

```
要在版本信息中使用的产品版本。必须为一个最多4个数字的序列，例如1.0或1.0.0.0, 不允许使用更多的数字或者使用字符串。默认为无。
```

---

### --file-description=FILE_DESCRIPTION

原始参数名:

```
--file-description=FILE_DESCRIPTION
```

中文参数名:

```
文件描述=文件描述
```

原始简介:

```
Description of the file used in version information. Windows only at this time.
Defaults to binary filename.
```

中文简介:

```
要在版本信息中使用的文件描述。目前仅限Windows。默认为二进制文件的文件名。
```

---

### --copyright=COPYRIGHT_TEXT

原始参数名:

```
--copyright=COPYRIGHT_TEXT
```

中文参数名:

```
版权=版权文本
```

原始简介:

```
Copyright used in version information. Windows only at this time. Defaults to
not present.
```

中文简介:

```
在版本信息中使用的版权信息。目前仅限Windows。默认为无。
```

---

### --trademarks=TRADEMARK_TEXT

原始参数名:

```
--trademarks=TRADEMARK_TEXT
```

中文参数名:

```
商标=商标文本
```

原始简介:

```
Trademark used in version information. Windows only at this time. Defaults to
not present.
```

中文简介:

```
要在版本信息中使用的商标。目前仅限Windows。默认为无。
```

---

---

## Plugin control(插件控制)

---

### --enable-plugins=PLUGIN_NAME

原始参数名:

```
--enable-plugins=PLUGIN_NAME
```

中文参数名:

```
启用插件=插件名称
```

原始简介:

```
Enabled plugins. Must be plug-in names. Use '--plugin- list' to query the full
list and exit. Default empty.
```

中文简介:

```
启用插件。必须为插件名称。使用'--plugin-list'查询完整列表并退出。默认为空。
```

---

### --disable-plugins=PLUGIN_NAME

原始参数名:

```
--disable-plugins=PLUGIN_NAME
```

中文参数名:

```
禁用插件=插件名称
```

原始简介:

```
Disabled plugins. Must be plug-in names. Use '-- plugin-list' to query the full
list and exit. Most standard plugins are not a good idea to disable. Default
empty.
```

中文简介:

```
禁用插件。必须为插件名称。使用'--plugin-list'查询完整列表并退出。大多数情况下禁用标准插件并不是一个好主意。默认为空。
```

---

### --plugin-no-detection

原始参数名:

```
--plugin-no-detection
```

中文参数名:

```
禁止插件检测
```

原始简介:

```
Plugins can detect if they might be used, and the you can disable the warning
via "--disable-plugin=plugin-that-warned", or you can use this option to
disable the mechanism entirely, which also speeds up compilation slightly of
course as this detection code is run in vain once you are certain of which
plugins to use. Defaults to off.
```

中文简介:

```
插件可以检测它们是否可能被使用，您可以通过"--disable-plugin=plugin-that-warned"禁用警告，
或者你可以使用这个选项来完全禁用该机制，当然，这也会稍微加快编译速度，因为一旦你确定了要使用的插件，
这个检测代码就会白白运行。默认关闭。
```

---

### --plugin-list

原始参数名:

```
--plugin-list
```

中文参数名:

```
插件列表
```

原始简介:

```
Show list of all available plugins and exit. Defaults to off.
```

中文简介:

```
显示所有可用插件的列表并退出。默认关闭。
```

---

### --user-plugin=PATH

原始参数名:

```
--user-plugin=PATH
```

中文参数名:

```
用户插件=路径
```

原始简介:

```
The file name of user plugin. Can be given multiple times. Default empty.
```

中文简介:

```
用户插件的文件名。可以多次给出。默认为空。
```

---

### --show-source-changes

原始参数名:

```
--show-source-changes
```

中文参数名:

```
显示源代码更改
```

原始简介:

```
Show source changes to original Python file content before compilation. Mostly
intended for developing plugins. Default False.
```

中文简介:

```
显示编译前对原始Python文件内容的源代码的更改。主要用于开发插件。默认关闭。
```

---

---

## Plugin options of 'anti-bloat'('反膨胀'插件选项)

---

### --show-anti-bloat-changes

原始参数名:

```
--show-anti-bloat-changes
```

中文参数名:

```
显示反膨胀更改
```

原始简介:

```
Annotate what changes are by the plugin done.
```

中文简介:

```
注释插件所做的更改。
```

---

### --noinclude-setuptools-mode=NOINCLUDE_SETUPTOOLS_MODE

原始参数名:

```
--noinclude-setuptools-mode=NOINCLUDE_SETUPTOOLS_MODE
```

中文参数名:

```
不包含setuptools模式=不包含setuptools模式
```

原始简介:

```
What to do if a 'setuptools' or import is encountered. This package can be big
with dependencies, and should definitely be avoided. Also handles
'setuptools_scm'.
```

中文简介:

```
遇到"setuptools"或"setuptools_scm"导入时的处理方式。这个包可能会有很多依赖而变得很大，应该尽量避免使用。
```

---

### --noinclude-pytest-mode=NOINCLUDE_PYTEST_MODE

原始参数名:

```
--noinclude-pytest-mode=NOINCLUDE_PYTEST_MODE
```

中文参数名:

```
不包含pytest模式=不包含pytest模式
```

原始简介:

```
What to do if a 'pytest' import is encountered. This package can be big with
dependencies, and should definitely be avoided. Also handles 'nose' imports.
```

中文简介:

```
遇到"pytest"或"nose"导入时的处理方式。这个包可能会有很多依赖而变得很大，应该尽量避免使用。
```

---

### --noinclude-unittest-mode=NOINCLUDE_UNITTEST_MODE

原始参数名:

```
--noinclude-unittest-mode=NOINCLUDE_UNITTEST_MODE
```

中文参数名:

```
不包含单元测试模式=不包含unittest模式
```

原始简介:

```
What to do if a unittest import is encountered. This package can be big with
dependencies, and should definitely be avoided.
```

中文简介:

```
遇到"unittest(单元测试)"导入时的处理方式。这个包可能会有很多依赖而变得很大，应该尽量避免使用。
```

---

### --noinclude-IPython-mode=NOINCLUDE_IPYTHON_MODE

原始参数名:

```
--noinclude-IPython-mode=NOINCLUDE_IPYTHON_MODE
```

中文参数名:

```
不包含IPython模式=不包含IPython模式
```

原始简介:

```
What to do if a IPython import is encountered. This package can be big with
dependencies, and should definitely be avoided.
```

中文简介:

```
遇到"IPython"导入时的处理方式。这个包可能会有很多依赖而变得很大，应该尽量避免使用。
```

---

### --noinclude-dask-mode=NOINCLUDE_DASK_MODE

原始参数名:

```
--noinclude-dask-mode=NOINCLUDE_DASK_MODE
```

中文参数名:

```
不包含dask模式=不包含dask模式
```

原始简介:

```
What to do if a 'dask' import is encountered. This package can be big with
dependencies, and should definitely be avoided.
```

中文简介:

```
遇到"dask"导入时的处理方式。这个包可能会有很多依赖而变得很大，应该尽量避免使用。
```

---

### --noinclude-numba-mode=NOINCLUDE_NUMBA_MODE

原始参数名:

```
--noinclude-numba-mode=NOINCLUDE_NUMBA_MODE
```

中文参数名:

```
不包含numba模式=不包含numba模式
```

原始简介:

```
What to do if a 'numba' import is encountered. This package can be big with
dependencies, and is currently not working for standalone. This package is big
with dependencies, and should definitely be avoided.
```

中文简介:

```
遇到"numba"导入时的处理方式。这个包可能会有很多依赖而变得很大，目前在独立模式下还不能正常工作。
这个包可能会有很多依赖而变得很大，应该尽量避免使用。
```

---

### --noinclude-default-mode=NOINCLUDE_DEFAULT_MODE

原始参数名:

```
--noinclude-default-mode=NOINCLUDE_DEFAULT_MODE
```

中文参数名:

```
不包含的默认模式=不包含的默认模式
```

原始简介:

```
This actually provides the default "warning" value for above options, and can
be used to turn all of these on.
```

中文简介:

```
这实际上为上面的选项提供了默认的"警告(warning)"值，并且可以用来打开上述所有选项。
```

---

### --noinclude-custom-mode=CUSTOM_CHOICES

原始参数名:

```
--noinclude-custom-mode=CUSTOM_CHOICES
```

中文参数名:

```
不包含自定义模式=自定义选项
```

原始简介:

```
What to do if a specific import is encountered. Format is module name, which
can and should be a top level package and then one choice, "error", "warning",
"nofollow", e.g. PyQt5:error.
```

中文简介:

```
遇到特定导入时的处理方式。格式为模块名称，可以并且应该是一个顶级包，接着是一个选项，"error", "warning", "nofollow"，
例如PyQt5:error。
```

---

---