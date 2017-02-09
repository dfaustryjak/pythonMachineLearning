import scipy as sp
import matplotlib.pyplot as plt
import error as info



data = sp.genfromtxt("web_traffic.tsv", delimiter="\t")

x = data[:,0]
y = data[:,1]

x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]


plt.scatter(x,y)
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)], ['week %i'%w for w in range(10)])

fp1, residuals, rank, sv, rcond = sp.polyfit(x, y, 10, full=True)
fp2 = sp.polyfit(x, y, 2)


f1 = sp.poly1d(fp1)
f2 = sp.poly1d(fp2)

fx = sp.linspace(0,x[-1], 1000) # generate X-values for plotting

plt.plot(fx, f1(fx), linewidth=4, color="black")
plt.plot(fx, f2(fx), linewidth=4, color="red")


plt.legend(["d=%i" % f1.order], loc="upper left")
plt.autoscale(tight=True)
plt.grid()
plt.show()

print(info.error(f1, x, y))
print(info.error(f2, x, y))

plt.scatter(x,y)
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)], ['week %i'%w for w in range(10)])

inflection = 3.5*7*24
xa = x[:int(inflection)]
ya = y[:int(inflection)]
xb = x[int(inflection):]
yb = y[int(inflection):]

fa = sp.poly1d(sp.polyfit(xa, ya, 1))
fb = sp.poly1d(sp.polyfit(xb, yb, 1))

fa_error = info.error(fa, xa, ya)
fb_error = info.error(fb, xb, yb)

plt.plot(xa, fa(xa), linewidth=4, color="black")
plt.plot(xb, fb(xb), linewidth=4, color="red")

plt.legend(["d=%i" % f1.order], loc="upper left")
plt.autoscale(tight=True)
plt.grid()
plt.show()