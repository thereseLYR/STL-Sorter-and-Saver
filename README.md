# STL-Sorter-and-Saver
Python-based utility to unzip archives from thingiverse, show thumbnails with matplotlib, and decide whether to save or delete the file.

# How-to:
1) Dump all zip files in a single folder, with each of the utilities in the same folder.
2) Run stl_saver.py. 
3) If you notice certain trends in your files (e.g. all files with names containing 'parametric' are unsuitable for your use, create a file called DELETE_THESE.csv and run Zip_blacklister.py
4) Similarly, useful files can be autosaved with SAVE_THESE.csv and Zip_whitelister.py
5) Once all files have been classified (i.e. black/whitelisted), use Zip_Deleter.py to mass-remove them. Do note that files removed with this emthod are unrecoverable.
