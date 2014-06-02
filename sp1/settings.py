# Scrapy settings for sp1 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'sp1'

SPIDER_MODULES = ['sp1.spiders']
NEWSPIDER_MODULE = 'sp1.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'sp1 (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
		'sp1.pipelines.Sp1Pipeline': 300,
		}
