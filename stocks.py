from pandas_datareader import data    
import datetime
from bokeh.plotting import figure, show, output_file

start = datetime.datetime(2020,2,11)
end = datetime.datetime(2020,2,21)

df = data.DataReader(name="FB", data_source="yahoo",start=start,end=end)

higherClose= df.index[df.Close > df.Open]
lowerClose= df.index[df.Close < df.Open]


def inc_dec(c, o):
    if o > c:
        value="Increase"
    elif o < c:
        value="Decrease"
    else:
        value="Equal"
    return value

df["Status"]=[inc_dec(c,o) for c,o in zip(df.Open, df.Close)]
df["Middle"]=(df.Open+df.Close)/2
df["Height"]=abs(df.Close-df.Open)

print(df)
p = figure(x_axis_type='datetime', width=1000, height=500, title="Stock Table")

hours = 12*60*60*1000

p.rect(df.index[df.Status == "Increase"],df.Middle[df.Status=="Increase"], hours,df.Height[df.Status=="Increase"],
 fill_color="green", line_color="black")

p.rect(df.index[df.Status == "Decrease"],df.Middle[df.Status=="Decrease"], hours,df.Height[df.Status=="Decrease"],
 fill_color="red", line_color="black")


output_file("Stocks.html")
show(p)