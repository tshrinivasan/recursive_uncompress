import glob
import os


indir = input("Enter Source Direcoty (Full Path) :")

outdir = input("Enter Destination Directory to extract the compressed directories :")

	
if not os.path.exists(outdir):
    os.makedirs(outdir)


for filename in glob.iglob( indir + '/**/*tar.gz', recursive=True):
    print("Extracting " + filename)

    extract_tar = "tar xzf " + filename + " -C " + outdir
    os.system(extract_tar)



for filename in glob.iglob( indir + '/**/*tar.bz2', recursive=True):
    print("Extracting " + filename)

    extract_tar_bz2 = "tar xjf " + filename + " -C " + outdir
    os.system(extract_tar_bz2)



for filename in glob.iglob( indir + '/**/*.zip', recursive=True):
    print("Extracting " + filename)

    extract_zip = "unzip " + filename + " -d " + outdir
    os.system(extract_zip)



for filename in glob.iglob( indir + '/**/*.7z', recursive=True):
    print("Extracting " + filename)


    extract_7z = "7z x -t7z " + filename + " -o" + outdir
    os.system(extract_7z)

        