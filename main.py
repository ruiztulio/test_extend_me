import core
import imp
import glob
import os


def load_plugins():
    modules = {}
    for path in glob.glob('plugins/[!_]*.py'):
        name, ext = os.path.splitext(os.path.basename(path))
        modules[name] = imp.load_source(name, path)
    return modules

if __name__ == '__main__':
    modules = load_plugins()
    pre = core.PreEvent()
    pre.run()
    test = core.BaseTestClass()
    test.start()
    test.stop()
    post = core.PostEvent()
    post.run()
