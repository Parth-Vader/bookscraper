# Testing the stability of the benchmark

I am using the given spider on `nginx` server with the following settings:
    
    LOGSTATS_INTERVAL = 3
    LOG_LEVEL = 'INFO'
    CLOSESPIDER_TIMEOUT = 30
    
I used the total number of `pages crawled` and `items scraped` and multiplied it with `60/30 = 2` to get the average speed per minute.
After taking such data of 50 spiders, the graph obtained is as follows :

![Graph](https://github.com/Parth-Vader/bookscraper/blob/master/Stability/20170511033241.jpg)

The benchmark is fairly stable, with lower values in the middle. The average CPU usage was around `35-40%`.
