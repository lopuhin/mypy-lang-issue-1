class A(object):
    def do(self):
        from package import do_b      # this gives an error
        # from package.b import do_b  # this works
        return do_b(self)
