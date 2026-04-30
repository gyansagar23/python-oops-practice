# Build this inheritance structure:

# Parent: TestCase
# (test_name, priority, status)
# Methods: run_test(), pass_test()

# Child: PerformanceTestCase(TestCase)
# New attributes: throughput, latency
# New method: check_kpi()
# Override: run_test() — add throughput info

# Grandchild: FiveGTestCase(PerformanceTestCase)  
# New attribute: band, numerology
# New method: show_5g_config()

# Create objects and test all methods!

class TestCase:
    department = "Modem Testing"

    def __init__(self,test_name, priority, status):
        self.test_name= test_name
        self.priority = priority
        self.status = status
    def run_test(self):
        print(f"Running {self.test_name} with priority: {self.priority} and status: {self.status}")
    def pass_test(self):
        self.status = "Passed"
        print(f"{self.test_name} has {self.status}")

class PerformanceTestCase(TestCase):
    def __init__(self, test_name, priority, status, throughput, latency):
        super().__init__(test_name, priority, status)
        self.throughput = throughput
        self.latency = latency
    def run_test(self):
        super().run_test()
        print(f"throughput {self.throughput} and latency {self.latency}")
    def check_kpi(self):
        print(f"{self.test_name} has throughput {self.throughput} and latency {self.latency}")

class FiveGTestCase(PerformanceTestCase):
    def __init__(self, test_name, priority, status, throughput, latency, band, numerology):
        super().__init__(test_name, priority, status, throughput, latency)
        self.band = band
        self.numerology = numerology
    def show_5g_config(self):
        print(f"{self.test_name} is on band {self.band} with numerology {self.numerology}")

test_1 = TestCase ("P2P Inter Freq HO", 1, "Not Run")
test_1.run_test()
test_1.pass_test()
test_2 = PerformanceTestCase("Full Buffer Peak Throughput", 1, "Not Run", "1.5 Gbps", "40ms")
test_2.run_test()
test_2.check_kpi()
test_3 = FiveGTestCase("Idle Mode MO Pings", 2, "Not Run", "100 Kbps", "20ms", "n78", "30KHz SCS")
test_3.run_test()
test_3.check_kpi()
test_3.show_5g_config()