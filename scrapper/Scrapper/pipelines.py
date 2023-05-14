# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.exceptions import DropItem
from sqlalchemy.orm import sessionmaker
import sqlalchemy as sa

from .items import RecordItem
from .models import connect_db, create_table, Record


class SaveToSQLDatabasePipeline:

    def __init__(self):
        engine = connect_db()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item: RecordItem, spider):
        session = self.Session()

        record = Record(**item)
        try:
            session.add(record)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item


class DuplicatesSQLDatabasePipeline:
    def __init__(self):
        engine = connect_db()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        record_exists = session.execute(sa.select(Record).where(Record.url == item["url"])).scalar_one_or_none()
        session.close()
        if record_exists is not None:
            raise DropItem(f"Duplicate item found: {item['name']}.")
        return item

