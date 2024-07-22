
import sys


from termstyle import TermStyle as style
    
style.Init()

print()
#style._generate_all()


print (style.style_ok+" Ok "+style.style_end)
print (style.style_wrn+"Warning"+style.style_end)
print (style.style_err+"Orrore"+style.style_end)
print (style.style_tmr+"10:23"+style.style_end)

style.print (style.style_ok, "Ok")
style.print (style.style_wrn, "Warning")
style.print (style.style_err, "Orrore")
style.print (style.style_tmr, "10:23")


print(style.reset) 

