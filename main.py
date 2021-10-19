import argparse
import logging
import sys
import feedparser
from utils.entry import Entry
from utils.csv_parser import WriteIntoCSV

class RSSFeedParser():
    def __init__(self, feed_url, title_node):
        self._feed_url = feed_url
        self._title_node = title_node
        self._news_feed = feedparser.parse(self._feed_url)

    def generate_csv(self, file_name, header):
        entries = self.__return_all_entries()
        csv_writer = WriteIntoCSV(file_name, header)
        csv_writer.write(entries)

    def __return_all_entries(self):
        entries = self._news_feed.entries
        entry_objects = []
        for entry in entries:
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
        return entry_objects


if __name__ == '__main__':

    # Initialise logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Parse command line arguements
    parser = argparse.ArgumentParser()
    parser.add_argument('--title_node', help='provide the title node to parse here', default='Top stories')
    parser.add_argument('--feed_url', help='provide the RSS feed url here',
                        default='https://www.europarl.europa.eu/rss/doc/top-stories/en.xml')
    parser.add_argument('--output', help='provide the csv file with path here', default='output.csv')
    args = parser.parse_args()
    logger.info(f'Parsing{args.title_node} from {args.feed_url}')

    rss_feed_parser = RSSFeedParser(title_node=args.title_node, feed_url=args.feed_url)
    rss_feed_parser.generate_csv(args.output, ['Title', 'Link', 'Summary', 'Source', 'Tags', 'Published'])
