from tools import *

frn = form()
iv =intVar()
checkbox(frn).pack()
checkbox(frn,"ahmed",iv).pack()

def test():
    print(iv.get())
button(frn,"ok",test).pack()
frn.mainloop()

