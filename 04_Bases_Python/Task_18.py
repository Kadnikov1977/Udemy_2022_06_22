def is_cat_here(item, *args):
    if item in list(args):
        return 'Yes'
    else:
        return 'No'

print(is_cat_here('cat', 123, 'cat', 'tyu'))