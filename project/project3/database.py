import psycopg2
DBNAME = "news"


# Function To Find Most Popular Article
def count_article():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select articles.title,count(*) from articles inner join log " +
              "on log.path like '/article/%' || articles.slug group by " +
              "articles.title order by count(*) desc limit 3;")
    posts = c.fetchall()
    db.close()
    return posts


# Function To Find Most Author
def count_authors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select authors.name , count(*) from authors join articles " +
              "on authors.id = articles.author join log on log.path like " +
              "'/article/%' || articles.slug group by authors.name order by " +
              "count(*) desc ;")
    posts = c.fetchall()
    db.close()
    return posts


# Function To Find Error
def net_err():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select x1.date,round((((x2.err * 1.0) * 100 ) / " +
              "(x1.total * 1.0 )),2) " +
              "from (select TO_CHAR(time,'Mon DD,YYYY') as date, " +
              "count(*) as total from log group by date ) as x1 join " +
              "(select TO_CHAR(time,'Mon DD,YYYY') " +
              "as date,count(*) as err from log where " +
              "status <> '200 OK' group by date) as x2 on x1.date = x2.date " +
              "where (x2.err * 100) / x1.total > 1.0 ;")
    posts = c.fetchall()
    db.close()
    return posts
