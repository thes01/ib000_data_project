from xml_parser import getDictOfDiscrictsForYear


def combineDictionaries(dictionaries_by_year: list):
    reference_keys = dictionaries_by_year[0].keys()

    new_dict = dict.fromkeys(reference_keys)

    for key in reference_keys:
        for dictionary in dictionaries_by_year:
            if new_dict[key] is None:
                new_dict[key] = []

            new_dict[key].append(dictionary[key])

    return new_dict

# load dictionaries for all years 2005-2014
dictionaries = [getDictOfDiscrictsForYear(year) for year in range(2005, 2015)]
print('loaded')

merged = combineDictionaries(dictionaries)

with open('data/region_counts.txt', mode='w') as csv_file:
    keys_list = list(merged.keys())
    keys_list.sort()
    for key in keys_list:
        csv_file.write('{}\n'.format(repr({"region": key, "counts": merged[key]})))

print('writing completed')