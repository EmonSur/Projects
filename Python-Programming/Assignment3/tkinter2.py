import tkinter as tk

class ShopItem(object):

    def __init__(self, itemid, itemname, itemcost):
        self._itemid = itemid
        self._itemname = itemname
        self._itemcost = itemcost
    
    def __str__(self):
        return "%i %s %i" % (self._itemid, self._itemname, self._itemcost)

    def getItemid(self):
        return self._itemid

    def setItemid(self, itemid):
        self._itemid = itemid

    def getItemname(self):
        return self._itemname

    def setItemname(self, itemname):
        self._itemname = itemname

    def getItemcost(self):
        return self._itemcost

    def setItemcost(self, itemcost):
        self._itemcost = itemcost

    itemid = property(getItemid, setItemid)
    itemname = property(getItemname, setItemname)
    itemcost = property(getItemcost, setItemcost)

class ShopStock(object):

    def __init__(self):
        self._itemdict = {}
        self._itemcount = 0

    def addItem(self, itemname, itemcost):
        newitem = ShopItem(self._itemcount, itemname, itemcost)
        self._itemdict[self._itemcount] = newitem
        self._itemcount += 1

    def getItem(self, itemid):
        return self._itemdict[itemid]

    def getStoreItemDescriptions(self):
        result = []
        items = self._itemdict.values()
        for item in items:
            result.append(item.itemname)
        return result

class TheInterface(object):

    def __init__(self, shop):

        self._shop = shop

        self._root = tk.Tk()
        self._root.title('My Wonderful Shop')
        
        self._labeltext = tk.StringVar()
        tk.Label(self._root, textvariable=self._labeltext).grid(row=1, column=0)

        self._var2 = tk.StringVar()
        self._var2.set(tuple(self._shop.getStoreItemDescriptions()))
        self._lb = tk.Listbox(self._root, listvariable=self._var2)
        self._lb.bind('<<ListboxSelect>>', self.getElement)
        self._lb.grid(row=0, column=0)

        self._root.mainloop()

    def getElement(self, event):    
        selection = event.widget.curselection()
        index = selection[0]
        self._labeltext.set(self._shop.getItem(index).itemname)


if __name__ == "__main__":
    shop = ShopStock()
    shop.addItem('Tayto', 3)
    shop.addItem('Snax', 2)
    shop.addItem('Pringles', 6)

    interface = TheInterface(shop)