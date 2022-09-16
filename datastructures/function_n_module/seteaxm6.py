fruits= {'apple', 'banana','grapes', 'pineapple'}
dry_fruits={'almond', 'date', 'casheew', 'kismis'}
 
all_fruits = dry_fruits|fruits

print(all_fruits)
print(fruits)
print(dry_fruits)

ans= dry_fruits.isdisjoint(fruits)
print(ans)

ans=dry_fruits.issuperset(all_fruits)
print('dry_fruitsis the subset of all fruits' ,ans)

ans= (' dry_fruits is the superset of apple', ans)

