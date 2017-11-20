import numpy as np

from pandas import Series, DataFrame

# using hard code data entry
seriesA = Series([0, 1, 2, 3], index=['E0', 'E1', 'E2', 'E3'])
print seriesA

# using random generated data entry
seriesB = Series(np.random.rand(4), index=['E0', 'E1', 'E2', 'E3'])
print seriesB

# using indexes to print some data from series
print seriesA[1], seriesB[1]

# using range to print some data from a series
print seriesA[1:4]

# create a 2x2 DataFrame with random value
DataFrameA = DataFrame(np.random.rand(4).reshape(2, 2))
print DataFrameA

# create a 2x2 DataFrame with random value and named rows and cols
DataFrameB = DataFrame(np.random.rand(4).reshape(2, 2), ['R0', 'R1'], ['C0', 'C1'])
print DataFrameB

# get a named cell from DataFrame
print DataFrameB.ix[['R0'], ['C1']]

# filter data using comparison operators
print DataFrameB < .5
print DataFrameB > .5

# create a 3x3 DataFrame with random value and named rows and cols
DataFrameC = DataFrame(np.random.rand(9).reshape(3, 3), ['R0', 'R1', 'R2'], ['C0', 'C1', 'C2'])

# slice a DataFrame by its rows
print DataFrameC['R0':'R1']

# slice a DataFrame by its rows and cols
print DataFrameC.loc['R0':'R1', 'C0':'C1']

# define a well-defined DataFrame
DataFrameD = DataFrame({'Ca': [1, 2, 3], 'Cb': [4, 5, 6], 'Cc': [7, 8, 9]}, index=['Ra', 'Rb', 'Rc'])
print DataFrameD

# maybe more convenient way to create a hard coded DataFrame
DataFrameE = DataFrame({'Ca': '1 2 3'.split(), 'Cb': '4 5 6'.split(), 'Cc': '7 8 9'.split()}, index=['Ra', 'Rb', 'Rc'])
print DataFrameE

# are these DataFrames same? No
print DataFrameD == DataFrameE

# but these are same! Note: data type is the point.
DataFrameF = DataFrame({'Ca': '1 2 3'.split(), 'Cb': '4 5 6'.split(), 'Cc': '7 8 9'.split()},
                       index=['Ra', 'Rb', 'Rc'],
                       dtype=int
                       )
print DataFrameD == DataFrameF

# get rows of a dataFrame which satisfy a condition
print DataFrameF.loc[DataFrameF['Ca'] > 2]

# get rows of a dataFrame which satisfy multiple condition
# Note: Don't forget to use parentheses
print DataFrameF.loc[(DataFrameF['Ca'] > 2) | (DataFrameF['Cb'] < 5)]

# copy a series
seriesAm = seriesA.copy()

# is SeriesAm same as SeriesA?
print seriesA.equals(seriesAm)

# Series mass-assignment
seriesAm['E0', 'E1'] = -1
print (seriesA)
print (seriesAm)
print seriesA.eq(seriesAm)

# find differences between these two series
print (seriesA - seriesAm)[(seriesA - seriesAm) <> 0]

# get element name instead of the whole series
# TODO: I couldn't find anything, Please contribute if you know how to do it!

# apply +, -, /, * on a series value
seriesAl = seriesA.apply(lambda x: x * 2)
print seriesAl
seriesAl = seriesAl.apply(lambda x: x / 2)
print seriesAl
seriesAl = seriesAl.apply(lambda x: x + 2)
print seriesAl
seriesAl = seriesAl.apply(lambda x: x - 2)
print seriesAl

# maybe you need to do some more complex manipulation
def func(item):
    return (item * 2) + 10
seriesAl = seriesAl.apply(func)
print seriesAl


# copy a DataFrame
DataFrameBm = DataFrameB.copy()

# is DataFrameAm same as DataFrameA?
print DataFrameB.equals(DataFrameBm)

# DataFrame mass-assignment
# TODO: I couldn't find anything, Please contribute if you know how to do it!

# apply +, -, /, * on a DataFrame value
DataFrameDl = DataFrameD.apply(lambda x: x * 2)
print DataFrameDl
DataFrameDl = DataFrameDl.apply(lambda x: x / 2)
print DataFrameDl
DataFrameDl = DataFrameDl.apply(lambda x: x + 2)
print DataFrameDl
DataFrameDl = DataFrameDl.apply(lambda x: x - 2)
print DataFrameDl

# maybe you need to do some more complex manipulation
DataFrameDl = DataFrameDl.apply(func)
print DataFrameDl
