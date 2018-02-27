### Academy of Py

#### Three trends based on this dataset:

1. School size and score results can have a negative effect on student performance. The larger the number of students, the lower success in grades.

2. The budget per student and spending levels are negatively correlated with scores.

3. Students from Charter schools perform better than students from District schools. The data shows a significant difference with the overall passing rate among students between Charter and District schools. The largest Charter school has much better scores than the smallest District school. This data only takes into consideration large District and small Charter school size so there is probably a discrepancy with the two types of schools.

#### Taking into consideration the following:
* My passing score and definition of a passing rate is an assumption. I decided to set it at a score of 65 based on Google's top search results for American High Schools. I did not look up Charter or District school categories. 

```python
# dependencies
import pandas as pd
import numpy as np
```


```python
# csv file location
schools_rdata = "raw_data/schools_complete.csv"
students_rdata = "raw_data/students_complete.csv"
```


```python
# format decimals
pd.options.display.float_format = '{:,.2f}'.format

# read schools data
schools_df = pd.read_csv(schools_rdata)
schools_df.head()

# rename column 'name' to 'school'
school = schools_df.rename(columns={"name": "school"})
school.head()
```

<div>
<!-- <style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style> -->

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School ID</th>
      <th>school</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
    </tr>
  </tbody>
</table>
</div>




```python
# read students data
students_df = pd.read_csv(students_rdata)
students_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Student ID</th>
      <th>name</th>
      <th>gender</th>
      <th>grade</th>
      <th>school</th>
      <th>reading_score</th>
      <th>math_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>66</td>
      <td>79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Victor Smith</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>61</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Dr. Richard Scott</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>67</td>
      <td>58</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>97</td>
      <td>84</td>
    </tr>
  </tbody>
</table>
</div>




```python
# find totals for district:
school_list = students_df['school'].unique()
total_schools = len(school_list)
total_students = students_df['name'].count()
total_budget = schools_df['budget'].sum()

# find averages for scores:
ave_math_score=students_df['math_score'].mean()
ave_reading_score=students_df['reading_score'].mean()

# locate and count passing (i.e. better than 65, based on US high school data) scores
math_pass_df = students_df.loc[students_df["math_score"] >= 65, :]
math_pass_count = math_pass_df['math_score'].count()
reading_pass_df = students_df.loc[students_df["reading_score"] >= 65, :]
reading_pass_count = reading_pass_df['reading_score'].count()

# calculate percentages:
percent_pass_math = math_pass_count/total_students*100
percent_pass_reading = reading_pass_count/total_students*100
percent_pass_overall = (math_pass_count + reading_pass_count)/total_students*50

# build district summary dataframe:
district_breakdown = pd.DataFrame({"Total Schools": [total_schools],
                                   "Total Students": [total_students],
                                   "Total Budget": [total_budget],
                                   "Average Math Score": [ave_math_score],
                                   "Average Reading Score": [ave_reading_score],
                                   "% Passing Math":[percent_pass_math],
                                   "% Passing Reading":[percent_pass_reading],
                                   "% Overall Passing Rate": [percent_pass_overall]})
district_breakdown['Total Budget'] = district_breakdown['Total Budget'].map('${:,.2f}'.format)
district_breakdown=district_breakdown[['Total Schools','Total Students','Total Budget','Average Math Score', 'Average Reading Score','% Passing Math','% Passing Reading','% Overall Passing Rate']]

district_breakdown
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Schools</th>
      <th>Total Students</th>
      <th>Total Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15</td>
      <td>39170</td>
      <td>$24,649,428.00</td>
      <td>78.99</td>
      <td>81.88</td>
      <td>84.73</td>
      <td>96.20</td>
      <td>90.46</td>
    </tr>
  </tbody>
</table>
</div>




