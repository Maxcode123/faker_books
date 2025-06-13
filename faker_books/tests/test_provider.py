from unittest import TestCase

from faker import Faker

from faker_books import BookProvider
from faker_books._genres import genre_list
from faker_books._authors import author_list
from faker_books._titles import title_list
from faker_books._publishers import publisher_list


class TestBookProvider(TestCase):
    @classmethod
    def setUpClass(cls):
        fake = Faker()
        fake.add_provider(BookProvider)
        cls.fake = fake


class TestBookGenre(TestBookProvider):
    def test_is_str(self):
        self.assertIsInstance(self.fake.book_genre(), str)

    def test_is_not_empty(self):
        self.assertNotEqual(self.fake.book_genre(), "")

    def test_is_in_genre_list(self):
        self.assertIn(self.fake.book_genre(), genre_list)


class TestBookAuthor(TestBookProvider):
    def test_is_str(self):
        self.assertIsInstance(self.fake.book_author(), str)

    def test_is_not_empty(self):
        self.assertNotEqual(self.fake.book_author(), "")

    def test_is_in_author_list(self):
        self.assertIn(self.fake.book_author(), author_list)


class TestBookTitle(TestBookProvider):
    def test_is_str(self):
        self.assertIsInstance(self.fake.book_title(), str)

    def test_is_not_empty(self):
        self.assertNotEqual(self.fake.book_title(), "")

    def test_is_in_title_list(self):
        self.assertIn(self.fake.book_title(), title_list)


class TestBookPublisher(TestBookProvider):
    def test_is_str(self):
        self.assertIsInstance(self.fake.book_publisher(), str)

    def test_is_not_empty(self):
        self.assertNotEqual(self.fake.book_publisher(), "")

    def test_is_in_publisher_list(self):
        self.assertIn(self.fake.book_publisher(), publisher_list)
