""" A simple API for collecting lunch orders.
    The person who makes jokes causing chaos on the list will be the delivery boy.
"""
import hug

domain = 'http://localhost:8000'
data = []

@hug.get(examples=['who=Big Dummy&what=MegaBurger'])
@hug.cli()
def order(who: hug.types.text, what: hug.types.text):
    ''' If you want to place an order, use /order?who=[your name]&what=[your pick]'''
    if len(data) == 0:
        id = 0
    else:
        id = max(len(data), max([x['id'] for x in data]))
    data.append({'id': id+1, 'who': who, 'what': what, 'actions': {'remove': f'{domain}/remove?id={id+1}'}})
    return wrap_data(data)


@hug.get()
@hug.cli()
def orders():
    ''' Returns the current list of orders '''
    return wrap_data(data)


@hug.get()
@hug.cli()
def remove(id: hug.types.text):
    for o in data:
        print(f'{o} == {id}?')
        if str(o['id']) == id:
            data.remove(o)
    return wrap_data(data)

def wrap_data(data):
    return {
        'data': [data],
        'actions': {
            'go back': domain
        }
    }

if __name__ == '__main__':
    add.interface.cli()
