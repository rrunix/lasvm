PYTHON ?= python
CYTHON ?= cython
NOSETESTS ?= nosetests
DATADIR=$(HOME)/lasvm_data

# Compilation...

CYTHONSRC= $(wildcard lasvm/*.pyx lasvm/random/*.pyx)
CSRC= $(CYTHONSRC:.pyx=.cpp)

inplace: cython
	$(PYTHON) setup.py build_ext -i

cython: $(CSRC)

clean:
	rm -f lasvm/*.c lasvm/*.cpp lasvm/*.so lasvm/*.html lasvm/*.pyc

%.cpp: %.pyx
	$(CYTHON) --cplus $<

# Tests...
#
test-code: in
	$(NOSETESTS) -s lasvm

test-coverage:
	$(NOSETESTS) -s --with-coverage --cover-html --cover-html-dir=coverage \
	--cover-package=lasvm lasvm

test: test-code test-doc
