import core


class Plugin1(core.BaseTestClass):
    """
    This is a plugin thar overloads the start method and call the parent after executing it's loginc
    """
    __my_second_name = "This is the plugin"

    def start(self):
        print "Start overloaded"
        super(Plugin1, self).start()