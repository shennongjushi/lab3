nosetests --with-xunit --all-modules --traverse-namespace --with-coverage ExperimentTest.py --cover-inclusive >& result.text
python -m coverage xml --include=Experiment.py,ExperimentTest.py
pylint -f parseable -d I0011,R0801 Experiment.py | tee pylint.out
