import glob
import os
import zipfile


# to keep: .PDF, .SCAD
TO_SAVE_DIR = 'SAVE_THESE.csv'
# WHITELIST_COUNT = 0


def main():
    zip_file_paths = glob.glob('./*.zip')

    for zip_path in zip_file_paths:
        stripped_path = zip_path.strip('.\\')
        print(f"opening {stripped_path}")

        fnames = unzip_and_filter(zip_path)

        print(f"{zip_path} contains:")
        print('\t'.join(fnames))
    print('Done Whitelisting. Files Whitelisted:')


def unzip_and_filter(path):
    with zipfile.ZipFile(path, 'r') as zip_ref:
        files = zip_ref.namelist()
        stl_files = [f for f in filter(lambda x: x.lower().endswith('.zip'), files)]

        for fname in stl_files:
            zip_ref.extract(fname)
            os.remove('./' + fname)

            stripped_path = path.strip('.\\')
            f = open(TO_SAVE_DIR, "a")
            f.write(stripped_path + "\n")
            f.close()
            # WHITELIST_COUNT += 1

    return stl_files


if __name__ == '__main__':
    main()