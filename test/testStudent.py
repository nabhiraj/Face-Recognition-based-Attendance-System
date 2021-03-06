import unittest
from students import Student

class TestStudent(unittest.TestCase):
    
    def setUp(self):
        self.name='nabhiraj'
        self.code=62
        self.img=None
        self.testobj=Student(self.code,self.name,self.img)
        
    def test_getName(self):
        print('student name')
        self.assertEqual(self.testobj.getName(),self.name)
    
    def test_getRollNo(self):
        print('studne roll')
        self.assertEqual(self.testobj.getRollNo(),self.code)
    
    def test_getImage(self):
        print('studnet image')
        self.assertEqual(self.testobj.getImage(),self.img)
        
if __name__ == '__main__':
    unittest.main()
    
    
