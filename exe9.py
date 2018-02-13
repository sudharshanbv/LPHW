"""
1	#	Here's	some	new	strange	stuff,	remember	type	it	exactly.
2
3	days	=	"Mon	Tue	Wed	Thu	Fri	Sat	Sun"
4	months	=	"Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
5
6	print("Here	are	the	days:	",	days)
7	print("Here	are	the	months:	",	months)
8
#9	print("""
#10	There's	something	going	on	here.
#11	With	the	three	double-quotes.
#12	We'll	be	able	to	type	as	much	as	we	like.
#13	Even	4	lines	if	we	want,	or	5,	or	6.
#14	""")

days = "mon tue wed thu fri sat sun"
months = "jan\nfeb\nmar\napr\nmay\njun\njul\naug\nsep\noct\nnov\ndec\n"

print ("Here the dats are : ", days)
print ("Here the months are : ", months)

#print("there is something going on here.\nwith the three double quotes.\nwe will be able to type as much as we like.")
print(f"""
{days}
there is something going on here.
with the three double quotes.
we will be able to type as much as we like.
""")
