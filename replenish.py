from odps.udf import annotate

@annotate("*->string")
class Replenish(object):
  '''
    Concat column2 to column1 to ensure that there are only 500 elements at most
    sep: dividing symbol between elements
    item_sep: the dividing symbol in the element
  '''
  def evaluate(self,column1,column2,sep=',',item_sep=':',number=500):
    if not column1 and not column2:
      return ""
    elif not column1:
      return column2
    elif not column2:
      return column1
    items=column1.split(sep)
    items_len=len(items)
    if items_len>number:
      return column1
    items_dict={}
    for it in items:
      it=it.split(item_sep)
      if len(it)<2:
        continue 
      items_dict[it[0]]=it[1]
    
    items_other=column2.split(sep)
    for its in items_other:
      it=its.split(item_sep)
      if len(it)<2:
        continue
      if it[0] not in items_dict:
        items.append(its)
        items_len+=1
      if items_len>number:
        break 
    return ','.join(items)