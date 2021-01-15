# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def format_dmg(entry_str):
    if entry_str.endswith('M'):
        return float(entry_str.strip('M')) * 1000000
    elif entry_str.endswith('B'):
        return float(entry_str.strip('B')) * 1000000000
    else:
        return entry_str

dmgs_fmtd = [format_dmg(dmg) for dmg in damages]
#print(dmgs_fmtd)

# write your construct hurricane dictionary function here:
hurricane_dict = {}

for i, v in enumerate(names):
    hurricane_dict[v] = {
        'Name': v,
        'Month': months[i],
        'Year': years[i],
        'Max Sustained Wind': max_sustained_winds[i],
        'Areas Affected': areas_affected[i],
        'Damage': damages[i],
        'Deaths': deaths[i]
    }

#print(hurricane_dict)

# write your construct hurricane by year dictionary function here:
hurr_by_year_dict = {}

for i, yr in enumerate(years):
    if yr in hurr_by_year_dict:
        hurr_by_year_dict[yr].append(hurricane_dict[names[i]])
    else:
        hurr_by_year_dict[yr] = [hurricane_dict[names[i]]]

#print(hurr_by_year_dict)

# write your count affected areas function here:
areas_dict = {}

for hurr_area in areas_affected:
    for area in hurr_area:
        if area in areas_dict:
            areas_dict[area] += 1
        else:
            areas_dict[area] = 1

#print(areas_dict)

# write your find most affected area function here:
def find_largest_val(d):
    max_val = 0
    max_key = ''

    for k, v in d.items():
        if v > max_val:
            max_val = v
            max_key = k
        else:
            continue

    return f"The region affected the most by hurricanes is {max_key} with {max_val} hurricanes."

#print(find_largest_val(areas_dict))

# write your greatest number of deaths function here:
def find_max_value_in_category(d, key):
    max_val = 0
    max_key = ''

    for k, v in d.items():
        if v[key] > max_val:
            max_val = v[key]
            max_key = k
        else:
            continue
    
    return f"The hurricane with the highest {key.lower()} is {max_key} with total of {max_val} deaths." 

#print(find_max_value_in_category(hurricane_dict, 'Deaths'))

# write your catgeorize by mortality function here:
def get_mort_scale(lst):
    mort_scale_per_hurr = []

    mortality_scale = {
        0: 0,
        1: 100,
        2: 1000,
        3: 10000,
        4: 100000
    }

    for total in deaths:
        for k, v in mortality_scale.items():
            if total < v:
                scale = k
                break
            else:
                scale = 5
        
        mort_scale_per_hurr.append(scale)
    
    return mort_scale_per_hurr

mort_scale_dict = {}

for rating, name in zip(get_mort_scale(deaths), names):
    if rating in mort_scale_dict:
        mort_scale_dict[rating].append(hurricane_dict[name])
    else:
        mort_scale_dict[rating] = [hurricane_dict[name]]
    
#print(mort_scale_dict)

# write your greatest damage function here:
def find_max_value_in_category_b(d, key):
    max_val = 0
    max_key = ''

    for k, v in d.items():
        try:
            if format_dmg(v[key]) > max_val:
                max_val = format_dmg(v[key])
                max_key = k
            else:
                continue
        except TypeError:
            continue
    
    return f"The hurricane with the highest {key.lower()} is {max_key} with total of {max_val} in damages." 

#print(find_max_value_in_category_b(hurricane_dict, 'Damage'))

# write your catgeorize by damage function here:
def get_dmg_scale(lst):
    dmg_scale_per_hurr = []

    damage_scale = {
        0: 0,
        1: 100000000,
        2: 1000000000,
        3: 10000000000,
        4: 50000000000
    }

    for total in dmgs_fmtd:
        for k, v in damage_scale.items():
            try:
                if total < v:
                    scale = k
                    break
                else:
                    scale = 5
            except TypeError:
                scale = total
        
        dmg_scale_per_hurr.append(scale)
    
    return dmg_scale_per_hurr

dmg_scale_dict = {}

for rating, name in zip(get_dmg_scale(deaths), names):
    if rating in dmg_scale_dict:
        dmg_scale_dict[rating].append(hurricane_dict[name])
    else:
        dmg_scale_dict[rating] = [hurricane_dict[name]]
    
print(dmg_scale_dict)