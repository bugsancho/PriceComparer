from sqlalchemy.orm import sessionmaker
from PriceComparer.persistance.models.product_offer import ProductOffer
from PriceComparer.persistance.database import db_connect


class DatabaseSaverPipeline(object):
    """Livingsocial pipeline for storing scraped items in the database"""

    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        """
        self.engine = db_connect()
        self.session_factory = sessionmaker(bind=self.engine)

    def process_item(self, item, spider):
        """Save offers in the database.

        This method is called for every item pipeline component.

        """
        session = self.session_factory()
        deal = ProductOffer(**item)

        try:
            session.add(deal)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
            self.engine.dispose()

        return item
