# rss-feed-parser
RSS feed parser parse the given rss feed for parsing titles/items from an RSS feed into CSV. We have 2 utils module here. One is to parse the RSS feed (entry.py) and 
another one is to write the parsed feeds into csv file (csv_parser.py).


## How to

- Clone this repository into local
- Verify that python3.7 + is available in local 
- Navigate into rss-feed-parser root directory in local
- Run this command 'pip install -r requirements.txt' for installing the dependencies
- Once the installation is success you can run the script either one of the following formats
  - python main.py <all default values will be used here>
  - python main.py --title_content "Verification string for the title" --feed_url "RSS feed url" --output "Output csv file name with path"

## Additional feature

We can have an additional feature from this solution using '--title_content' parameter to the script. Whatever we are passing into the parameter, the parser
will check whether the title contains it or not. if it not contains that item/title section will be omitted. By default it will be having 'Top Story' in it to
fetch all top stories from the feed


## Future Expansion

_This solution can be expanded to support huge bulk of data using dataflow. We can convert all utils classes into DoFn classes
in the dataflow. Also we can fetch the RSS feed in the initial node in a parallel process. So the entire solution will work in 
distributed manner. Further we can host it in Google Cloud for well managed distributed processing_