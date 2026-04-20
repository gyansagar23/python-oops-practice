class TestCase:
    department = "Modem Testing"

    def __init__(self,test_name, priority, status):
        self.test_name = test_name
        self.priority = priority
        self.status = status

    def run_test(self):
        print(f"Running {self.test_name} with priority {self.priority} and status {self.status}")
    
    def pass_test(self):
        self.status =  "Passed"
        print(f"{self.test_name} has {self.status}")

test_1 =TestCase("P2P Intra Freq HO", 1, "Not Run")
test_2 = TestCase("Full Buffer Peak Throughput", 2, "Not Run")

test_1.run_test()
test_1.pass_test()
test_2.run_test()
test_2.pass_test()


