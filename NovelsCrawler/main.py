#!/usr/bin/env python3
from scrapy.cmdline import execute

import sys
import os


# encoding=utf8



#execute(["scrapy","crawl","novel"])

execute(["scrapy","crawl","novel","-o","quotes.json"])
# execute(["scrapy","crawl","novel","-s", "LOG_ENABLED=False"])


# encoding:UTF-8



