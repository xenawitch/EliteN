# test_nftprism.py
"""
Tests for NFTPrism module.
"""

import unittest
from nftprism import NFTPrism

class TestNFTPrism(unittest.TestCase):
    """Test cases for NFTPrism class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NFTPrism()
        self.assertIsInstance(instance, NFTPrism)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NFTPrism()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
