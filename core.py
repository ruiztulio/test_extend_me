""" Here, in the core we have the base classes that could be extended,
 for safety and our mental health won't allow to overload all classes using extend_me"""
from extend_me import Extensible


class BaseTestClass(Extensible):
    """ Dummy base class, just start and top something
    """
    __my_name = "Base class"

    def start(self):
        print "Starting my friend"

    def stop(self):
        print "Stopping all"


class PreEvent(Extensible):
    """ This class is used previous to the start
    """
    def run(self):
        print "Running pre event from base class"


class PostEvent(Extensible):
    """ Executes after stop, post even processing
    """
    def run(self):
        print "Running post event from base class"
