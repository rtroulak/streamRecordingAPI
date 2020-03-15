from setuptools import setup

with open('requirements.txt') as fp:
    install_requires = fp.read()

setup(
    name='streamRecordingAPI',
    packages=['streamRecordingAPI'],
    version='0.1',
    description='A recording  CRUD RestAPI',
    author='Troulakis Georgios Rafail',
    author_email='rtroulak@protonmail.com',
    url='https://github.com/rtroulak/streamRecordingAPI',
    download_url='https://github.com/rtroulak/streamRecordingAPI/archive/master.zip',
    keywords=['RestAPI', 'recording', 'stream', 'sqlAlchemy'],
    classifiers=['Topic :: RestAPI', 'Topic :: Software Development', 'Topic :: System',
                 'Topic :: Recording', 'Topic :: Streaming'],
    install_requires=install_requires
)
