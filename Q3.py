def add_tag(profile, tag):
    updated = profile.copy()
    updated['tags'] = profile['tags'].copy()             #make 2nd list independent
    updated['tags'].append(tag)
    return updated
original = {'name': 'Ada', 'tags': ['pyhton']}
changed = add_tag(original, 'testing')

print(original['tags'])
print(changed)
print(changed is original)
print(changed['tags'] is original['tags'])

assert original['tags'] == ['pyhton'], 'Original tags was altered'
assert changed['tags'] == ['pyhton', 'testing'], 'Returned tags dont contain new tag'
changed['tags'].append('jesu')
assert original['tags'] == ['pyhton'], 'Original tags altered after final append'