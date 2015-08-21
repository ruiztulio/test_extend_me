import core
import imp
import glob
import os


if __name__ == '__main__':
    modules = {}
    for path in glob.glob('plugins/[!_]*.py'):
        name, ext = os.path.splitext(os.path.basename(path))
    modules[name] = imp.load_source(name, path)
    pre = core.PreEvent()
    pre.run()
    test = core.BaseTestClass()
    test.start()
    test.stop()
    post = core.PostEvent()
    post.run()
