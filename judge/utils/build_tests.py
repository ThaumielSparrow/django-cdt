from __future__ import absolute_import
import pkgutil
import importlib
import unittest

from utils.lazy_property import multi_lazy_properties


class Package():
    """
    The package class, represents the packages.
    """
    def __init__(self, package_name):
        self._package_name = package_name

    @multi_lazy_properties('submodule_names')
    def submodule_names(self):
        pass

    @submodule_names.add
    def subpackage_names(self):
        pass

    @submodule_names.function
    def get_submodules_and_subpackages(self):
        """
        Evaluation method for multiple lazy properties submodules and'
        subpackages.

        @return (list, list) submodules name list and subpackages name list
        """
        # get submodules and subpackages
        modules_packages_list = list(pkgutil.iter_modules([ _to_path(
                                                    self._package_name)] ))

        # get submodule names
        submodules = map(self._build_submodule_name,
                    filter(lambda m: not m.ispkg and not m.name == 'tests',
                           modules_packages_list))

        # get subpackage names
        subpackages = map(self._build_submodule_name,
                    filter(lambda m: m.ispkg, modules_packages_list))

        return list(submodules), list(subpackages)

    def _build_submodule_name(self, module_info):
        if module_info.module_finder.path == '.':
            return module_info.name
        return _to_name(module_info.module_finder.path + '.' +
                                                            module_info.name)


def _get_tests(module_names):
    """
    Return list of TestCase of all given modules.

    @param list module_names: names of modules
    @return list TestCase of modules in module_names
    """
    return [ unittest.TestLoader().loadTestsFromModule(
                                        importlib.import_module(module_name)) \
                                            for module_name in module_names ]

def _get_test_suites(package_names):
    """
    Return list of TestSuite of all given packges.

    @param list package_names: names of packages
    @return list TestSuite of packages in package_names
    """
    return [ importlib.import_module(package_test_module).test_suite() \
             for package_test_module in map(lambda p: p + '.tests',
                                            package_names) ]

def _to_path(string):
    """
    Process the string as package path.

    @param string: raw string
    @return string package path
    """
    return string.replace('.', '/')

def _to_name(string):
    """
    Process the string as module name.

    @param string: raw string
    @return string module name
    """
    return string.replace('/', '.')

def build_test_suite(package):
    """
    Build and return the test suite for the given package.

    @param Package package: package to be tested
    @return TestSuite test suite for the package
    """
    # build test suite with subpackages' test suites
    test_suite = unittest.TestSuite(_get_test_suites(package.subpackage_names))

    # add test cases from submodules
    [ test_suite.addTest(test) for test in _get_tests(package.submodule_names) ]

    return test_suite

