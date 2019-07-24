import prettytable as pt

# @pip install PrettyTable
# @link https://www.cnblogs.com/Mr-Koala/p/6582299.html?utm_source=tuicool&utm_medium=referral

tb = pt.PrettyTable()

tb.field_names = ["City name", "Area", "Population", "Annual Rainfall"]

tb.add_row(["Adelaide",1295, 1158259, 600.5])

tb.add_row(["Brisbane",5905, 1857594, 1146.4])

tb.add_row(["Darwin", 112, 120900, 1714.7])

tb.add_row(["Hobart", 1357, 205556,619.5])

print(tb)

"""
+-----------+------+------------+-----------------+
| City name | Area | Population | Annual Rainfall |
+-----------+------+------------+-----------------+
|  Adelaide | 1295 |  1158259   |      600.5      |
|  Brisbane | 5905 |  1857594   |      1146.4     |
|   Darwin  | 112  |   120900   |      1714.7     |
|   Hobart  | 1357 |   205556   |      619.5      |
+-----------+------+------------+-----------------+
"""