import argparse
import logging
import sys
import feedparser
import yaml

from utils.entry import Entry
from utils.csv_parser import WriteIntoCSV

class RSSFeedParser():
    def __init__(self, feed_url, title_content):
        self._feed_url = feed_url
        self._title_content = title_content
        self._news_feed = feedparser.parse(self._feed_url)

    def generate_csv(self, file_name, header):
        logger.info('generating csv')
        entries = self.__return_all_entries()
        csv_writer = WriteIntoCSV(file_name, header)
        csv_writer.write(entries)

    def __return_all_entries(self):
        logger.info('parsing RSS feeds')
        entries = self._news_feed.entries
        entry_objects = []
        for entry in entries:
            if not (self._title_content) in entry.title:
                continue
            entry_object = Entry()
            entry_object.title = entry.title
            entry_object.link = entry.link
            entry_object.summary = entry.summary
            entry_object.source = entry.source.title

            tags = []
            for tag in entry.tags:
                tags.append(tag.term)
            entry_object.tags = tags
            entry_object.published = entry.published
            entry_objects.append(entry_object)
        logger.info(f'total {len(entry_objects)} sections are found')
        return entry_objects


if __name__ == '__main__':

    with open('config.yaml', 'r') as config_file:
        config = yaml.safe_load(config_file)

    header = config.get('csv_header').split('|')

    # Initialise logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Parse command line arguements
    parser = argparse.ArgumentParser()
    parser.add_argument('--title_content', help='provide the title content to parse here. based on this '
                                                'title content, the titles will be fetched', default='Top story')
    parser.add_argument('--feed_url', help='provide the RSS feed url here',
                        default='https://www.europarl.europa.eu/rss/doc/top-stories/en.xml')
    parser.add_argument('--output', help='provide the csv file with path here', default='output.csv')
    args = parser.parse_args()
    logger.info(f'parsing{args.title_content} from {args.feed_url}')

    rss_feed_parser = RSSFeedParser(title_content=args.title_content, feed_url=args.feed_url)
    rss_feed_parser.generate_csv(args.output, header)
