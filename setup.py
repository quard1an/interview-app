from setuptools import find_packages, setup

setup(
    name='interview-app',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='A simple Django project for technical interview',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/interview-app',
    author='Your Name',
    author_email='your.email@example.com',
    install_requires=[
        'Django>=3.2,<4.0',
        'celery>=5.1.0',
        'redis>=3.5.3',
        'gunicorn>=20.1.0',
        'psycopg2>=2.9.1',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    python_requires='>=3.7',
)