```python
# prepare schools df for merge with average students scores:
schools_df = schools_df.rename(index=str, columns={"name":"school"})
school_groups_df =students_df.groupby(["school"])
school_score_groups_df = school_groups_df[['school','math_score','reading_score']].mean().reset_index()

# merge schools data with average scores data:
aves_merge_df = pd.merge(school_score_groups_df, schools_df, on="school")

# find pass counts by school and merge with school summary df:
school_math_pass_group  = math_pass_df.groupby(["school"])
school_math_pass_df = school_math_pass_group[['math_score']].count().reset_index()
school_reading_pass_group  = reading_pass_df.groupby(["school"])
school_reading_pass_df = school_reading_pass_group[['reading_score']].count().reset_index()
pass_count_merge_df = pd.merge(aves_merge_df, school_math_pass_df, on="school")
pass_count_merge_df = pd.merge(pass_count_merge_df, school_reading_pass_df, on="school")

# complete per school summary with percentages columns and per student budgets:
pass_count_merge_df['% Passing Math'] = pass_count_merge_df['math_score_y']/pass_count_merge_df['size']*100
pass_count_merge_df['% Passing Reading'] = pass_count_merge_df['reading_score_y']/pass_count_merge_df['size']*100
pass_count_merge_df['% Overall Passing'] = (pass_count_merge_df['% Passing Math'] + pass_count_merge_df['% Passing Reading'])/2
pass_count_merge_df['Per Student Budget'] = pass_count_merge_df['budget']/pass_count_merge_df['size']

school_summary = pass_count_merge_df.rename(index=str, columns={"school":"School",'math_score_x':'Average Math Score',
                                                                'reading_score_x':'Average Reading Score','type':'School Type',
                                                                'size':'Total Students','budget':'Total Budget'})

school_summary = school_summary.drop(['math_score_y','reading_score_y','School ID'], axis = 1)
school_summary = school_summary[["School",'School Type','Total Students','Total Budget','Per Student Budget',
                                 'Average Math Score', 'Average Reading Score','% Passing Math',
                                 '% Passing Reading','% Overall Passing']]

school_summary = school_summary.set_index('School')
school_summary['Total Budget'] = school_summary['Total Budget'].map('${:,.2f}'.format)
school_summary['Per Student Budget'] = school_summary['Per Student Budget'].map('${:,.2f}'.format)
school_summary
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing</th>
    </tr>
    <tr>
      <th>School</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>District</td>
      <td>4976</td>
      <td>$3,124,928.00</td>
      <td>$628.00</td>
      <td>77.05</td>
      <td>81.03</td>
      <td>77.91</td>
      <td>94.55</td>
      <td>86.23</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>Charter</td>
      <td>1858</td>
      <td>$1,081,356.00</td>
      <td>$582.00</td>
      <td>83.06</td>
      <td>83.98</td>
      <td>100.00</td>
      <td>100.00</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>District</td>
      <td>2949</td>
      <td>$1,884,411.00</td>
      <td>$639.00</td>
      <td>76.71</td>
      <td>81.16</td>
      <td>77.18</td>
      <td>94.54</td>
      <td>85.86</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>District</td>
      <td>2739</td>
      <td>$1,763,916.00</td>
      <td>$644.00</td>
      <td>77.10</td>
      <td>80.75</td>
      <td>78.20</td>
      <td>93.87</td>
      <td>86.04</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>Charter</td>
      <td>1468</td>
      <td>$917,500.00</td>
      <td>$625.00</td>
      <td>83.35</td>
      <td>83.82</td>
      <td>100.00</td>
      <td>100.00</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>District</td>
      <td>4635</td>
      <td>$3,022,020.00</td>
      <td>$652.00</td>
      <td>77.29</td>
      <td>80.93</td>
      <td>77.73</td>
      <td>94.61</td>
      <td>86.17</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>Charter</td>
      <td>427</td>
      <td>$248,087.00</td>
      <td>$581.00</td>
      <td>83.80</td>
      <td>83.81</td>
      <td>100.00</td>
      <td>100.00</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>District</td>
      <td>2917</td>
      <td>$1,910,635.00</td>
      <td>$655.00</td>
      <td>76.63</td>
      <td>81.18</td>
      <td>77.72</td>
      <td>94.48</td>
      <td>86.10</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>District</td>
      <td>4761</td>
      <td>$3,094,650.00</td>
      <td>$650.00</td>
      <td>77.07</td>
      <td>80.97</td>
      <td>77.97</td>
      <td>94.48</td>
      <td>86.22</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>Charter</td>
      <td>962</td>
      <td>$585,858.00</td>
      <td>$609.00</td>
      <td>83.84</td>
      <td>84.04</td>
      <td>100.00</td>
      <td>100.00</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>District</td>
      <td>3999</td>
      <td>$2,547,363.00</td>
      <td>$637.00</td>
      <td>76.84</td>
      <td>80.74</td>
      <td>77.94</td>
      <td>94.62</td>
      <td>86.28</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>Charter</td>
      <td>1761</td>
      <td>$1,056,600.00</td>
      <td>$600.00</td>
      <td>83.36</td>
      <td>83.73</td>
      <td>100.00</td>
      <td>100.00</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>Charter</td>
      <td>1635</td>
      <td>$1,043,130.00</td>
      <td>$638.00</td>
      <td>83.42</td>
      <td>83.85</td>
      <td>100.00</td>
      <td>100.00</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>Charter</td>
      <td>2283</td>
      <td>$1,319,574.00</td>
      <td>$578.00</td>
      <td>83.27</td>
      <td>83.99</td>
      <td>100.00</td>
      <td>100.00</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>Charter</td>
      <td>1800</td>
      <td>$1,049,400.00</td>
      <td>$583.00</td>
      <td>83.68</td>
      <td>83.95</td>
      <td>100.00</td>
      <td>100.00</td>
      <td>100.00</td>
    </tr>
  </tbody>
</table>
</div>




```python
# extract the top performing schools
top_five_schools = school_summary.sort_values(by=["% Overall Passing"], ascending=False)
top_five_schools.head(5)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing</th>
    </tr>
    <tr>
      <th>School</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Cabrera High School</th>
      <td>Charter</td>
      <td>1858</td>
      <td>$1,081,356.00</td>
      <td>$582.00</td>
      <td>83.06</td>
      <td>83.98</td>
      <td>100.00</td>
      <td>100.00</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>Charter</td>
      <td>1468</td>
      <td>$917,500.00</td>
      <td>$625.00</td>
      <td>83.35</td>
      <td>83.82</td>
      <td>100.00</td>
      <td>100.00</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>Charter</td>
      <td>427</td>
      <td>$248,087.00</td>
      <td>$581.00</td>
      <td>83.80</td>
      <td>83.81</td>
      <td>100.00</td>
      <td>100.00</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>Charter</td>
      <td>962</td>
      <td>$585,858.00</td>
      <td>$609.00</td>
      <td>83.84</td>
      <td>84.04</td>
      <td>100.00</td>
      <td>100.00</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>Charter</td>
      <td>1761</td>
      <td>$1,056,600.00</td>
      <td>$600.00</td>
      <td>83.36</td>
      <td>83.73</td>
      <td>100.00</td>
      <td>100.00</td>
      <td>100.00</td>
    </tr>
  </tbody>
