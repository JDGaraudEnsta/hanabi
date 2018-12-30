.PHONY: help all module doc clean distclean uninstall list

default: help

help:
	@echo "Available targets:"
	@echo "  module - build and install hanabi python3 module"
	@echo "  doc    - build the module's documentation"
	@echo "  test   - run the non-regression and validation tests"
	@echo "  all    - do all 3 previous targets"
	@echo "  clean  - remove compilation residual files"
	@echo "  distclean, uninstall"
	@echo "         - clean, then remove the module"


all: module doc


module:
	cd src && python3 setup.py install --user

doc: README.html module
	cd doc && make html

clean:
	cd doc && make clean
	cd src && rm -rf build/ dist/ hanabi.egg-info/

distclean: clean
	-pip3 uninstall -y hanabi
	rm -f README.html

uninstall: distclean

tests:
	cd test && ./run_tests.sh
	@echo All tests are ok

%.html: %.md
	pandoc -s --toc $< --css=./github-pandoc.css -o $@

# Funny rule, that lists all available targets
list:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$' | xargs
# Could also use bash_completion:
#  sed -nrf <(_make_target_extract_script --) Makefile
