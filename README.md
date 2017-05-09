# Simple scraper for testing

When `scrapy crawl books` is done, the following is the output :


		2017-05-09 22:24:16 [scrapy.core.engine] INFO: Spider opened
		2017-05-09 22:24:16 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
		2017-05-09 22:24:17 [scrapy.extensions.logstats] INFO: Crawled 4 pages (at 240 pages/min), scraped 2 items (at 120 items/min)
		2017-05-09 22:24:18 [scrapy.extensions.logstats] INFO: Crawled 12 pages (at 480 pages/min), scraped 11 items (at 540 items/min)
		2017-05-09 22:24:19 [scrapy.extensions.logstats] INFO: Crawled 18 pages (at 360 pages/min), scraped 17 items (at 360 items/min)
		2017-05-09 22:24:20 [scrapy.extensions.logstats] INFO: Crawled 23 pages (at 300 pages/min), scraped 22 items (at 300 items/min)
		2017-05-09 22:24:21 [scrapy.extensions.logstats] INFO: Crawled 27 pages (at 240 pages/min), scraped 25 items (at 180 items/min)
		2017-05-09 22:24:22 [scrapy.extensions.logstats] INFO: Crawled 35 pages (at 480 pages/min), scraped 33 items (at 480 items/min)
		2017-05-09 22:24:23 [scrapy.extensions.logstats] INFO: Crawled 43 pages (at 480 pages/min), scraped 39 items (at 360 items/min)
		2017-05-09 22:24:24 [scrapy.extensions.logstats] INFO: Crawled 50 pages (at 420 pages/min), scraped 48 items (at 540 items/min)
		2017-05-09 22:24:25 [scrapy.extensions.logstats] INFO: Crawled 59 pages (at 540 pages/min), scraped 55 items (at 420 items/min)
		2017-05-09 22:24:26 [scrapy.core.engine] INFO: Closing spider (closespider_timeout)
		2017-05-09 22:24:26 [scrapy.extensions.logstats] INFO: Crawled 65 pages (at 360 pages/min), scraped 63 items (at 480 items/min)
		2017-05-09 22:24:27 [scrapy.extensions.logstats] INFO: Crawled 72 pages (at 420 pages/min), scraped 70 items (at 420 items/min)
		2017-05-09 22:24:28 [scrapy.extensions.logstats] INFO: Crawled 84 pages (at 720 pages/min), scraped 82 items (at 720 items/min)
		2017-05-09 22:24:29 [scrapy.extensions.logstats] INFO: Crawled 95 pages (at 660 pages/min), scraped 93 items (at 660 items/min)
		2017-05-09 22:24:29 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
		
		{'downloader/request_bytes': 27624,
		 'downloader/request_count': 97,
		 'downloader/request_method_count/GET': 97,
		 'downloader/response_bytes': 420221,
		 'downloader/response_count': 97,
		 'downloader/response_status_count/200': 96,
		 'downloader/response_status_count/404': 1,
		 'finish_reason': 'closespider_timeout',
		 'finish_time': datetime.datetime(2017, 5, 9, 16, 54, 29, 535048),
		 'item_scraped_count': 96,
		 'log_count/INFO': 20,
		 'response_received_count': 97,
		 'scheduler/dequeued': 96,
		 'scheduler/dequeued/memory': 96,
		 'scheduler/enqueued': 96,
		 'scheduler/enqueued/memory': 96,
		 'start_time': datetime.datetime(2017, 5, 9, 16, 54, 16, 5485)}
