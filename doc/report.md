Identifying strong predictors of breast cancer recurrence
================
Fanli Zhou
2020/1/23 (updated: 2020-02-06)

  - [Summary](#summary)
  - [Introduction](#introduction)
  - [Methods](#methods)
      - [Data](#data)
      - [Analysis](#analysis)
  - [Results and Discussion](#results-and-discussion)
  - [References](#references)

# Summary

We explored to use a logistic regression model to identify strong
predictors of breast cancer recurrence. Based on the feature weights
assigned in the model, we found that degrees of malignancy are very
strong predictors of breast cancer recurrence. The other two predictors,
including being in the age 60-69 group and having cancer in the right-up
of the breast quadrants, are also among the top five features with the
highest absolute weight values. Our model didn’t perform well on unseen
data, with a fair accuracy score of 0.71 and a low recall score of 0.62.
The low recall score is likely due to the data imbalance problem noticed
in the training data set. If time permits, we would like to explore some
advanced methods to handle the imbalanced data situation and try some
advanced feature selection methods to build a better model.

# Introduction

Breast cancer is a type of cancer that develops in the breast. With
around 0.3 million women are estimated to be diagnosed with breast
cancer in 2019 alone, breast cancer is the second most common cancer
found in women (Cancer.Net 2019). Breast cancer may come back after the
initial treatment, known as breast cancer recurrence (Staff 2018). Based
on a medical study in 2010, breast cancer has a high recurrence rate of
around 40% (Halls 2019). Although the cause of breast cancer recurrence
is not clear, some factors such as age and the tumor size are known to
affect the recurrence risk (Staff 2018).

In this project, we attempt to answer the question: What are the
strongest predictors of breast cancer recurrence? Answering this
question will help identify patients who have high risk of breast cancer
recurrence. Once we can identify patients with high recurrence risk, we
can give patients corresponding treatments to help prevent recurrence
events. Besides, finding out factors related to breast cancer recurrence
may shed light on understanding the cause of breast cancer recurrence.
Thus, it’s important to identify strong predictors of breast cancer
recurrence.

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
variables in the original data set were used to fit the model. Features,
including the tumor size and ranges of the number of axillary lymph
nodes, were converted to the average number and used as numeric
variables, while other features were treated as categorical variables.
The hyperparameter `C` for logistic regression was chosen with 5-fold
cross-validation based on the recall score. The Python programming
language (Van Rossum and Drake 2009), the R programming language (R Core
Team 2019) and the following Python/R packages were used: Pandas
(McKinney 2010), NumPy (Oliphant 2006, 1:@walt2011numpy), Altair
(VanderPlas et al. 2018), scikit-learn (Pedregosa et al. 2011),
Matplotlib(Hunter 2007), docopt (de Jonge 2018), knitr (Xie 2014),
tidyverse (Wickham 2017), cowplot (Wilke 2019), ggridges (Wilke 2018).
The code used to perform the analysis and create this report can be
found here: <https://github.com/UBC-MDS/DSCI_522_Group_301>.

# Results and Discussion

Before exploring any features, We first analyzed the rate of breast
cancer recurrence in the training data set. Only around 29.5% of the
patients had breast cancer recurrence events, while 70.5% of them don’t
have any recurrence events. So the training data set is not well
balanced, and we decided to address this question by scoring our model
with metrics such as the recall score.

Some factors such as “younger age, particularly those under age 35” and
“larger tumor size” are known to increase the risk of breast cancer
recurrence (Staff 2018). To explore the training data set, we would like
to first look at how breast cancer recurrence is related to age and
tumor size.

To understand the relation between breast cancer recurrence events and
age, we made a plot to show the age distribution of patients with or
without breast cancer recurrence. Based on figure 1A, most of the
patients in the training data set are between the ages of 30 and 69.
Patients at ages 30-39 are more likely to have breast cancer recurrence
than other age groups.

To study the relation between breast cancer recurrence events and the
tumor size, we first converted the tumor size range to the corresponding
average tumor size and then visualized the average tumor size
distribution of patients with or without breast cancer recurrence. From
figure 1B, we see that the 0.25 quantile and the mean of the average
tumor size of patients with breast cancer recurrence are bigger than
those without breast cancer recurrence. So “larger tumor size” is
related to breast cancer recurrence events.

<div class="figure">

<img src="../results/data_analysis.png" alt="Figure 1. Breast cancer recurrence is related to age and average tumor size in the training data set." width="100%" />

<p class="caption">

Figure 1. Breast cancer recurrence is related to age and average tumor
size in the training data set.

</p>

</div>

Known that the data set reflects the relation between breast cancer
recurrence and age or the tumor size, we then started to look for
features that are good at predicting breast cancer recurrence. We
decided to train a simple logistic regression model to calculate weights
for each feature in the training data set. We used 5-fold
cross-validation with the recall score to determine the performance of a
logistic regression model. We observed that the optimized hyperparameter
`C` for logistic regression is 1. To address the data imbalance problem,
we adjuested the threshold of the logistic regression mode primarily
based on the recall score, and we observed that the best threshold is
0.22.

Table 1 shows feature weights from our best logistic regression model.
The top five features with the highest absolute weight values are from
the categories of the degree of malignancy, age, and cancer location on
the breast quadrants. The degree of malignancy is clearly a strong
predictor of breast cancer recurrence, with a degree of 3 strongly
(meaning a high absolute weight value) related to “recurrence” and a
degree of 1 or 2 strongly related to “no recurrence”. The feature, being
in the age 60-69 group, has a high positive weight value, but the
overall trending of weights as age increases is confusing. Besides,
having cancer in the right-up of the breast quadrants is another strong
predictor. However, some factors that are known related to breast cancer
recurrence, including “younger age, particularly those under age 35” and
“larger tumor size” (Staff 2018), didn’t stand out in this analysis.

| features                                   | weights | abs(weights) |
| :----------------------------------------- | ------: | -----------: |
| malignancy\_degree\_3                      |    0.86 |         0.86 |
| malignancy\_degree\_2                      |  \-0.62 |         0.62 |
| age\_group\_60-69                          |    0.51 |         0.51 |
| malignancy\_degree\_1                      |  \-0.49 |         0.49 |
| position\_on\_breast\_quadrant\_right\_up  |    0.46 |         0.46 |
| radiation\_therapy\_no                     |  \-0.44 |         0.44 |
| menopause\_age\_premenopause               |    0.42 |         0.42 |
| age\_group\_70-79                          |  \-0.42 |         0.42 |
| menopause\_age\_great\_than\_40            |  \-0.38 |         0.38 |
| position\_on\_breast\_quadrant\_left\_up   |  \-0.33 |         0.33 |
| avgerage\_axillary\_lymph\_nodes           |    0.30 |         0.30 |
| menopause\_age\_less\_than\_40             |  \-0.30 |         0.30 |
| cap\_node\_presence\_no                    |  \-0.29 |         0.29 |
| position\_on\_breast\_right                |  \-0.29 |         0.29 |
| age\_group\_20-29                          |  \-0.22 |         0.22 |
| radiation\_therapy\_yes                    |    0.18 |         0.18 |
| position\_on\_breast\_quadrant\_central    |  \-0.18 |         0.18 |
| avgerage\_tumor\_size                      |    0.12 |         0.12 |
| position\_on\_breast\_quadrant\_left\_low  |  \-0.12 |         0.12 |
| age\_group\_50-59                          |  \-0.11 |         0.11 |
| position\_on\_breast\_quadrant\_right\_low |  \-0.09 |         0.09 |
| age\_group\_40-49                          |  \-0.04 |         0.04 |
| cap\_node\_presence\_yes                   |    0.04 |         0.04 |
| position\_on\_breast\_left                 |    0.03 |         0.03 |
| age\_group\_30-39                          |    0.02 |         0.02 |

Table 1. Features and corresponding weights in the logistic regression
model.

Our model didn’t perform well on either the training or test data set.
As shown in table 2, the training data set has a fair recall score, but
very low precision and f1 scores. It suggests that we didn’t build a
good model to separate “recurrence” and “no-recurrence” events even in
the training data set. Furthermore, the test data set has a much lower
recall score. So it’s likely that the model is over-fitted. The ROC
report of the test data set in figure 2 also shows that our model
performed poorly at predicting “recurrence” events.

| dataset | accuracy | recall | precision | f1 score | auc score |
| :------ | -------: | -----: | --------: | -------: | --------: |
| train   |     0.66 |   0.77 |      0.46 |     0.57 |      0.69 |
| test    |     0.71 |   0.62 |      0.50 |     0.56 |      0.68 |

Table 2. Training and test data scores.

<div class="figure">

<img src="../results/roc_report.png" alt="Figure 2. ROC curve of the test data set." width="50%" />

<p class="caption">

Figure 2. ROC curve of the test data set.

</p>

</div>

If time permits, we want to improve our model in two ways. First, we
need to find a better way to handle data imbalance other than just
ajusting the scoring method. With an advanced approach to deal with the
data imbalance problem, we expect to see a big improvement in the
recall, precision, and f1 scores for both training and test data.
Second, we want to explore other feature selection methods to help us
decide which predictors are better over others. We also need some advice
and experience in handling categorical variables during feature
selection.

# References

<div id="refs" class="references">

<div id="ref-cancer1">

Cancer.Net. 2019. “Breast Cancer: Statistics.” Cancer.Net.
<https://www.cancer.net/cancer-types/breast-cancer/statistics>.

</div>

<div id="ref-docopt">

de Jonge, Edwin. 2018. *Docopt: Command-Line Interface Specification
Language*. <https://CRAN.R-project.org/package=docopt>.

</div>

<div id="ref-Dua2019">

Dua, Dheeru, and Casey Graff. 2017. “UCI Machine Learning Repository.”
University of California, Irvine, School of Information; Computer
Sciences. This breast cancer domain was obtained from the University
Medical Centre, Institute of Oncology, Ljubljana, Yugoslavia. Thanks go
to M. Zwitter; M. Soklic for providing the data.
<http://archive.ics.uci.edu/ml>.

</div>

<div id="ref-cancer3">

Halls, Dr. 2019. “Moose & Doc Breast Cancer.” Cross Cancer Institute in
Edmonton. <https://breast-cancer.ca/chance-cure/>.

</div>

<div id="ref-Hunter:2007">

Hunter, J. D. 2007. “Matplotlib: A 2D Graphics Environment.” *Computing
in Science & Engineering* 9 (3): 90–95.
<https://doi.org/10.1109/MCSE.2007.55>.

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

<div id="ref-pedregosa2011scikit">

Pedregosa, Fabian, Gaël Varoquaux, Alexandre Gramfort, Vincent Michel,
Bertrand Thirion, Olivier Grisel, Mathieu Blondel, et al. 2011.
“Scikit-Learn: Machine Learning in Python.” *Journal of Machine
Learning Research* 12 (Oct): 2825–30.

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

<div id="ref-ggridges">

Wilke, Claus O. 2018. *Ggridges: Ridgeline Plots in ’Ggplot2’*.
<https://CRAN.R-project.org/package=ggridges>.

</div>

<div id="ref-cowplot">

———. 2019. *Cowplot: Streamlined Plot Theme and Plot Annotations for
’Ggplot2’*. <https://CRAN.R-project.org/package=cowplot>.

</div>

<div id="ref-knitr">

Xie, Yihui. 2014. “Knitr: A Comprehensive Tool for Reproducible Research
in R.” In *Implementing Reproducible Computational Research*, edited by
Victoria Stodden, Friedrich Leisch, and Roger D. Peng. Chapman;
Hall/CRC. <http://www.crcpress.com/product/isbn/9781466561595>.

</div>

</div>
