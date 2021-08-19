

class MyList(list):

  def remove_min(self):

    self.remove = min(self)

    return self.remove


  def remove_max(self):

    self.remove = max(self)

    return self.remove


u = [10, 3, 5, 1, 2, 7, 6, 4, 8]
i = MyList(u)


print(i.remove_min())
print(i.remove_max())
