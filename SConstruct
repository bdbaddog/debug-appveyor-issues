if False:
    env=Environment(tools=['msvc', 'mslink', 'jar', 'javac', 'javah', 'swig'])

    import os
    for k in os.environ:
        print("%s->%s"%(k,os.environ[k]))

    print("SCONS PATH:%s"%env['ENV']['PATH'])

    print("SHLINK: %s"%env.subst('$SHLINK'))

    print("LINK:%s"%env.WhereIs('link.exe'))
else:
    env=Environment(tools=['msvc'], MSVS_VERSION='14.1')
    retval=env.Execute('devenv.com /build')
    print(f"retval: {retval}")
