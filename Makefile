venv:
	python3 -m venv .venv
	echo "Please run 'source .venv/bin/activate'"
dev:
	pip install -r requirements.txt

test:
	PYTHONPATH=src pytest test.py