</table>
</div>




```python
# lower five performing schools
lower_five_schools = top_five_schools.tail()
lower_five_schools = lower_five_schools.sort_values("% Overall Passing")
lower_five_schools
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing</th>
    </tr>
    <tr>
      <th>School</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Figueroa High School</th>
      <td>District</td>
      <td>2949</td>
      <td>$1,884,411.00</td>
      <td>$639.00</td>
      <td>76.71</td>
      <td>81.16</td>
      <td>77.18</td>
      <td>94.54</td>
      <td>85.86</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>District</td>
      <td>2739</td>
      <td>$1,763,916.00</td>
      <td>$644.00</td>
      <td>77.10</td>
      <td>80.75</td>
      <td>78.20</td>
      <td>93.87</td>
      <td>86.04</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>District</td>
      <td>2917</td>
      <td>$1,910,635.00</td>
      <td>$655.00</td>
      <td>76.63</td>
      <td>81.18</td>
      <td>77.72</td>
      <td>94.48</td>
      <td>86.10</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>District</td>
      <td>4635</td>
      <td>$3,022,020.00</td>
      <td>$652.00</td>
      <td>77.29</td>
      <td>80.93</td>
      <td>77.73</td>
      <td>94.61</td>
      <td>86.17</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>District</td>
      <td>4761</td>
      <td>$3,094,650.00</td>
      <td>$650.00</td>
      <td>77.07</td>
      <td>80.97</td>
      <td>77.97</td>
      <td>94.48</td>
      <td>86.22</td>
    </tr>
  </tbody>
</table>
</div>




```python
# math scores by grade
twelfthgrade = students_df.loc[students_df["grade"] == "12th"].groupby("school")["math_score"].mean()
eleventhgrade = students_df.loc[students_df["grade"] == "11th"].groupby("school")["math_score"].mean()
tenthgrade = students_df.loc[students_df["grade"] == "10th"].groupby("school")["math_score"].mean()
ninthgrade = students_df.loc[students_df["grade"] == "9th"].groupby("school")["math_score"].mean()

math_scores = pd.DataFrame({
        "9th": ninthgrade,
        "10th": tenthgrade,
        "11th": eleventhgrade,
        "12th": twelfthgrade
})

