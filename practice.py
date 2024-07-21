from datetime import datetime,timedelta


start=datetime.now()

end=start+timedelta(days=30)

x=end-start
print(x.days,x.total_seconds()/60)



