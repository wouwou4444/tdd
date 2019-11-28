# Test Driven Development 

pytest -v

## Naming convention

Documentation available here : https://docs.pytest.org/en/latest/goodpractices.documentation 

* file name should start by test for automatic discovery or file name can be explicity passed on th ecommand line

* function name **must** start by test

* class names **must** start by Test

## how to execute

* pytest -v 

* pytest -v file_name

## test convention : assert

* use assert for most of test

## assert exception

    import pytest


    def f():
        raise SystemExit(1)


    def test_mytest():
        with pytest.raises(SystemExit):
            f()


# Markers

## warning 

## pytest.ini file : declare marker names

# Fixtures

## directive : @pytest.py

## builtin fixtures : tempfile

* tmpdir : https://docs.pytest.org/en/latest/builtin.html

## conftest.py : sharing fixtures 

## fixture scope

## parametrization and factories


