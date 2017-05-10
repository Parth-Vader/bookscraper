# Simple scraper for testing

When `scrapy crawl books` is done, the following is the output -

For the settings :
		
		
		'LOG_LEVEL': 'INFO',
		'LOGSTATS_INTERVAL': 1,
		'CLOSESPIDER_TIMEOUT': 10
		
		
		
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
		 

For the settings :
		
		
		'LOG_LEVEL': 'INFO',
		'LOGSTATS_INTERVAL': 6,
		'CLOSESPIDER_TIMEOUT': 60
		
		
		2017-05-10 10:54:27 [scrapy.core.engine] INFO: Spider opened
		2017-05-10 10:54:27 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
		2017-05-10 10:54:33 [scrapy.extensions.logstats] INFO: Crawled 144 pages (at 1440 pages/min), scraped 141 items (at 1410 items/min)
		2017-05-10 10:54:39 [scrapy.extensions.logstats] INFO: Crawled 204 pages (at 600 pages/min), scraped 202 items (at 610 items/min)
		2017-05-10 10:54:45 [scrapy.extensions.logstats] INFO: Crawled 256 pages (at 520 pages/min), scraped 253 items (at 510 items/min)
		2017-05-10 10:54:51 [scrapy.extensions.logstats] INFO: Crawled 325 pages (at 690 pages/min), scraped 324 items (at 710 items/min)
		2017-05-10 10:54:57 [scrapy.extensions.logstats] INFO: Crawled 391 pages (at 660 pages/min), scraped 387 items (at 630 items/min)
		2017-05-10 10:55:03 [scrapy.extensions.logstats] INFO: Crawled 457 pages (at 660 pages/min), scraped 454 items (at 670 items/min)
		2017-05-10 10:55:09 [scrapy.extensions.logstats] INFO: Crawled 523 pages (at 660 pages/min), scraped 521 items (at 670 items/min)
		2017-05-10 10:55:15 [scrapy.extensions.logstats] INFO: Crawled 588 pages (at 650 pages/min), scraped 587 items (at 660 items/min)
		2017-05-10 10:55:21 [scrapy.extensions.logstats] INFO: Crawled 659 pages (at 710 pages/min), scraped 656 items (at 690 items/min)
		2017-05-10 10:55:27 [scrapy.core.engine] INFO: Closing spider (closespider_timeout)
		2017-05-10 10:55:27 [scrapy.extensions.logstats] INFO: Crawled 717 pages (at 580 pages/min), scraped 716 items (at 600 items/min)
		2017-05-10 10:55:30 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
		
		{'downloader/request_bytes': 209615,
		 'downloader/request_count': 749,
		 'downloader/request_method_count/GET': 749,
		 'downloader/response_bytes': 3314472,
		 'downloader/response_count': 749,
		 'downloader/response_status_count/200': 748,
		 'downloader/response_status_count/404': 1,
		 'finish_reason': 'closespider_timeout',
		 'finish_time': datetime.datetime(2017, 5, 10, 5, 25, 30, 40324),
		 'item_scraped_count': 748,
		 'log_count/INFO': 17,
		 'response_received_count': 749,
		 'scheduler/dequeued': 748,
		 'scheduler/dequeued/memory': 748,
		 'scheduler/enqueued': 748,
		 'scheduler/enqueued/memory': 748,
		 'start_time': datetime.datetime(2017, 5, 10, 5, 24, 27, 85947)}
