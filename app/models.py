from datetime import date
from datetime import datetime
from pony.orm import *


db = Database()


class ToDoItem(db.Entity):
    _table_ = 'to_do_item'
    id = PrimaryKey(int, auto=True)
    item = Required(str)
    due_date = Required(str)

    
    # to_do_list = Required('ToDoList')
    # notes = Optional(LongStr)
    # info = Required(Json)


    # def to_dict(self):
    #     return {
    #         'id': self.id,
    #         'item': self.item,
    #         'due_date': self.due_date,
    #         'to_do_list': self.to_do_list,
    #         'notes': self.notes
    #     }




class ToDoList(db.Entity):
    _table_ = 'to_do_list'
    id = PrimaryKey(int, auto=True)
    list_name = Required(str)
    # to_do_item = Optional(ToDoItem)


