echo "BUILD START"
python 3.9.1 -m pip install -r requirements.txt
python 3.9.1 manage.py collectstatic --noinput --clear
echo "BUILD END"
