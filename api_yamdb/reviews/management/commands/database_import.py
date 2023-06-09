import logging
from csv import DictReader

from django.core.management import BaseCommand
from reviews.models import Category, Comment, Genre, GenreTitle, Review, Title

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO
)

ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the child data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""

LIST_OF_TABLES = [Category, Genre, Title, GenreTitle, Review, Comment]


class Command(BaseCommand):
    help = 'Loads data from children.csv'

    def handle(self, *args, **options):
        for tables in LIST_OF_TABLES:
            if tables.objects.exists():
                logging.warning('data already loaded...exiting.')
                raise Exception(ALREDY_LOADED_ERROR_MESSAGE)

        logging.info('Loading - data into a table - Category')
        for row in DictReader(open('static/data/category.csv')):
            child = Category(id=row['id'], name=row['name'], slug=row['slug'])
            child.save()
        logging.info('Successfully - loading data into table - Category')

        logging.info('Loading - data into a table - Genre')
        for row in DictReader(open('static/data/genre.csv')):
            child = Genre(id=row['id'], name=row['name'], slug=row['slug'])
            child.save()
        logging.info('Successfully - loading data into table - Genre')

        logging.info('Loading - data into a table - Title')
        for row in DictReader(open('static/data/titles.csv')):
            child = Title(
                id=row['id'],
                name=row['name'],
                year=row['year'],
                category=row['category'],
            )
            child.save()
        logging.info('Successfully - loading data into table - Title')

        logging.info('Loading - data into a table GenreTitle')
        for row in DictReader(open('static/data/genre_title.csv')):
            child = GenreTitle(
                id=row['id'], title=row['title_id'], genre=row['genre_id']
            )
            child.save()
        logging.info('Successfully - loading data into table - GenreTitle')

        logging.info('Loading - data into a table - Review')
        for row in DictReader(open('static/data/review.csv')):
            child = Review(
                id=row['id'],
                title=row['title_id'],
                text=row['text'],
                author=row['author'],
                score=row['score'],
                pub_date=row['pub_date'],
            )
            child.save()
        logging.info('Successfully - loading data into table - Review')

        logging.info('Loading - data into a table - Comment')
        for row in DictReader(open('static/data/comments.csv')):
            child = Comment(
                id=row['id'],
                review=row['review_id'],
                text=row['text'],
                author=row['author'],
                pub_date=row['pub_date'],
            )
            child.save()
        logging.info('Successfully - loading data into table - Comment')
