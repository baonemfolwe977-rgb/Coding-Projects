import unittest
import sys
import io
from contextlib import contextmanager
from Mfolwe_Baone_SectionE_F.py import Student, Gradebook

@contextmanager
def capture_output():
    """Helper function to capture stdout for testing"""
    new_out = io.StringIO()
    old_out = sys.stdout
    try:
        sys.stdout = new_out
        yield sys.stdout
    finally:
        sys.stdout = old_out

class TestStudent(unittest.TestCase):
    """Unit tests for the Student class"""
    
    def setUp(self):
        """Set up test cases"""
        self.student = Student("Test Student")

    def test_init(self):
        """Test student initialization"""
        self.assertEqual(self.student.name, "Test Student")
        self.assertEqual(len(self.student.grades), len(Gradebook.SUBJECTS))
        for subject in Gradebook.SUBJECTS:
            self.assertIn(subject, self.student.grades)
            self.assertEqual(self.student.grades[subject], [])

    def test_validate_grade(self):
        """Test grade validation"""
        # Valid grades
        self.assertEqual(Student.validate_grade("85"), (True, 85.0))
        self.assertEqual(Student.validate_grade("100"), (True, 100.0))
        self.assertEqual(Student.validate_grade("0"), (True, 0.0))
        
        # Invalid grades
        self.assertEqual(Student.validate_grade("101"), (False, None))
        self.assertEqual(Student.validate_grade("-1"), (False, None))
        self.assertEqual(Student.validate_grade("abc"), (False, None))

    def test_add_grade(self):
        """Test adding grades"""
        # Valid grade addition
        self.assertTrue(self.student.add_grade("Math", "85"))
        self.assertEqual(self.student.grades["Math"], [85.0])
        
        # Invalid grade
        self.assertFalse(self.student.add_grade("Math", "101"))
        self.assertEqual(self.student.grades["Math"], [85.0])
        
        # Invalid subject
        self.assertFalse(self.student.add_grade("Invalid", "85"))

    def test_calculate_average(self):
        """Test average calculation"""
        # No grades
        self.assertIsNone(self.student.calculate_average("Math"))
        
        # Single grade
        self.student.add_grade("Math", "85")
        self.assertEqual(self.student.calculate_average("Math"), 85.0)
        
        # Multiple grades
        self.student.add_grade("Math", "95")
        self.assertEqual(self.student.calculate_average("Math"), 90.0)

    def test_get_report(self):
        """Test report generation"""
        # Add some grades
        self.student.add_grade("Math", "85")
        self.student.add_grade("Math", "95")
        self.student.add_grade("English", "90")
        
        report = self.student.get_report()
        
        # Check Math grades and average
        self.assertEqual(report["Math"]["grades"], [85.0, 95.0])
        self.assertEqual(report["Math"]["average"], 90.0)
        
        # Check English grades and average
        self.assertEqual(report["English"]["grades"], [90.0])
        self.assertEqual(report["English"]["average"], 90.0)
        
        # Check Science (no grades)
        self.assertEqual(report["Science"]["grades"], [])
        self.assertEqual(report["Science"]["average"], "No grades yet")

class TestGradebook(unittest.TestCase):
    """Unit tests for the Gradebook class"""
    
    def setUp(self):
        """Set up test cases"""
        self.gradebook = Gradebook()

    def test_add_student(self):
        """Test adding students"""
        # Add new student
        self.assertTrue(self.gradebook.add_student("John"))
        self.assertIn("John", self.gradebook.students)
        
        # Try to add same student again
        self.assertFalse(self.gradebook.add_student("John"))

    def test_remove_student(self):
        """Test removing students"""
        # Add and then remove student
        self.gradebook.add_student("John")
        self.assertTrue(self.gradebook.remove_student("John"))
        self.assertNotIn("John", self.gradebook.students)
        
        # Try to remove non-existent student
        self.assertFalse(self.gradebook.remove_student("Jane"))

    def test_get_subject_grades(self):
        """Test retrieving subject grades"""
        # Add student with grades
        self.gradebook.add_student("John")
        student = self.gradebook.get_student("John")
        student.add_grade("Math", "85")
        student.add_grade("Math", "95")
        
        # Get grades for valid subject
        grades = self.gradebook.get_subject_grades("Math")
        self.assertEqual(grades["John"], [85.0, 95.0])
        
        # Try invalid subject
        self.assertIsNone(self.gradebook.get_subject_grades("Invalid"))

    def test_display_student_report(self):
        """Test student report display"""
        self.gradebook.add_student("John")
        student = self.gradebook.get_student("John")
        student.add_grade("Math", "85")
        student.add_grade("Math", "95")
        
        with capture_output() as output:
            self.gradebook.display_student_report(student.get_report(), "John")
            printed_output = output.getvalue()
            
        # Verify output contains expected information
        self.assertIn("Report Card for John", printed_output)
        self.assertIn("Math", printed_output)
        self.assertIn("85", printed_output)
        self.assertIn("95", printed_output)
        self.assertIn("90.00", printed_output)  # Average

class TestIntegration(unittest.TestCase):
    """Integration tests for the Grade Management System"""
    
    def setUp(self):
        """Set up test cases"""
        self.gradebook = Gradebook()

    def test_complete_workflow(self):
        """Test complete workflow of adding student, grades, and generating reports"""
        # Add student
        self.gradebook.add_student("John")
        
        # Add grades for multiple subjects
        student = self.gradebook.get_student("John")
        student.add_grade("Math", "85")
        student.add_grade("Math", "95")
        student.add_grade("English", "90")
        student.add_grade("Science", "88")
        
        # Get and verify subject grades
        math_grades = self.gradebook.get_subject_grades("Math")
        self.assertEqual(math_grades["John"], [85.0, 95.0])
        
        # Get and verify student report
        report = student.get_report()
        self.assertEqual(report["Math"]["average"], 90.0)
        self.assertEqual(report["English"]["average"], 90.0)
        self.assertEqual(report["Science"]["average"], 88.0)
        
        # Test removing student
        self.gradebook.remove_student("John")
        self.assertIsNone(self.gradebook.get_student("John"))

if __name__ == '__main__':
    unittest.main()