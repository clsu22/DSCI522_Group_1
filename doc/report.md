Identifying strong predictors of breast cancer recurrence
================
Fanli Zhou
2020/1/23 (updated: 2020-01-23)

  - [Summary](#summary)
  - [Introduction](#introduction)
  - [Methods](#methods)
      - [Data](#data)
      - [Analysis](#analysis)
  - [Results and Discussion](#results-and-discussion)
  - [References](#references)

# Summary

We use a model to find out the top three strongest features to predict
breast cancer recurrence.

# Introduction

Breast cancer is a type of cancer that develops in the breast. With
hundreds of thousand women are estimated to be diagnosed with breast
cancer in 2019 alone, breast cancer is the second common cancer found in
women (Cancer.Net 2019). Breast cancer may come back after the initial
treatment, known as breast cancer recurrence (Staff 2018). Based on a
medical study in 2010, breast cancer has a high recurrence rate of
around 40% (Halls 2019). Although the cause of breast cancer is not
clear, some factors such as age and the tumor size are known to affect
the recurrence risk (Staff 2018).

In this project, we attempt to answer the question: What are the
strongest predictors of breast cancer recurrence? Answering this
question will help identify patients who have high breast cancer
recurrence risk. Once we can identify patients with high recurrence
risk, we can give patients corresponding treatments to help prevent
recurrence. Besides, finding out factors related to breast cancer
recurrence may shed light on understanding the cause of breast cancer
recurrence. Thus, it’s important to identify strong predictors of breast
cancer recurrence.

# Methods

## Data

The breast cancer data set was obtained from the UCI Machine Learning
Repository (Dua and Graff 2017) and can be found
[here](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer). The data
set looks at the recurrence and non-recurrence of breast cancer based on
9 features, including groups of age, menopause time, tumor size, ranges
of the number of axillary lymph nodes, presence of node in cap, degree
of malignancy, breast type, breast quadrant, and whether the patient
used radiation therapy. The data set contains 286 instances with missing
values.

## Analysis

The logistic regression algorithm was used to build a classification
model to find out the weights of each feature in the data set. All
variables in the original data set were used to fit the model. The
hyperparameter was chosen with 5-fold cross-validation with as the
scoring method. The Python programming language (Van Rossum and Drake
2009), R programming language (R Core Team 2019) and the following
Python/R packages were used: Pandas (McKinney 2010), NumPy (Oliphant
2006, 1:@walt2011numpy), Altair (VanderPlas et al. 2018), scikit-learn
\[pedregosa2011scikit\], knitr (Xie 2014) and tidyverse (Wickham 2017).
The code used to perform the analysis can be found here: . The code used
to create this report can be found here: .

# Results and Discussion

Before exploring any features, We first analyzed the rate of breast
cancer recurrence in the data set. Only around 28.6% of the patients had
breast cancer recurrence events, while 71.4% of them don’t have any
recurrence events. So the train data set is not well balanced, and we
decided to address this question by scoring our model with metrics such
as the recall score.

Some factors such as “younger age, particularly those under age 35” and
“larger tumor size” are known to increase the risk of breast cancer
recurrence (Staff 2018). To explore the data set, we would like to first
look at how breast cancer recurrence is related to age and tumor size.

To understand the relation between breast cancer recurrence events and
age, we made a plot to show the age distribution of patients with or
without breast cancer recurrence. Based on the plots, most of the
patients in the train data set are between the ages of 30 and 69.
Patients at ages 30-39 are more likely to have breast cancer recurrence
than other age groups.

To study the relation between breast cancer recurrence events and the
average tumor size, we visualized the average tumor size distribution of
patients with or without breast cancer recurrence. From the plot, we see
that the mean of the average tumor size of patients with breast cancer
recurrence is bigger than those without breast cancer recurrence. So
“larger tumor size” is related to breast cancer recurrence events.

Known that the data set reflects the relation between breast cancer
recurrence and age or the tumor size, we then started to look for
features that are good at predicting breast cancer recurrence. We
decided to train a simple logistic regression model to calculate weights
for each feature in the data set. We used 5-fold cross-validation to …

The feature…

Our model works well on the test data set…

# References

<div id="refs" class="references">

<div id="ref-cancer1">

Cancer.Net. 2019. “Breast Cancer: Statistics.” Cancer.Net.
<https://www.cancer.net/cancer-types/breast-cancer/statistics>.

</div>

<div id="ref-Dua2019">

Dua, Dheeru, and Casey Graff. 2017. “UCI Machine Learning Repository.”
University of California, Irvine, School of Information; Computer
Sciences. <http://archive.ics.uci.edu/ml>.

</div>

<div id="ref-cancer3">

Halls, Dr. 2019. “Moose & Doc Breast Cancer.” Cross Cancer Institute in
Edmonton. <https://breast-cancer.ca/chance-cure/>.

</div>

<div id="ref-mckinney-proc-scipy-2010">

McKinney, Wes. 2010. “Data Structures for Statistical Computing in
Python.” In *Proceedings of the 9th Python in Science Conference*,
edited by Stéfan van der Walt and Jarrod Millman, 51–56.

</div>

<div id="ref-oliphant2006guide">

Oliphant, Travis E. 2006. *A Guide to Numpy*. Vol. 1. Trelgol Publishing
USA.

</div>

<div id="ref-R">

R Core Team. 2019. *R: A Language and Environment for Statistical
Computing*. Vienna, Austria: R Foundation for Statistical Computing.
<https://www.R-project.org/>.

</div>

<div id="ref-cancer2">

Staff, Mayo Clinic. 2018. “Recurrent Breast Cancer.” Mayo Clinic.
<https://www.mayoclinic.org/diseases-conditions/recurrent-breast-cancer/symptoms-causes/syc-20377135>.

</div>

<div id="ref-Altair2018">

VanderPlas, Jacob, Brian Granger, Jeffrey Heer, Dominik Moritz, Kanit
Wongsuphasawat, Arvind Satyanarayan, Eitan Lees, Ilia Timofeev, Ben
Welsh, and Scott Sievert. 2018. “Altair: Interactive Statistical
Visualizations for Python.” *Journal of Open Source Software*, December.
<https://doi.org/10.21105/joss.01057>.

</div>

<div id="ref-Python">

Van Rossum, Guido, and Fred L. Drake. 2009. *Python 3 Reference Manual*.
Scotts Valley, CA: CreateSpace.

</div>

<div id="ref-walt2011numpy">

Walt, Stéfan van der, S Chris Colbert, and Gael Varoquaux. 2011. “The
Numpy Array: A Structure for Efficient Numerical Computation.”
*Computing in Science & Engineering* 13 (2): 22–30.

</div>

<div id="ref-tidyverse">

Wickham, Hadley. 2017. *Tidyverse: Easily Install and Load the
’Tidyverse’*. <https://CRAN.R-project.org/package=tidyverse>.

</div>

<div id="ref-knitr">

Xie, Yihui. 2014. “Knitr: A Comprehensive Tool for Reproducible Research
in R.” In *Implementing Reproducible Computational Research*, edited by
Victoria Stodden, Friedrich Leisch, and Roger D. Peng. Chapman;
Hall/CRC. <http://www.crcpress.com/product/isbn/9781466561595>.

</div>

</div>
