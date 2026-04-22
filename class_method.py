# Build TestCase class with ALL 3 method types:

# 1. Regular method: run_test()
#    → prints test_name + status

# 2. Class method: from_string()
#    → create TestCase from "P2P HO-1-Not Run"

# 3. Static method: is_critical()
#    → returns True if priority == 1

# Test all 3 methods!

class TestCase:
    department = "Modem testing"

    def __init__(self,test_name, priority, status):
        self.test_name = test_name
        self.priority = priority
        self.status = status

    @classmethod
    def from_string(cls, test_string):
        test_name, priority, status = test_string.split("-")
        return cls(test_name, int(priority), status)
    @staticmethod
    def is_critical(priority):
        return True if priority == 1 else False
    
test_1 = TestCase("P2P Intra Freq HO", 1, "Not Run")
print(test_1.test_name)
print(test_1.is_critical(test_1.priority))
test_2 = TestCase("Full Buffer Peak Throughput", 2, "Not run")
print(test_2.test_name)
print(test_2.is_critical(test_2.priority))
test_3 = TestCase.from_string("Idle Mode mobility-1-Not run")
print(test_3.test_name)
print(test_3.priority)
print(test_3.is_critical(test_3.priority))

    
    