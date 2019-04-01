"""
redistribute the dataset files from folds to categories
"""
import os
import shutil

URBAN_CSV = 'UrbanSound8K_original.csv';
URBAN_FOLD_PATH = 'I:/UrbanSound8KunifiedSampling'
URBAN_CATEGORY_PATH = 'I:/UrbanSound8KunifiedSampling/tocategory'

with open(URBAN_CSV) as csvfile:

    csvfile.readline()  # skip first row
    for row in csvfile:
        fields = row.strip().split(",")  # make Into fields

        if not os.path.exists(os.path.join(URBAN_CATEGORY_PATH, fields[-1])):
            os.mkdir( os.path.join(URBAN_CATEGORY_PATH, fields[-1]))

        src_path = os.path.join(URBAN_FOLD_PATH, 'fold'+ fields[-3], fields[0])
        dst_path = os.path.join(URBAN_CATEGORY_PATH, fields[-1], fields[0])
        shutil.copy(src_path, dst_path)
        print(src_path+ '   '+ dst_path)



