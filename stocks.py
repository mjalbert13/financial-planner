from pandas_datareader import data    
import datetime
from bokeh.plotting import figure, show, output_file

start = datetime.datetime(2020,2,11)
end = datetime.datetime(2020,2,21)

df = data.DataReader(name="FB", data_source="yahoo",start=start,end=end)

higherClose= df.index[df.Close > df.Open]
lowerClose= df.index[df.Close < df.Open]


def inc_dec(o, c):
    if c > o:
        value="Increase"
    elif c < o:
        value="Decrease"
    else:
        value="Equal"
    return value

df["Status"]=[inc_dec(o,c) for o,c in zip(df.Open, df.Close)]
df["Middle"]=[(df.Open+df.Close)/2]

print(df)
p = figure(x_axis_type='datetime', width=1000, height=500, title="Stock Table")

hours = 12*60*60*1000

p.rect(df.index[df.Close > df.Open],(df.Open +df.Close)/2, hours,abs(df.Open-df.Close),
 fill_color="green", line_color="black")

p.rect(df.index[df.Close < df.Open],(df.Open +df.Close)/2, hours,abs(df.Open-df.Close),
 fill_color="red", line_color="black")


output_file("Stocks.html")
show(p)