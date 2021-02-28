from distutils.core import setup
setup(
  name = 'flask-middleware',        
  packages = ['flask-middleware'],  
  version = '1.0',      
  license='MIT',        
  description = 'Flask middleware for flask based app on UniAuth',  
  author = 'Some Name',                   
  author_email = 'your.email@domain.com',     
  url = 'https://github.com/user/reponame',  
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',   
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   
  install_requires=[           
          'flask',
        ],
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3',     
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)