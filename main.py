###solution to exercise 86 from ben stephenson's "the python workbook".

def get_ordinal(num_):

  mydict = {  1:  'first',
            2:  'second',
            3:  'third',
            4:  'fourth',
            5:  'fifth',
            6:  'sixth',
            7:  'seventh',
            8:  'eighth',
            9:  'ninth',
            10: 'tenth',
            11: 'eleventh',
            12: 'twelfth' }

  if not (num_ in range(1,13)):
    return ''
  else:
    return mydict[num_]

def print_verse(num_):

  mydict = {  1:  'And a partridge in a pear tree.\n',
            2:  'Two turtle doves',
            3:  'Three french hens',
            4:  'Four calling birds',
            5:  'Five golden rings',
            6:  'Six geese a-laying',
            7:  'Seven swans a-swimming',
            8:  'Eight maids a-milking',
            9:  'Nine ladies dancing',
            10: 'Ten lords a-leaping',
            11: 'Eleven pipers piping',
            12: 'Twelve drummers drumming' }

  strophes = [int(i) for i in range(1,num_ + 1)]
  strophes.reverse()
  print(f'On the {get_ordinal(num_)} day of Christmas\nmy true love sent to me')
  for i in strophes:
    print(mydict[i])

for i in range(1,13):
  if i == 1:
    print('On the first day of Christmas\nmy true love sent to me\nA partridge in a pear tree.\n')
  else:
    print_verse(i)
