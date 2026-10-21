from pathlib import Path
from PIL import Image, ImageChops
import json
import argparse

parser=argparse.ArgumentParser(description='Remove detached top/bottom fragments from the six running frames.')
parser.add_argument('--input',type=Path,required=True)
parser.add_argument('--output-dir',type=Path,required=True)
args=parser.parse_args()
folder=args.output_dir
folder.mkdir(parents=True,exist_ok=True)
src=args.input
original=Image.open(src).convert('RGBA')
image=original.copy()
report=[]
for col in range(6):
    removed=0
    for y in list(range(20))+list(range(190,208)):
        for x in range(192):
            pos=(col*192+x,7*208+y)
            if image.getpixel(pos)[3]:
                image.putpixel(pos,(0,0,0,0));removed+=1
    report.append({'frame':col,'removed_pixels':removed})
    # Character region must remain exactly unchanged.
    box=(col*192,7*208+20,(col+1)*192,7*208+190)
    assert ImageChops.difference(original.crop(box),image.crop(box)).getbbox() is None
assert ImageChops.difference(original.crop((0,0,1536,1456)),image.crop((0,0,1536,1456))).getbbox() is None
assert ImageChops.difference(original.crop((0,1664,1536,1872)),image.crop((0,1664,1536,1872))).getbbox() is None
target=folder/'seele-pet-clean-running-v3.png'
image.save(target)
preview=Image.new('RGB',(1152,416),(224,229,240))
frames=[]
for col in range(6):
    for j,source in enumerate([original,image]):
        cell=source.crop((col*192,1456,(col+1)*192,1664))
        preview.paste(cell,(col*192,j*208),cell)
    cell=image.crop((col*192,1456,(col+1)*192,1664))
    bg=Image.new('RGB',(192,208),(224,229,240));bg.paste(cell,mask=cell.getchannel('A'));frames.append(bg)
preview.save(folder/'running-edge-before-after-v3.jpg')
frames[0].save(folder/'running-clean-preview-v3.gif',save_all=True,append_images=frames[1:],duration=[120]*5+[220],loop=0)
(folder/'running-edge-cleanup-v3.json').write_text(json.dumps({'row':7,'frames':report,'removed_total':sum(r['removed_pixels'] for r in report),'character_region_unchanged':True,'other_rows_unchanged':True},indent=2),encoding='utf8')
print(json.dumps(report))
