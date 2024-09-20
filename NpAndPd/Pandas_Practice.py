# Group By
import pandas as pd

data = pd.read_csv('NYC_Jobs.csv')
print(data.info())
gg = data.groupby('Agency')

# both prints are same
print(gg["Salary Range From"].mean())
print(data.groupby("Agency")["Salary Range From"].mean())

# median, max, min, sum
# possible functions https://pandas.pydata.org/docs/reference/groupby.html
data.groupby("Agency")["Salary Range From"].agg(["mean", "median"])


def do_sth_to_groups(grp):
    print(grp)
    print('*******')


data.groupby("Agency")["Salary Range From"].apply(do_sth_to_groups)


def do_sth_to_groups(grp):
    print(type(grp))
    return grp.mean()


data.groupby("Agency")["Salary Range From"].apply(do_sth_to_groups)
data.groupby(["Agency", "Posting Type"])["Salary Range From"].mean()
data.groupby(["Agency", "Posting Type"])["Salary Range From", "Salary Range To"].mean()
data.groupby(["Agency", "Posting Type"], as_index=False)["Salary Range From", "Salary Range To"].mean()
agency_groups = data.groupby('Agency')
agency_groups.last()
agency_groups.groups
agency_groups.groups.keys()  # .values()
agency_groups.get_group("ADMIN FOR CHILDREN'S SVCS")
double_group = data.groupby(['Agency', 'Posting Type'])['Salary Range From']
double_group
data[(data['Agency'] == "ADMIN FOR CHILDREN'S SVCS") & (data['Posting Type'] == "External")]

pd.DataFrame(double_group.first())
# If you'd like to speed up the grouping, you can turn off the sorting

data.groupby('Agency', sort=False)
df = pd.DataFrame(
    {
        "Publish date": [
            pd.Timestamp("2000-01-02"),
            pd.Timestamp("2000-01-02"),
            pd.Timestamp("2000-01-09"),
            pd.Timestamp("2000-01-16")
        ],
        "ID": [0, 1, 2, 3],
        "Price": [10, 20, 30, 40]
    }
)
df
# if you want to go deeper

# https://pandas.pydata.org/docs/reference/api/pandas.Grouper.html#pandas.Grouper
# potential frequencies: https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases

# you can customize this way more, you can decide on the beginning date, there are
# many more frew options, add offsets etc, but that's beyond the scope of this video
# go check out the documentation above

df.groupby(pd.Grouper(key="Publish date", freq="1W")).mean()
# df.groupby(pd.Grouper(key="Publish date", freq="2W")).mean()
# df.groupby(pd.Grouper(key="Publish date", freq="1D")).mean()



# Apply


import numpy as np
data = pd.read_csv("NYC_Jobs.csv")
data = data[['Job ID','Civil Service Title','Agency','Posting Type','Job Category','Salary Range From','Salary Range To']]
data.head()
# apply can be used with dataframe and series
# you can apply a pre-defined function to it
data['Salary Range From'].apply(np.sqrt)
# depending on whether you apply it to the columns or rows you will get a different result
data[['Salary Range From','Salary Range To']].apply(np.mean, axis=0)
data[['Salary Range From','Salary Range To']].apply(np.mean, axis=1)
# it returns a new series or dataframe object
# so if you don't assign it to anything, nothing will change in your original dataset
data['Avg salary'] = data[['Salary Range From','Salary Range To']].apply(np.mean, axis=1)
data
# you can create a custom function and apply it to the dataframe
def capitalize_position(title):
    title_lower = title.lower()
    title_final = title_lower.capitalize()
    return title_final

data['Civil Service Title'].apply(make_lower_case)
# again you would need to assign it to the dataframe
data['Civil Service Title'] = data['Civil Service Title'].apply(make_lower_case)
# you can write lambda functions
data.apply(lambda x: x.tolist(), axis=1)
# if the result of this apply process is a list, you can decide to do different things with that list
# expand will assign each element of the list to a different column
data.apply(lambda x: x.tolist(), axis=1, result_type='expand')
# broadcast would do that and keep the column names
# see that in expand the column names are newly created to go from 0 to 7
data.apply(lambda x: x.tolist(), axis=1, result_type='broadcast')



# Apply vs Map vs ApplyMap


data = pd.read_csv("NYC_Jobs.csv")
data = data[
    ['Job ID', 'Civil Service Title', 'Agency', 'Posting Type', 'Job Category', 'Salary Range From', 'Salary Range To']]
data.head()


# Talked about apply in more detail in another video
# see it here: https://youtu.be/DsjvCKxOdgI
# apply is good for applying a function to either axis or the whole dataframe at once
def capitalize(text):
    return text.lower().capitalize()


data['Civil Service Title'].apply(capitalize)


# applymap applies a function to each element of the dataframe
# difference between apply and applymap is that apply passes the dataframe to the function
# one axis at a time
# applymap passes one element at a time

def add_year(text):
    return str(text) + '_2022'


data.applymap(add_year)
# map works only on series and its main strength is to replace values
# so given a series like that
s = pd.Series(['cat', 'dog', 'NaN', 'rabbit'])
s
# we can change the values using a dict only
s.map({'cat': 'kitten', 'dog': 'puppy'})


# but you can also still pass a function to it
# this, however, can be done using apply too, so nothing special
# thus, map is mainly useful for when you want to completely map elements from
# one value to another
def change_word(title):
    title = title.replace('DEPT', 'kitten')
    return title


data['Agency'].map(change_word)

# it is also useful if you'd like to update the value in the same way for each element
data['Agency'].map('The position is created by {}'.format)
# for both map and applymap, you can specify na_action to ignore,
# so that NA values will not even be passed to the function
# the result does not change

s.map({'cat': 'kitten', 'dog': 'puppy'}, na_action='')



# Reshape dataframe


data = pd.read_csv("NYC_Jobs.csv")
data.head()



## Pivot
df = pd.DataFrame({'foo': ['one', 'one', 'one', 'two', 'two',
                           'two'],
                   'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'baz': [1, 2, 3, 4, 5, 6],
                   'zoo': ['x', 'y', 'z', 'q', 'w', 't']})
df
df.pivot(index='foo', columns='bar', values='baz')

## Pivot_table
df.pivot_table(values="baz", index=["foo", "bar"], columns=["zoo"])
data.pivot(values='Salary Range From', index='Job ID', columns="Agency")
data.pivot_table(values='Salary Range From', index='Job ID', columns="Agency")
pd.pivot_table(df, values="baz", index=["foo", "bar"], columns=["zoo"])

## Stack


tuples = list(
    zip(
        *[
            ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
            ["one", "two", "one", "two", "one", "two", "one", "two"],
        ]
    )
)
index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])
df2 = df[:4]
df2
a = pd.DataFrame(df.stack())
a

## Unstack


a.unstack(0)
a.unstack('second')

## Melt
melted_data = pd.melt(data, id_vars='Job ID', value_vars=['Agency', 'Posting Type'])
melted_data
melted_data[melted_data['Job ID']==510670]

## Groupby
# I will make a separate video going into the details of groupby
data[['Agency', 'Salary Range From']].groupby('Agency').mean()

## Crosstab
pd.crosstab(data["Agency"], data["Civil Service Title"])
keys = ["panda1", "panda2", "panda3"]

values = [["eats", "shoots"], ["shoots", "leaves"], ["eats", "leaves"]]

df = pd.DataFrame({"keys": keys, "values": values})

df

## Explode
# two different ways of using it
# one just gives you a series object of all the values
# another returns a new dataframe that has each list element on their own row

df["values"].explode()
df.explode('values')





