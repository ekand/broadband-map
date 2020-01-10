### WARNING ### This is an example of what not to do

map_il = {} # fake, empty data (to quiet down the linter)

# # remove non-cook county entries from the features list in map_il
features = map_il['features']
features_length_before = len(features)
for i, feature in enumerate(features):
    if feature['properties']['COUNTYFP10'] != "031":
        del features[i]
print('removed non-cook county entries from map_il')
features_length_after = len(features)
assert features_length_after < features_length_before, "features list should be shorter after removing non-cook-county entries"

"""
Here's the problem with this code: I have a for loop through features,
but as I delete items from features, the for loop get jacked up
somehow and behaves unexpectedly.
The result is that some features with county not
equal to "031: creep into the resultant map
"""