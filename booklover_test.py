import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        '''Add a book and test if it is in book_list'''
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_name, rating = "War of the Worlds", 4
        test_object.add_book(book_name, rating)
        book_names_lst = test_object.book_list.book_name.to_list()
        self.assertTrue(book_name in book_names_lst)

    def test_2_add_book(self):
        '''Add the same book twice. Test if it's in book_list only once.'''
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_name, rating = "War of the Worlds", 4
        test_object.add_book(book_name, rating)
        test_object.add_book(book_name, rating)
        reps_book_name = test_object.book_list[test_object.book_list.book_name == book_name].shape[0]
        self.assertEqual(1, reps_book_name)

    def test_3_has_read(self):
        '''Pass a book in the list and test the answer is True.'''
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_name, rating = "War of the Worlds", 4
        test_object.add_book(book_name, rating)
        self.assertTrue(test_object.has_read(book_name))

    def test_4_has_read(self):
        '''Pass a book NOT in the list and use assert False to test if the answer is True.'''
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_name, rating = "War of the Worlds", 4
        test_object.add_book(book_name, rating)
        self.assertFalse(test_object.has_read('Star Wars'))

    def test_5_num_books_read(self):
        '''Add some books to the list, and test num_books matches expected.'''
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("Mobidick", 4)
        test_object.add_book("El Quijote", 5)
        actual = test_object.num_books
        expected = 3
        self.assertEqual(actual, expected)

    def test_6_fav_books(self):
        '''Add some books with ratings to the list, making sure some of them have rating > 3. 
        Your test should check that the returned books have rating > 3.'''
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("Mars Attack", 2)
        test_object.add_book("Mobidick", 5)
        test_object.add_book("El Quijote", 5)
        expected = 3
        actual = test_object.fav_books()
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(verbosity=3)