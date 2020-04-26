# SiteScraper
A python script to scrape the homepages of various technology websites and return titles, descriptions, and urls of the home articles. (At the time of first upload, April 2020, pretty much all articles are about the coronavirus.)

![article scrape](https://i.imgur.com/ltVa6ok.png "Screenshot of articledata.csv")

This python script uses [Beautiful Soap](https://www.crummy.com/software/BeautifulSoup/) to pull text and urls from websites, and exports the information into CSV files.

Most websites are structured differently, so each individual website should be scraped through a unique process. Users who want to add to the script should:
* load up the desired website in a browser
* enable "developer mode" or "inspect" the website
* find the page element (eg, "div", "a", "li", etc) that repeats to display articles. This should be identified in the "find_All()" function.
* identify the elements that make up article properties (eg,"h2", "h5", .get_text()) containing the header, url, and, where applicable, description). There are a bunch of different methods of creating content - consequently, you'll see that each scrape function uses a different method of extracting content. 

Each article is appended to a .csv file. 
