class ProxyItem(object):
    def __init__(self, sourcerow:int, sourcecolumn:int, parent=None) -> None:
        self.sRow = sourcerow
        self.sCol = sourcecolumn
        self.parentItem = parent
        self.childItems = []
        if parent:
            parent.addChild(self)

    def addChild(self, item):
        self.childItems.append(item)

    def child(self, row):
        return self.childItems[row]
    
    def childCount(self):
        return len(self.childItems)

    def parent(self):
        return self.parentItem

    def row(self):
        if self.parentItem:
            return self.parentItem.childItems.index(self)
        return 0


