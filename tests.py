import pytest

from main import BooksCollector


class TestBooksCollector:

    @pytest.mark.parametrize(
        'book_name, books_length',
        [
            ('Гордость и предубеждение', 1),
            ('Что делать, если ваш кот хочет вас убить, и прочее прочее ведь книга может быть очень длинной', 0),
        ]
    )
    def test_add_new_book(self, book_name, books_length):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        if books_length != 0:
            assert book_name in collector.get_books_genre()
        assert len(collector.get_books_genre()) == books_length

    def test_add_new_book_already_exists(self, ):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_success(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    def test_set_book_genre_book_is_not_exists(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби 2')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') is None

    @pytest.mark.parametrize(
        'name, genre',
        [
            ('Гордость и предубеждение и зомби', 'Фантастика'),
            ('Гордость и предубеждение и зомби 2', None),
        ],
    )
    def test_get_book_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_book_genre(name) == genre

    @pytest.mark.parametrize(
        'genre, book_list',
        [
            ('Фантастика', ['Гордость и предубеждение и зомби', 'Гордость и предубеждение и зомби 2']),
            ('Ужасы', []),
            ('Детективы', []),
            ('Мультфильмы', []),
            ('Комедии', ['Гордость и предубеждение и зомби 3']),
        ],
    )
    def test_get_books_with_specific_genre(self, genre, book_list):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби 2')
        collector.add_new_book('Гордость и предубеждение и зомби 3')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.set_book_genre('Гордость и предубеждение и зомби 2', 'Фантастика')
        collector.set_book_genre('Гордость и предубеждение и зомби 3', 'Комедии')
        collector.set_book_genre('Гордость и предубеждение и зомби 4', 'Мультфильмы')

        assert collector.get_books_with_specific_genre(genre) == book_list

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби 2')
        collector.add_new_book('Гордость и предубеждение и зомби 3')

        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.set_book_genre('Гордость и предубеждение и зомби 2', 'Ужасы')
        collector.set_book_genre('Гордость и предубеждение и зомби 3', 'Комедии')

        assert collector.get_books_for_children() == [
            'Гордость и предубеждение и зомби', 'Гордость и предубеждение и зомби 3',
        ]

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби 2')

        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби 2')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби 4')
        assert collector.get_list_of_favorites_books() == [
            'Гордость и предубеждение и зомби',
            'Гордость и предубеждение и зомби 2',
        ]

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')

        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == [
            'Гордость и предубеждение и зомби',
        ]
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_book_is_not_exist(self):
        collector = BooksCollector()

        assert collector.get_list_of_favorites_books() == []
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == []
