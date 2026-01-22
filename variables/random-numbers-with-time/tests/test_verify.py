import os
import sys
import unittest

# Add the tests directory and challenge directory to path for imports
tests_dir = os.path.dirname(os.path.abspath(__file__))
challenge_dir = os.path.dirname(tests_dir)
sys.path.insert(0, tests_dir)
sys.path.insert(0, challenge_dir)

from base_test import BaseTestValidator
from paceCParser.data_classes import Variable

# Import verification functions from verify script
# We need to import them as a module
import importlib.util

verify_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "verify"
)
spec = importlib.util.spec_from_loader("verify_module", loader=None)
verify_module = importlib.util.module_from_spec(spec)

# Read and exec the verify file (skip the shebang and suid parts)
with open(verify_path, "r") as f:
    verify_code = f.read()

# Execute in module namespace, skipping the if __name__ == '__main__' block
exec(compile(verify_code, verify_path, "exec"), verify_module.__dict__)

check_libraries = verify_module.check_libraries
check_srand_time = verify_module.check_srand_time
check_num1 = verify_module.check_num1
check_num2 = verify_module.check_num2
check_print_statements = verify_module.check_print_statements


class TestCheckLibraries(BaseTestValidator):
    """Tests for the check_libraries function."""

    def test_success_all_libraries(self):
        """Test that all required libraries pass validation."""
        c_code = """#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    return 0;
}
"""
        filepath = self.create_temp_c_file(c_code)
        file_contents = self.parse_c_file(filepath)
        passed, error_msg = check_libraries(file_contents)
        self.assertTrue(passed)
        self.assertEqual(error_msg, "")

    def test_missing_stdio(self):
        """Test that missing stdio.h fails validation."""
        c_code = """#include <stdlib.h>
#include <time.h>

int main() {
    return 0;
}
"""
        filepath = self.create_temp_c_file(c_code)
        file_contents = self.parse_c_file(filepath)
        passed, error_msg = check_libraries(file_contents)
        self.assertFalse(passed)
        self.assertIn("stdio.h", error_msg)

    def test_missing_stdlib(self):
        """Test that missing stdlib.h fails validation."""
        c_code = """#include <stdio.h>
#include <time.h>

int main() {
    return 0;
}
"""
        filepath = self.create_temp_c_file(c_code)
        file_contents = self.parse_c_file(filepath)
        passed, error_msg = check_libraries(file_contents)
        self.assertFalse(passed)
        self.assertIn("stdlib.h", error_msg)

    def test_missing_time(self):
        """Test that missing time.h fails validation."""
        c_code = """#include <stdio.h>
#include <stdlib.h>

int main() {
    return 0;
}
"""
        filepath = self.create_temp_c_file(c_code)
        file_contents = self.parse_c_file(filepath)
        passed, error_msg = check_libraries(file_contents)
        self.assertFalse(passed)
        self.assertIn("time.h", error_msg)


class TestCheckSrandTime(BaseTestValidator):
    """Tests for the check_srand_time function."""

    def test_success_srand_time_null(self):
        """Test that srand(time(NULL)) passes validation."""
        c_code = """#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));
    return 0;
}
"""
        filepath = self.create_temp_c_file(c_code)
        main_contents = self.get_main_function_contents(filepath)
        passed, error_msg = check_srand_time(main_contents)
        self.assertTrue(passed)
        self.assertEqual(error_msg, "")

    def test_success_srand_time_zero(self):
        """Test that srand(time(0)) passes validation."""
        c_code = """#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(0));
    return 0;
}
"""
        filepath = self.create_temp_c_file(c_code)
        main_contents = self.get_main_function_contents(filepath)
        passed, error_msg = check_srand_time(main_contents)
        self.assertTrue(passed)
        self.assertEqual(error_msg, "")

    def test_missing_srand(self):
        """Test that missing srand fails validation."""
        c_code = """#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int x = rand();
    return 0;
}
"""
        filepath = self.create_temp_c_file(c_code)
        main_contents = self.get_main_function_contents(filepath)
        passed, error_msg = check_srand_time(main_contents)
        self.assertFalse(passed)
        self.assertIn("srand()", error_msg)

    def test_srand_with_fixed_seed(self):
        """Test that srand with a fixed seed (not time) fails validation."""
        c_code = """#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(42);
    return 0;
}
"""
        filepath = self.create_temp_c_file(c_code)
        main_contents = self.get_main_function_contents(filepath)
        passed, error_msg = check_srand_time(main_contents)
        self.assertFalse(passed)
        self.assertIn("time(NULL)", error_msg)


