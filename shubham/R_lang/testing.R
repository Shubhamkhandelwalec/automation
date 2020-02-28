library(RMySQL)

mydb = dbConnect(MySQL(), user='root', password='shubham', dbname='sk', host='localhost')

rs = dbSendQuery(mydb, "select * from login_registration ")
data = fetch(rs, n=1)
print(data)