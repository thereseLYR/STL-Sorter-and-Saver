import glob
import os
import zipfile

from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

TO_SAVE_DIR = 'SAVE_THESE.csv'
TO_DELETE_DIR = 'DELETE_THESE.CSV'


def main():
	zip_file_paths = glob.glob('./*.zip')

	for zip_path in zip_file_paths:
		stripped_path = zip_path.strip('.\\')
		print(f"opening {stripped_path}")

		fnames = unzip_and_display_stls(zip_path)

		print(f"{zip_path} contains:")
		print('\t'.join(fnames))
		print("Keep file? (y/n): ", end="")
		option = input()
		option = option.strip().lower()

		if option == "y":
			f = open(TO_SAVE_DIR, "a")  # open in append mode
			f.write(stripped_path+"\n")
			f.close()
		elif option == "n":
			f = open(TO_DELETE_DIR, "a")
			f.write(stripped_path + "\n")
			f.close()


def display_stl(path):
	figure = pyplot.figure(path)
	axes = mplot3d.Axes3D(figure)

	your_mesh = mesh.Mesh.from_file(path)
	axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

	scale = your_mesh.points.flatten('A')
	axes.auto_scale_xyz(scale, scale, scale)
	# axes.auto_scale_xyz(100, 100, 100)

	pyplot.show()


def unzip_and_display_stls(path): 
	with zipfile.ZipFile(path, 'r') as zip_ref:
		files = zip_ref.namelist()
		stl_files = [f for f in filter(lambda x: x.lower().endswith('.stl'), files)]
		
		for fname in stl_files:
			zip_ref.extract(fname)
			display_stl('./'+fname)
			os.remove('./'+fname)

	return stl_files


if __name__ == '__main__':
	main()