class TestCheckNum1(BaseTestValidator):
    """Tests for the check_num1 function."""

    def test_success_correct_rand_num1(self):
        """Test that correct rand_num1 passes validation."""
        c_code = """#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));
    int rand_num1 = rand() % (25 + 1);
    return 0;
}
"""
        filepath = self.create_temp_c_file(c_code)
        main_contents = self.get_main_function_contents(filepath)
        passed, error_msg = check_num1(main_contents)
        self.assertTrue(passed)
        self.assertEqual(error_msg, "")

    def test_success_no_spaces(self):
        """Test that rand_num1 without spaces passes validation."""
        c_code = """#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));
    int rand_num1 = rand()%(25+1);
    return 0;
}
"""
        filepath = self.create_temp_c_file(c_code)
        main_contents = self.get_main_function_contents(filepath)
        passed, error_msg = check_num1(main_contents)
        self.assertTrue(passed)
        self.assertEqual(error_msg, "")

    def test_missing_rand_num1(self):
        """Test that missing rand_num1 fails validation."""
        c_code = """#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));
    int x = rand() % (25 + 1);
    return 0;
}
"""
        filepath = self.create_temp_c_file(c_code)
        main_contents = self.get_main_function_contents(filepath)
        passed, error_msg = check_num1(main_contents)
        self.assertFalse(passed)
        self.assertIn("rand_num1", error_msg)

    def test_wrong_range_rand_num1(self):
        """Test that wrong range for rand_num1 fails validation."""
        c_code = """#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));
    int rand_num1 = rand() % (100 + 1);
    return 0;
}
"""
        filepath = self.create_temp_c_file(c_code)
        main_contents = self.get_main_function_contents(filepath)
        passed, error_msg = check_num1(main_contents)
        self.assertFalse(passed)
        self.assertIn("correct value", error_msg)


class TestCheckNum2(BaseTestValidator):
    """Tests for the check_num2 function."""

    def test_success_correct_rand_num2(self):
        """Test that correct rand_num2 passes validation."""
        c_code = """#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));
    int rand_num2 = rand() % (1000 + 1);
    return 0;
}
"""
        filepath = self.create_temp_c_file(c_code)
        main_contents = self.get_main_function_contents(filepath)
        passed, error_msg = check_num2(main_contents)
        self.assertTrue(passed)
        self.assertEqual(error_msg, "")

    def test_success_no_spaces(self):
        """Test that rand_num2 without spaces passes validation."""
        c_code = """#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));
    int rand_num2 = rand()%(1000+1);
    return 0;
}
"""
        filepath = self.create_temp_c_file(c_code)
        main_contents = self.get_main_function_contents(filepath)
        passed, error_msg = check_num2(main_contents)
        self.assertTrue(passed)
        self.assertEqual(error_msg, "")

    def test_missing_rand_num2(self):
        """Test that missing rand_num2 fails validation."""
        c_code = """#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));
    int y = rand() % (1000 + 1);
    return 0;
}
"""
        filepath = self.create_temp_c_file(c_code)
        main_contents = self.get_main_function_contents(filepath)
        passed, error_msg = check_num2(main_contents)
        self.assertFalse(passed)
        self.assertIn("rand_num2", error_msg)

    def test_wrong_range_rand_num2(self):
        """Test that wrong range for rand_num2 fails validation."""
        c_code = """#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));
    int rand_num2 = rand() % (500 + 1);
    return 0;
}
"""
        filepath = self.create_temp_c_file(c_code)
        main_contents = self.get_main_function_contents(filepath)
        passed, error_msg = check_num2(main_contents)
        self.assertFalse(passed)
        self.assertIn("correct value", error_msg)


