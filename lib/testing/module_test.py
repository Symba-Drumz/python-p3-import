"""Test script to demonstrate absolute and relative imports."""

print("Running absolute import demonstration:")
import lib.absolute_package.package1.module2

print("\\nRunning relative import demonstration:")
import lib.relative_package.subpackage1.subpackage2.module2
