Install::

    $ git clone git@github.com:lopuhin/mypy-lang-issue-1.git
    $ cd mypy-lang-issue-1
    $ pip3 install -e .

Reproduce::

    $ mypy --silent-imports --check-untyped-defs package
    package/a.py: note: In function "do":
    package/a.py:3: error: Module 'package' has no attribute 'do_b'
    package/a.py:5: error: Name 'do_b' is not defined

If we change imports in ``package/a.py``::

	--- a/package/a.py
	+++ b/package/a.py
	@@ -1,5 +1,5 @@
	class A(object):
		def do(self):
	-        from package import do_b      # this gives an error
	-        # from package.b import do_b  # this works
	+        # from package import do_b      # this gives an error
	+        from package.b import do_b  # this works
			return do_b(self)

Then ``mypy --silent-imports --check-untyped-defs package`` succeeds.

