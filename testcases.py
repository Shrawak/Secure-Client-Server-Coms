import unittest
import subprocess
import time
import sys

class TestAESEncryption(unittest.TestCase):
    def setUp(self):
        self.server = subprocess.Popen([sys.executable, 'server.py'])
        time.sleep(1)
        self.client = subprocess.Popen([sys.executable, 'client.py'],
                                       stdin=subprocess.PIPE,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)

    def tearDown(self):
        self.client.terminate()
        self.server.terminate()
    
    def test_encryption(self):
        self.client.stdin.write(b'Hello\n')
        self.client.stdin.flush()
        time.sleep(1)
        output = self.client.stdout.readline()
        self.assertEqual(output.strip(), b'Write your message: Server: Hello')
        
if __name__ == '__main__':
    unittest.main()