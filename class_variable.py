# Challenge: 
# Create TestSuite class with:
# 1. Class variable: total_suites = 0
# 2. Class variable: lab = "RF Lab"
# 3. Instance variables: suite_name, test_count
# 4. Each new instance should increment total_suites
# 5. Create 3 instances
# 6. Prove class variable changes affect all instances
# 7. Prove instance variable overrides class variable
#    for ONLY that instance
class TestSuite:
    total_suites =0
    lab = "RF Lab"

    def __init__(self, suite_name, test_count):
        self.suite_name = suite_name
        self.test_count = test_count
        TestSuite.total_suites +=1

testsuite_1 = TestSuite("Mobility Tests", 5)
testsuite_2 = TestSuite("Idle Mode Mobility", 5)
testsuite_3 = TestSuite("full Buffer Peak Throughput", 10)

print(f"Total Number of Test Suites are {TestSuite.total_suites}")

TestSuite.total_suites = 10
print(f"Total Number of Test Suites are {TestSuite.total_suites}")

testsuite_1.total_suites =30
print(f"Total Number of Test Suites are {testsuite_1.total_suites}")


