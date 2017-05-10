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
		 
		 
## After moving the site to a local server, the following is the result for different results :

For the settings :
		
		
		'LOG_LEVEL': 'INFO',
		'LOGSTATS_INTERVAL': 6,
		'CLOSESPIDER_TIMEOUT': 60
		
		2017-05-10 11:01:32 [scrapy.core.engine] INFO: Spider opened
		2017-05-10 11:01:32 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
		2017-05-10 11:01:38 [scrapy.extensions.logstats] INFO: Crawled 159 pages (at 1590 pages/min), scraped 155 items (at 1550 items/min)
		2017-05-10 11:01:44 [scrapy.extensions.logstats] INFO: Crawled 316 pages (at 1570 pages/min), scraped 315 items (at 1600 items/min)
		2017-05-10 11:01:50 [scrapy.extensions.logstats] INFO: Crawled 474 pages (at 1580 pages/min), scraped 470 items (at 1550 items/min)
		2017-05-10 11:01:56 [scrapy.extensions.logstats] INFO: Crawled 632 pages (at 1580 pages/min), scraped 630 items (at 1600 items/min)
		2017-05-10 11:02:02 [scrapy.extensions.logstats] INFO: Crawled 795 pages (at 1630 pages/min), scraped 792 items (at 1620 items/min)
		2017-05-10 11:02:08 [scrapy.extensions.logstats] INFO: Crawled 942 pages (at 1470 pages/min), scraped 941 items (at 1490 items/min)
		2017-05-10 11:02:10 [scrapy.core.engine] INFO: Closing spider (finished)
		2017-05-10 11:02:10 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
		{'downloader/request_bytes': 278341,
		 'downloader/request_count': 1001,
		 'downloader/request_method_count/GET': 1001,
		 'downloader/response_bytes': 4402725,
		 'downloader/response_count': 1001,
		 'downloader/response_status_count/200': 1000,
		 'downloader/response_status_count/404': 1,
		 'finish_reason': 'finished',
		 'finish_time': datetime.datetime(2017, 5, 10, 5, 32, 10, 913137),
		 'item_scraped_count': 1000,
		 'log_count/INFO': 13,
		 'response_received_count': 1001,
		 'scheduler/dequeued': 1000,
		 'scheduler/dequeued/memory': 1000,
		 'scheduler/enqueued': 1000,
		 'scheduler/enqueued/memory': 1000,
		 'start_time': datetime.datetime(2017, 5, 10, 5, 31, 32, 679865)}
		 
		 
For the settings :
		
		
		'LOG_LEVEL': 'INFO',
		'LOGSTATS_INTERVAL': 1,
		'CLOSESPIDER_TIMEOUT': 10
		
		2017-05-10 11:04:08 [scrapy.core.engine] INFO: Spider opened
		2017-05-10 11:04:08 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
		2017-05-10 11:04:09 [scrapy.extensions.logstats] INFO: Crawled 1 pages (at 60 pages/min), scraped 0 items (at 0 items/min)
		2017-05-10 11:04:10 [scrapy.extensions.logstats] INFO: Crawled 7 pages (at 360 pages/min), scraped 6 items (at 360 items/min)
		2017-05-10 11:04:11 [scrapy.extensions.logstats] INFO: Crawled 22 pages (at 900 pages/min), scraped 18 items (at 720 items/min)
		2017-05-10 11:04:12 [scrapy.extensions.logstats] INFO: Crawled 31 pages (at 540 pages/min), scraped 29 items (at 660 items/min)
		2017-05-10 11:04:13 [scrapy.extensions.logstats] INFO: Crawled 41 pages (at 600 pages/min), scraped 38 items (at 540 items/min)
		2017-05-10 11:04:14 [scrapy.extensions.logstats] INFO: Crawled 46 pages (at 300 pages/min), scraped 45 items (at 420 items/min)
		2017-05-10 11:04:15 [scrapy.extensions.logstats] INFO: Crawled 54 pages (at 480 pages/min), scraped 51 items (at 360 items/min)
		2017-05-10 11:04:16 [scrapy.extensions.logstats] INFO: Crawled 58 pages (at 240 pages/min), scraped 57 items (at 360 items/min)
		2017-05-10 11:04:17 [scrapy.extensions.logstats] INFO: Crawled 67 pages (at 540 pages/min), scraped 66 items (at 540 items/min)
		2017-05-10 11:04:18 [scrapy.core.engine] INFO: Closing spider (closespider_timeout)
		2017-05-10 11:04:18 [scrapy.extensions.logstats] INFO: Crawled 78 pages (at 660 pages/min), scraped 75 items (at 540 items/min)
		2017-05-10 11:04:19 [scrapy.extensions.logstats] INFO: Crawled 81 pages (at 180 pages/min), scraped 80 items (at 300 items/min)
		2017-05-10 11:04:20 [scrapy.extensions.logstats] INFO: Crawled 90 pages (at 540 pages/min), scraped 88 items (at 480 items/min)
		2017-05-10 11:04:21 [scrapy.extensions.logstats] INFO: Crawled 98 pages (at 480 pages/min), scraped 95 items (at 420 items/min)
		2017-05-10 11:04:22 [scrapy.extensions.logstats] INFO: Crawled 107 pages (at 540 pages/min), scraped 106 items (at 660 items/min)
		2017-05-10 11:04:23 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
		{'downloader/request_bytes': 31347,
		 'downloader/request_count': 110,
		 'downloader/request_method_count/GET': 110,
		 'downloader/response_bytes': 477988,
		 'downloader/response_count': 110,
		 'downloader/response_status_count/200': 109,
		 'downloader/response_status_count/404': 1,
		 'finish_reason': 'closespider_timeout',
		 'finish_time': datetime.datetime(2017, 5, 10, 5, 34, 23, 237432),
		 'item_scraped_count': 109,
		 'log_count/INFO': 21,
		 'response_received_count': 110,
		 'scheduler/dequeued': 109,
		 'scheduler/dequeued/memory': 109,
		 'scheduler/enqueued': 109,
		 'scheduler/enqueued/memory': 109,
		 'start_time': datetime.datetime(2017, 5, 10, 5, 34, 8, 340710)}
		 
