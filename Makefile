default: help

help:
	@echo "Available targets:"
	@echo "  module - build and install hanabi python3 module"
	@echo "  doc    - build the module's documentation"
	@echo "  tests  - run the non-regression and validation tests"
	@echo "  all    - do all 3 previous targets"
	@echo "  clean  - remove compilation residual files"
	@echo "  distclean - clean, then remove the module"


all: module doc


module:
	python3 setup.py install --user

doc: module
	cd doc && make html

clean:
	cd doc && make clean
	rm -rf build/ dist/ hanabi.egg-info/

distclean: clean
	pip3 uninstall -y hanabi
uninstall: distclean
