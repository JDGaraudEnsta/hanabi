.PHONY: help all module doc test clean distclean uninstall list

default: help

help:
	@echo "Available targets:"
	@echo "  module, install - build and install hanabi python3 module"
	@echo "  doc             - build the module's documentation"
	@echo "  all             - do all 3 previous targets"
	@echo "  clean           - remove compilation residual files"
	@echo "  distclean, uninstall - clean, then remove the module"


all: module doc


module:
	pip3 install -r requirements.txt
	pip3 install -e src

install: module

doc: README.html module
	cd doc && make html

clean:
	cd doc && make clean
	cd src && rm -rf build/ dist/ hanabi.egg-info/
	cd tests && rm -f *.log autosave.py *~

distclean: clean
	-pip3 uninstall -y hanabi
	rm -f README.html

uninstall: distclean


%.html: %.md
	-pandoc -s --toc $< --css=./doc/github-pandoc.css -o $@

# Funny rule, that lists all available targets
list:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$' | xargs
# Could also use bash_completion:
#  sed -nrf <(_make_target_extract_script --) Makefile
