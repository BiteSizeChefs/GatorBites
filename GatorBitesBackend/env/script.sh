# Have the source code (src/ and static_cdn/ and a venv setup)
## virtualenv env
if [[ ! -f "$1" && "$1" == "install" ]]; then
    pip install django
    pip install Pillow
    pip install djangorestframework django-cors-headers 
fi

source bin/activate
cd src/
chmod +x runServer.sh
./runServer.sh