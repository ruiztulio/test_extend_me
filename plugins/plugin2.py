""" This plugin overloads 2 classes from our fantastic core"""
import core


class CheckSome(core.PreEvent):
    def run(self):
        super(CheckSome, self).run()
        print "Running checks from Some"


class CheckPost(core.PostEvent):
    """ This could be dangerous, completely overloads the parent method """
    def run(self):
        print "Killing parent method"
