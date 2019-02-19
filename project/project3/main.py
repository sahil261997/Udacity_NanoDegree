#!/usr/bin/env python

from database import count_article, count_authors, net_err

articles = count_article()
authors = count_authors()
error = net_err()
print("Most popular articles of all time:")
# Loop To Print Most Popular Article
for title, views in articles:
    print("* {} - {} views".format(title, views))

print("\nMost popular article authors of all time:")
# Loop To Print Most Popular Author
for name, views in authors:
    print("* {} - {} views".format(name, views))

print("\nMore than 1% of requests failed:")
# Loop To Print Error
for date, percent in error:
    print("* {} -- {}% errors".format(date, percent))
