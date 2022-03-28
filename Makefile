# Arcane incantation to print all the other targets, from https://stackoverflow.com/a/26339924
help:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

# Recipe for activating the conda environment within the sub-shell as a target, from https://stackoverflow.com/a/55696820/13749426
.ONESHELL:

# Need to specify bash in order for conda activate to work, otherwise it will try to use the default shell, which is "zsh" in this case
SHELL = /bin/bash

# Note that the extra activate is needed to ensure that the activate floats env to the front of PATH, otherwise it will not work
CONDA_ACTIVATE = source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate

# Create conda env from env.yml and compile and install exact pip packages
conda-pip:
	conda env update --prune -f env.yml
	$(CONDA_ACTIVATE) vortex3.9
	pip-compile requirements/req.in
	pip-sync requirements/req.txt
pip-tools:
	pip-compile requirements/req.in
	pip-sync requirements/req.txt

train-test-split:
	$(CONDA_ACTIVATE) vortex3.9
	cd vortex/utils 
	python test_train_split.py --datadir="../../data/processed/threshZero_data/AN_DATA" --split=0.2 --train_output="../../data/processed/train" --test_output="../../data/processed/test" --image_ext="jpg"


# Convert keras model to TFJS
con-tfjs:
	model_dir=./vortex/artifacts/border_box/detector; \
	target_dir=./vortex/artifacts/border_box/tfjs/detector; \
	tensorflowjs_converter --input_format keras \
                       $$model_dir.h5 \
                       $$target_dir
	@echo -n "TFJS model.json saved at './vortex/artifacts/border_box/tfjs'"