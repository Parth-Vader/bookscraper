# Testing the stability of the benchmark

I am using the given spider on `nginx` server with the following settings:
    
    LOGSTATS_INTERVAL = 3
    LOG_LEVEL = 'INFO'
    CLOSESPIDER_TIMEOUT = 30
    
I used the total number of `pages crawled` and `items scraped` and multiplied it with `60/30 = 2` to get the average speed per minute.
After taking such data of 50 spiders, the graph obtained is as follows :

![Graph](https://github.com/Parth-Vader/bookscraper/blob/master/Stability/20170511033241.jpg)

The benchmark is fairly stable, with lower values in the middle. The average CPU usage was around `35-40%`.

The statistics for the data is as follows :

		Population size:50

		Mean (μ): 1590.8
		Median: 1672
		Modes: 1632 1718
		Lowest value: 1024
		Highest value: 1806
		Range: 782
		Interquartile range: 213.5
		First quartile: 1523.5
		Third quartile: 1737
		Variance (σ2): 40267.84
		Standard deviation (σ): 200.66848282678
		Quartile deviation: 106.75
		Mean absolute deviation (MAD): 154.368

		99% Confidence Interval: 1515 to 1667
		95% Confidence Interval: 1534 to 1648
		90% Confidence Interval: 1543 to 1638

