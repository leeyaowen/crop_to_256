from PIL import Image
import glob
import os


def crop_to256():
    InputPath = input('InputPath=?\n')
    OutputPath = input('OutputPath=?\n')
    all_file = sorted(glob.glob('%s/*.jpg' % InputPath), key=os.path.getmtime)
    if len(all_file) == 0:
        print('no file!\n')
        return None

    for filename in all_file:
        try:
            with Image.open(filename) as img:
                img_crop = img.crop((0, 0, 7295, 3694))
                img_256 = img_crop.resize((256, 256)).save(OutputPath + os.path.basename(filename))
        except Exception:
            print('error in %s\n' % filename)
            continue


while __name__ == '__main__':
    crop_to256()