class TestCheckPrintStatements(BaseTestValidator):
    """Tests for the check_print_statements function."""

    def test_success_correct_prints(self):
        """Test that correct print statements pass validation."""
        c_code = """#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));
    int rand_num1 = rand() % (25 + 1);
    int rand_num2 = rand() % (1000 + 1);
    printf("Random number (0-25): %d\\n", rand_num1);
    printf("Random number (0-1000): %d\\n", rand_num2);
    return 0;
}
"""
        filepath = self.create_temp_c_file(c_code)
        main_contents = self.get_main_function_contents(filepath)
        passed, error_msg = check_print_statements(main_contents)
        self.assertTrue(passed)
        self.assertEqual(error_msg, "")

    def test_success_no_space_after_comma(self):
        """Test that print statements without space after comma pass."""
        c_code = """#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));
    int rand_num1 = rand() % (25 + 1);
    int rand_num2 = rand() % (1000 + 1);
    printf("Random number (0-25): %d\\n",rand_num1);
    printf("Random number (0-1000): %d\\n",rand_num2);
    return 0;
}
"""
        filepath = self.create_temp_c_file(c_code)
        main_contents = self.get_main_function_contents(filepath)
        passed, error_msg = check_print_statements(main_contents)
        self.assertTrue(passed)
        self.assertEqual(error_msg, "")

    def test_missing_first_print(self):
        """Test that missing first print statement fails validation."""
        c_code = """#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));
    int rand_num1 = rand() % (25 + 1);
    int rand_num2 = rand() % (1000 + 1);
    printf("Random number (0-1000): %d\\n", rand_num2);
    return 0;
}
"""
        filepath = self.create_temp_c_file(c_code)
        main_contents = self.get_main_function_contents(filepath)
        passed, error_msg = check_print_statements(main_contents)
        self.assertFalse(passed)
        self.assertIn("first", error_msg)

    def test_missing_second_print(self):
        """Test that missing second print statement fails validation."""
        c_code = """#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));
    int rand_num1 = rand() % (25 + 1);
    int rand_num2 = rand() % (1000 + 1);
    printf("Random number (0-25): %d\\n", rand_num1);
    return 0;
}
"""
        filepath = self.create_temp_c_file(c_code)
        main_contents = self.get_main_function_contents(filepath)
        passed, error_msg = check_print_statements(main_contents)
        self.assertFalse(passed)
        self.assertIn("second", error_msg)

    def test_wrong_format_string(self):
        """Test that wrong format string fails validation."""
        c_code = """#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));
    int rand_num1 = rand() % (25 + 1);
    int rand_num2 = rand() % (1000 + 1);
    printf("Random: %d\\n", rand_num1);
    printf("Random: %d\\n", rand_num2);
    return 0;
}
"""
        filepath = self.create_temp_c_file(c_code)
        main_contents = self.get_main_function_contents(filepath)
        passed, _ = check_print_statements(main_contents)
        self.assertFalse(passed)


class TestFullSolution(BaseTestValidator):
    """Integration tests for complete solutions."""

    def test_complete_correct_solution(self):
        """Test that a complete correct solution passes all checks."""
        c_code = """#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));
    int rand_num1 = rand() % (25 + 1);
    int rand_num2 = rand() % (1000 + 1);
    printf("Random number (0-25): %d\\n", rand_num1);
    printf("Random number (0-1000): %d\\n", rand_num2);
    return 0;
}
"""
        filepath = self.create_temp_c_file(c_code)
        file_contents = self.parse_c_file(filepath)
        main_contents = self.get_main_function_contents(filepath)

        # Check all verification functions pass
        passed, _ = check_libraries(file_contents)
        self.assertTrue(passed, "Libraries check failed")

        passed, _ = check_srand_time(main_contents)
        self.assertTrue(passed, "srand(time(NULL)) check failed")

        passed, _ = check_num1(main_contents)
        self.assertTrue(passed, "rand_num1 check failed")

        passed, _ = check_num2(main_contents)
        self.assertTrue(passed, "rand_num2 check failed")

        passed, _ = check_print_statements(main_contents)
        self.assertTrue(passed, "Print statements check failed")

    def test_complete_solution_with_time_zero(self):
        """Test that a solution using time(0) instead of time(NULL) passes."""
        c_code = """#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(0));
    int rand_num1 = rand() % (25 + 1);
    int rand_num2 = rand() % (1000 + 1);
    printf("Random number (0-25): %d\\n", rand_num1);
    printf("Random number (0-1000): %d\\n", rand_num2);
    return 0;
}
"""
        filepath = self.create_temp_c_file(c_code)
        file_contents = self.parse_c_file(filepath)
        main_contents = self.get_main_function_contents(filepath)

        # Check all verification functions pass
        passed, _ = check_libraries(file_contents)
        self.assertTrue(passed, "Libraries check failed")

        passed, _ = check_srand_time(main_contents)
        self.assertTrue(passed, "srand(time(0)) check failed")

        passed, _ = check_num1(main_contents)
        self.assertTrue(passed, "rand_num1 check failed")

        passed, _ = check_num2(main_contents)
        self.assertTrue(passed, "rand_num2 check failed")

        passed, _ = check_print_statements(main_contents)
        self.assertTrue(passed, "Print statements check failed")


if __name__ == "__main__":
    unittest.main()
