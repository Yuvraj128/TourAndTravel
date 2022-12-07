echo "BUILD START"
python3.9.1 -m pip install -r requirements.txt
python3.9.1 manage.py collectstatic --noinput --clear
echo "BUILD END"