math_scores = math_scores[["9th", "10th", "11th", "12th"]]
math_scores.index.name = " "
math_scores
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>9th</th>
      <th>10th</th>
      <th>11th</th>
      <th>12th</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>77.08</td>
      <td>77.00</td>
      <td>77.52</td>
      <td>76.49</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.09</td>
      <td>83.15</td>
      <td>82.77</td>
      <td>83.28</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>76.40</td>
      <td>76.54</td>
      <td>76.88</td>
      <td>77.15</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>77.36</td>
      <td>77.67</td>
      <td>76.92</td>
      <td>76.18</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>82.04</td>
      <td>84.23</td>
      <td>83.84</td>
      <td>83.36</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>77.44</td>
      <td>77.34</td>
      <td>77.14</td>
      <td>77.19</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.79</td>
      <td>83.43</td>
      <td>85.00</td>
      <td>82.86</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>77.03</td>
      <td>75.91</td>
      <td>76.45</td>
      <td>77.23</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>77.19</td>
      <td>76.69</td>
      <td>77.49</td>
      <td>76.86</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.63</td>
      <td>83.37</td>
      <td>84.33</td>
      <td>84.12</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>76.86</td>
      <td>76.61</td>
      <td>76.40</td>
      <td>77.69</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>83.42</td>
      <td>82.92</td>
      <td>83.38</td>
      <td>83.78</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.59</td>
      <td>83.09</td>
      <td>83.50</td>
      <td>83.50</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.09</td>
      <td>83.72</td>
      <td>83.20</td>
      <td>83.04</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.26</td>
      <td>84.01</td>
      <td>83.84</td>
      <td>83.64</td>
    </tr>
  </tbody>
</table>
</div>




```python
# reading scores by grade
twelfthgrade = students_df.loc[students_df["grade"] == "12th"].groupby("school")["reading_score"].mean()
eleventhgrade = students_df.loc[students_df["grade"] == "11th"].groupby("school")["reading_score"].mean()
tenthgrade = students_df.loc[students_df["grade"] == "10th"].groupby("school")["reading_score"].mean()
ninthgrade = students_df.loc[students_df["grade"] == "9th"].groupby("school")["reading_score"].mean()

reading_scores = pd.DataFrame({
        "9th": ninthgrade,
        "10th": tenthgrade,
        "11th": eleventhgrade,
        "12th": twelfthgrade
})

reading_scores = reading_scores[["9th", "10th", "11th", "12th"]]
reading_scores.index.name = " "
reading_scores
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>9th</th>
      <th>10th</th>
      <th>11th</th>
      <th>12th</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>81.30</td>
      <td>80.91</td>
      <td>80.95</td>
      <td>80.91</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.68</td>
      <td>84.25</td>
      <td>83.79</td>
      <td>84.29</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>81.20</td>
      <td>81.41</td>
      <td>80.64</td>
      <td>81.38</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>80.63</td>
      <td>81.26</td>
      <td>80.40</td>
      <td>80.66</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>83.37</td>
      <td>83.71</td>
      <td>84.29</td>
      <td>84.01</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>80.87</td>
      <td>80.66</td>
      <td>81.40</td>
      <td>80.86</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.68</td>
      <td>83.32</td>
      <td>83.82</td>
      <td>84.70</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>81.29</td>
      <td>81.51</td>
      <td>81.42</td>
      <td>80.31</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>81.26</td>
      <td>80.77</td>
      <td>80.62</td>
      <td>81.23</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.81</td>
      <td>83.61</td>
      <td>84.34</td>
      <td>84.59</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>80.99</td>
      <td>80.63</td>
      <td>80.86</td>
      <td>80.38</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>84.12</td>
      <td>83.44</td>
      <td>84.37</td>
      <td>82.78</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.73</td>
      <td>84.25</td>
      <td>83.59</td>
      <td>83.83</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.94</td>
      <td>84.02</td>
      <td>83.76</td>
      <td>84.32</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.83</td>
      <td>83.81</td>
      <td>84.16</td>
      <td>84.07</td>
    </tr>
  </tbody>
</table>
</div>




```python
# compare results based on per student spending:
spend_bins = [0, 580, 605, 630, 655]
spend_labels = ["Less than $580", "Medium $580-605", "Average $605-630", "Above Average $630-655"]
spend_categories = pd.cut(pass_count_merge_df["Per Student Budget"], spend_bins, labels=spend_labels)

breakdown_by_spending_df = pd.DataFrame({'Spend Level':spend_categories,
                                        'Average Math Score':aves_merge_df['math_score'],                                       
                                        'Average Reading Score':aves_merge_df['reading_score'],
                                        '% Passing Math':pass_count_merge_df['% Passing Math'], 
                                        '% Passing Reading':pass_count_merge_df['% Passing Reading'],
                                        'Overall Passing Rate':pass_count_merge_df['% Overall Passing']})

