skipper-cli
=========

*Skipper Internal Tools untuk kebutuhan continuous integration and continuous delivery.*


Syarat
-----

Python 3.6.4
pip 9.0.1


Tujuan
-------

Tujuan dibuatnya script ini untuk mempermudah proses development dan deploy dengan satu interface.

Yang akan terintegrasi dengan beberapa tools automation dan notification sehingga mempermudah
semua engineer, QA serta Product Owner untuk melakukan monitoring.

Ide ini muncul, melihat proses development dan deploy yang begitu berbelit-belit dan
sangat tidak konsisten di setiap environment.

Implementasi yang akan ditambahkan adalah docker support, untuk memastikan bahwa setiap environment
memiliki konsistensi.


Penggunaan
-----

Instalasi dapat dilakukan dengan 2 metode, otomatis atau manual.

    Otomatis:
    
    Pastikan OS sudah terinstall build-essential. Setelah melakukan clone project,
    silahkan jalankan command dibawah ini::
    
        $ make

    Make hanya akan menjalankan proses installasi, tanpa menjalankan proses test dan yang lain.

    Manual:

    Setelah melakukan clone project, jalankan command dibawah ini::
    
        $ pip install -e .[test]

    Jika kamu developer/contributor, untuk melakukan test, jalankan command di bawah ini::
    
        $ python setup.py test

    Jika ingin melakukan publish ke (`PyPI <https://pypi.python.org/pypi>`_).
    Ikuti langkah-langkah dibawah ini::

    $ python setup.py sdist bdist_wheel
    $ twine upload dist/*

    Proses publish ke PyPI menggunakan tool ``twine upload``.
    Pastikan `twine <https://pypi.python.org/pypi/twine>`_ tool) sudah terinstall.