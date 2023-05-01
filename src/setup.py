from setuptools import setup, find_packages


setup(
    name="Hackaton Teamate Statistical",
    version="0.0.1",
    packages=find_packages(exclude=["tests", "test", "*.tests", "tests.*", "*.tests.*"]),
    install_requires=[
        "gunicorn==20.0.4",
        "flask==2.3.2",
        "requests==2.22.0",
        "werkzeug==1.0.0",
        "cachelib==0.1",
        "pymongo==3.4",
        "six==1.10.0",
        "python-dateutil==2.1.0",
        "Pillow",
        "mongoengine==0.19.1",
        "python-dotenv>=0.11.0",
        "pyjwt"
    ],
    author="dongnt",
    author_email="dongnt@appota.com",
    description="this project is Hackathon AppotaPay Internal Day, it is project manage time checkin,checkout and give statistical in app AppotaEwallet",
    url="https://git.appota.com/appotapay/teamate-statistical",
    python_requires=">=3.7",
    classifiers = [
        "Framework :: Flask",
        "Framework :: Pytest",
        "Framework :: tox",
        "Natural Language :: Vietnamese",
        "Programming Language :: Python :: 3.7"
    ]
)
