# breast cancer data pipe

all: doc/report.md doc/report.html 

# download data
data/raw_data/breast_cancer_raw.csv: src/download_save_data.py
	python src/download_save_data.py --url="https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer/breast-cancer.data" --output="data/raw_data/breast_cancer_raw.csv" 

# pre-processing/clean data 
data/clean_data/breast_cancer_clean.csv data/clean_data/breast_cancer_train.csv data/clean_data/breast_cancer_test.csv results/train_info.csv: src/wrangled_data.py data/raw_data/breast_cancer_raw.csv
	python src/wrangled_data.py --input="raw_data/breast_cancer_raw.csv" --output=clean_data

# create EDA figures/tables 
results/data_analysis.png: src/visualization.R data/clean_data/breast_cancer_train.csv data/clean_data/breast_cancer_test.csv
	Rscript src/visualization.R --train="data/clean_data/breast_cancer_train.csv"  --out_dir=results

# data analysis
results/features_and_weights.csv results/scores.csv results/model_info.csv results/roc_report.png: src/analysis.py data/clean_data/breast_cancer_clean.csv
	python src/analysis.py --input="clean_data/breast_cancer_clean.csv" --output=results

# render report
doc/report.md doc/report.html: doc/report.Rmd doc/breast_cancer_refs.bib results/model_info.csv results/train_info.csv results/scores.csv results/features_and_weights.csv results/roc_report.png results/data_analysis.png
	Rscript -e "rmarkdown::render('doc/report.Rmd', output_format = 'github_document')"

clean: 
	rm -rf data/clean_data/*csv data/raw_data/*csv
	rm -rf results/*.csv results/*.png
	rm -rf doc/report.md doc/report.html
			