breakdown_by_spending_df.sort_values('Spend Level')
grouped_breakdown_by_spending_df = breakdown_by_spending_df.groupby(['Spend Level'])

spending_per_student = grouped_breakdown_by_spending_df.mean()
spending_per_student = spending_per_student[['Average Math Score', 'Average Reading Score', '% Passing Math',
                                             '% Passing Reading', 'Overall Passing Rate']]
spending_per_student
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
    <tr>
      <th>Spend Level</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Less than $580</th>
      <td>83.27</td>
      <td>83.99</td>
      <td>100.00</td>
      <td>100.00</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Medium $580-605</th>
      <td>83.48</td>
      <td>83.87</td>
      <td>100.00</td>
      <td>100.00</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Average $605-630</th>
      <td>81.41</td>
      <td>82.97</td>
      <td>92.64</td>
      <td>98.18</td>
      <td>95.41</td>
    </tr>
    <tr>
      <th>Above Average $630-655</th>
      <td>77.87</td>
      <td>81.37</td>
      <td>80.96</td>
      <td>95.23</td>
      <td>88.10</td>
    </tr>
  </tbody>
</table>
</div>




```python
# scores by school size
school_size_bins = [0, 500, 2750, 5000]
school_size_labels = ["Small (<500)", "Medium (500-2750)", "Large (2750-5000)"]
school_size_categories = pd.cut(pass_count_merge_df["size"], school_size_bins, labels=school_size_labels)

breakdown_by_size_df = pd.DataFrame({'School Size':school_size_categories,
                                        'Average Math Score':aves_merge_df['math_score'],                                       
                                        'Average Reading Score':aves_merge_df['reading_score'],
                                        '% Passing Math':pass_count_merge_df['% Passing Math'], 
                                        '% Passing Reading':pass_count_merge_df['% Passing Reading'],
                                        'Overall Passing Rate':pass_count_merge_df['% Overall Passing']})

grouped_breakdown_by_size_df = breakdown_by_size_df.groupby(['School Size'])

size_comparison = grouped_breakdown_by_size_df.mean()
size_comparison = size_comparison[['Average Math Score', 'Average Reading Score', '% Passing Math',
                                   '% Passing Reading', 'Overall Passing Rate']]
size_comparison
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
    <tr>
      <th>School Size</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Small (&lt;500)</th>
      <td>83.80</td>
      <td>83.81</td>
      <td>100.00</td>
      <td>100.00</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>Medium (500-2750)</th>
      <td>82.64</td>
      <td>83.51</td>
      <td>97.28</td>
      <td>99.23</td>
      <td>98.25</td>
    </tr>
    <tr>
      <th>Large(2750-5000)</th>
      <td>76.93</td>
      <td>81.00</td>
      <td>77.74</td>
      <td>94.55</td>
      <td>86.14</td>
    </tr>
  </tbody>
</table>
</div>




```python
# scores by school type (District/Charter)
school_types = schools_df[['type','school']]
calcs_by_type_df = pd.DataFrame({'school':aves_merge_df['school'],
                                        'Average Math Score':aves_merge_df['math_score'],                                       
                                        'Average Reading Score':aves_merge_df['reading_score'],
                                        '% Passing Math':pass_count_merge_df['% Passing Math'], 
                                        '% Passing Reading':pass_count_merge_df['% Passing Reading'],
                                        'Overall Passing Rate':pass_count_merge_df['% Overall Passing']})
breakdown_by_type_df = pd.merge(calcs_by_type_df, school_types,on='school')
breakdown_by_type_df = breakdown_by_type_df.rename(index=str, columns={"type":"Type"})

grouped_breakdown_by_type_df = breakdown_by_type_df.groupby(['Type'])

chart_vs_dist_df = grouped_breakdown_by_type_df.mean()
chart_vs_dist_df = chart_vs_dist_df[['Average Math Score', 'Average Reading Score','% Passing Math',
                                     '% Passing Reading','Overall Passing Rate']]
chart_vs_dist_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
    <tr>
      <th>Type</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Charter</th>
      <td>83.47</td>
      <td>83.90</td>
      <td>100.00</td>
      <td>100.00</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>District</th>
      <td>76.96</td>
      <td>80.97</td>
      <td>77.81</td>
      <td>94.45</td>
      <td>86.13</td>
    </tr>
  </tbody>
</table>
</div>




```python

```