For the settings:


		LOGSTATS_INTERVAL = 3
		LOG_LEVEL = 'INFO'
		CLOSESPIDER_TIMEOUT = 30


		2017-05-10 11:07:32 [scrapy.core.engine] INFO: Spider opened
		2017-05-10 11:07:32 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
		2017-05-10 11:07:35 [scrapy.extensions.logstats] INFO: Crawled 4 pages (at 80 pages/min), scraped 3 items (at 60 items/min)
		2017-05-10 11:07:38 [scrapy.extensions.logstats] INFO: Crawled 19 pages (at 300 pages/min), scraped 17 items (at 280 items/min)
		2017-05-10 11:07:41 [scrapy.extensions.logstats] INFO: Crawled 38 pages (at 380 pages/min), scraped 37 items (at 400 items/min)
		2017-05-10 11:07:44 [scrapy.extensions.logstats] INFO: Crawled 64 pages (at 520 pages/min), scraped 63 items (at 520 items/min)
		2017-05-10 11:07:47 [scrapy.extensions.logstats] INFO: Crawled 90 pages (at 520 pages/min), scraped 89 items (at 520 items/min)
		2017-05-10 11:07:50 [scrapy.extensions.logstats] INFO: Crawled 122 pages (at 640 pages/min), scraped 120 items (at 620 items/min)
		2017-05-10 11:07:53 [scrapy.extensions.logstats] INFO: Crawled 148 pages (at 520 pages/min), scraped 145 items (at 500 items/min)
		2017-05-10 11:07:56 [scrapy.extensions.logstats] INFO: Crawled 187 pages (at 780 pages/min), scraped 184 items (at 780 items/min)
		2017-05-10 11:07:59 [scrapy.extensions.logstats] INFO: Crawled 219 pages (at 640 pages/min), scraped 217 items (at 660 items/min)
		2017-05-10 11:08:02 [scrapy.core.engine] INFO: Closing spider (closespider_timeout)
		2017-05-10 11:08:02 [scrapy.extensions.logstats] INFO: Crawled 251 pages (at 640 pages/min), scraped 249 items (at 640 items/min)
		2017-05-10 11:08:05 [scrapy.extensions.logstats] INFO: Crawled 279 pages (at 560 pages/min), scraped 278 items (at 580 items/min)
		2017-05-10 11:08:07 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
		{'downloader/request_bytes': 79631,
		 'downloader/request_count': 283,
		 'downloader/request_method_count/GET': 283,
		 'downloader/response_bytes': 1244980,
		 'downloader/response_count': 283,
		 'downloader/response_status_count/200': 282,
		 'downloader/response_status_count/404': 1,
		 'finish_reason': 'closespider_timeout',
		 'finish_time': datetime.datetime(2017, 5, 10, 5, 38, 7, 55279),
		 'item_scraped_count': 282,
		 'log_count/INFO': 18,
		 'response_received_count': 283,
		 'scheduler/dequeued': 282,
		 'scheduler/dequeued/memory': 282,
		 'scheduler/enqueued': 282,
		 'scheduler/enqueued/memory': 282,
		 'start_time': datetime.datetime(2017, 5, 10, 5, 37, 32, 585861)}

