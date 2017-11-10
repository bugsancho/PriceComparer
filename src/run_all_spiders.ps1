$spiders = scrapy list
foreach($spider in $spiders){
    scrapy crawl $spider -a search_term='tp link c1200'
}